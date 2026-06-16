# 🧪 TP Intégratif – Déploiement complet d'une application multi-composants

## 🎯 Objectifs pédagogiques

Cet exercice réunit **tous les concepts vus jusqu'à présent** dans un scénario réaliste :

- Créer et organiser des namespaces avec labels et annotations
- Déployer une application avec un Deployment, des labels et une stratégie de rolling update
- Exposer l'application via un Service ClusterIP et un NodePort
- Tester la résilience (auto-réparation), le scaling et le rollback
- Programmer une tâche de maintenance avec un CronJob
- Vérifier la résolution DNS inter-namespaces

---

## 🗺️ Architecture cible

```
Namespace: tp-integratif
│
├── Deployment: app-web         (image: stefanprodan/podinfo:6.7.0)
│   └── ReplicaSet              (3 Pods avec labels app=web, tier=frontend)
│       └── Pods x3
│
├── Service ClusterIP: svc-web  (port 80 → 9898)
├── Service NodePort:  svc-web-ext (port 80 → 9898, nodePort: 30090)
│
└── CronJob: job-sante          (toutes les minutes, affiche l'état)

Namespace: tp-client            (pour tester le DNS inter-namespaces)
```

---

## 🟦 Étape 1 – Créer et annoter les namespaces

### ✅ `namespace-integratif.yaml`

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: tp-integratif
  labels:
    environnement: formation
    projet: app-web
  annotations:
    contact: "devops@formation.local"
    description: "Namespace principal du TP intégratif"
```

```bash
kubectl apply -f namespace-integratif.yaml
```

```bash
kubectl create namespace tp-client
```

### 🔍 Vérification

```bash
kubectl get ns tp-integratif -o yaml
kubectl get ns --show-labels
```

> 📌 Remarquez comment les labels permettent d'identifier et filtrer les namespaces.

---

## 🟦 Étape 2 – Déployer l'application avec un Deployment

### ✅ `deployment-web.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-web
  namespace: tp-integratif
  labels:
    app: web
    tier: frontend
    version: v1
  annotations:
    deploye-par: "equipe-formation"
    doc: "https://formation.local/app-web"
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
      tier: frontend
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: web
        tier: frontend
        version: v1
    spec:
      containers:
      - name: podinfo
        image: stefanprodan/podinfo:6.7.0
        ports:
        - containerPort: 9898
```

```bash
kubectl apply -f deployment-web.yaml
```

### 🔍 Observer la hiérarchie Deployment → ReplicaSet → Pods

```bash
kubectl get deployments -n tp-integratif
kubectl get replicasets -n tp-integratif
kubectl get pods -n tp-integratif --show-labels
```

> 📌 Notez le nommage : `app-web` → `app-web-xxxxx` → `app-web-xxxxx-yyyyy`

---

## 🟦 Étape 3 – Créer les Services

### ✅ `services-web.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: svc-web
  namespace: tp-integratif
  labels:
    app: web
spec:
  selector:
    app: web
    tier: frontend
  ports:
  - port: 80
    targetPort: 9898
    protocol: TCP
---
apiVersion: v1
kind: Service
metadata:
  name: svc-web-ext
  namespace: tp-integratif
  labels:
    app: web
    exposition: externe
spec:
  type: NodePort
  selector:
    app: web
    tier: frontend
  ports:
  - port: 80
    targetPort: 9898
    nodePort: 30090
```

```bash
kubectl apply -f services-web.yaml
```

```bash
kubectl get svc -n tp-integratif
```

---

## 🟦 Étape 4 – Tester l'accès depuis l'intérieur (ClusterIP + DNS)

### 4a – Accès depuis le même namespace

```bash
kubectl run curl-test --rm -it \
  --image=curlimages/curl \
  --namespace=tp-integratif \
  -- sh
```

Depuis le shell du Pod :

```sh
# Accès par nom court (même namespace)
curl http://svc-web

# Sortir
exit
```

### 4b – Accès depuis un autre namespace (DNS inter-namespaces)

```bash
kubectl run dns-client --rm -it \
  --image=wbitt/network-multitool \
  --namespace=tp-client \
  -- /bin/bash
```

Depuis le shell :

```sh
# ❌ Ne fonctionne pas (mauvais namespace)
curl svc-web

# ✅ Résolution DNS complète
curl svc-web.tp-integratif.svc.cluster.local

# Voir la config DNS
cat /etc/resolv.conf

exit
```

### 4c – Accès depuis l'extérieur (NodePort)

```bash
kubectl get nodes -o wide
# Repérer INTERNAL-IP

curl http://<INTERNAL-IP>:30090
```

---

## 🟦 Étape 5 – Tester la résilience (auto-réparation)

```bash
# Repérer le nom d'un Pod
kubectl get pods -n tp-integratif

# Supprimer un Pod
kubectl delete pod <nom-du-pod> -n tp-integratif

# Observer la recréation immédiate
kubectl get pods -n tp-integratif -w
```

> 📌 Appuyer sur `Ctrl+C` pour arrêter le watch.

💬 Le Deployment, via son ReplicaSet, recrée automatiquement le Pod supprimé.

---

## 🟦 Étape 6 – Tester le scaling

```bash
# Scale up à 5 Pods
kubectl scale deployment app-web --replicas=5 -n tp-integratif
kubectl get pods -n tp-integratif

# Scale down à 2 Pods
kubectl scale deployment app-web --replicas=2 -n tp-integratif
kubectl get pods -n tp-integratif
```

```bash
# Vérifier que le ReplicaSet n'a pas changé, seul le compte de Pods varie
kubectl get replicasets -n tp-integratif
```

---

## 🟦 Étape 7 – Mise à jour et rollback

### 7a – Mise à jour vers une nouvelle version

Modifier `deployment-web.yaml` : changer l'image de `6.7.0` vers `6.8.0` et le label `version: v2`

```yaml
        image: stefanprodan/podinfo:6.8.0
      labels:
        ...
        version: v2
```

```bash
kubectl apply -f deployment-web.yaml

# Suivre le rolling update en temps réel
kubectl rollout status deployment app-web -n tp-integratif

# Observer les deux ReplicaSets (ancien et nouveau)
kubectl get replicasets -n tp-integratif
kubectl get pods -n tp-integratif --show-labels
```

### 7b – Rollback vers la version précédente

```bash
kubectl rollout undo deployment app-web -n tp-integratif

# Vérifier que l'ancien ReplicaSet reprend le relais
kubectl get replicasets -n tp-integratif
kubectl get pods -n tp-integratif --show-labels
```

> 📌 Observez que le label `version` est revenu à `v1` sur les Pods.

---

## 🟦 Étape 8 – Filtrage avancé par labels

```bash
# Lister tous les Pods frontend
kubectl get pods -n tp-integratif -l tier=frontend

# Lister les Pods en version v1
kubectl get pods -n tp-integratif -l version=v1

# Lister tous les Services exposés en externe
kubectl get svc -n tp-integratif -l exposition=externe

# Ajouter une annotation dynamique sur le Deployment
kubectl annotate deployment app-web \
  derniere-revue="2026-06-15" \
  -n tp-integratif

kubectl get deployment app-web -n tp-integratif -o yaml | grep annotations -A 5
```

---

## 🟦 Étape 9 – CronJob de surveillance

### ✅ `cronjob-sante.yaml`

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: job-sante
  namespace: tp-integratif
  labels:
    app: maintenance
    type: healthcheck
spec:
  schedule: "*/1 * * * *"
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: check
            image: curlimages/curl
            command:
            - sh
            - -c
            - |
              echo "=== Vérification santé $(date) ==="
              curl -s http://svc-web/healthz && echo "✅ App en bonne santé" || echo "❌ App inaccessible"
          restartPolicy: OnFailure
```

```bash
kubectl apply -f cronjob-sante.yaml
```

```bash
# Observer le CronJob
kubectl get cronjob -n tp-integratif

# Attendre ~60 secondes, puis observer les Jobs générés
kubectl get jobs -n tp-integratif
kubectl get pods -n tp-integratif -l app=maintenance
```

```bash
# Lire les logs du dernier Pod créé par le CronJob
kubectl logs -n tp-integratif -l app=maintenance --tail=10
```

> 📌 Le CronJob appelle le Service ClusterIP `svc-web` depuis l'intérieur du namespace.

---

## 🟦 Étape 10 – Nettoyage

```bash
kubectl delete namespace tp-integratif
kubectl delete namespace tp-client
```

📌 Tous les objets (Deployment, Services, CronJob, Jobs, Pods) sont supprimés d'un coup.

---

## ❓ Questions de fin de TP

### 🧠 Q1 – Vision globale :

Listez tous les types d'objets Kubernetes que vous avez créés dans ce TP.
Pour chacun, indiquez sa responsabilité principale et quel autre objet le "supervise" (si applicable).

### 🧠 Q2 – Labels et sélection :

Dans ce TP, le Service `svc-web` sélectionne les Pods avec `app: web` **et** `tier: frontend`.
Que se passerait-il si vous ajoutiez manuellement un Pod avec uniquement `app: web` mais sans `tier: frontend` ?
Ce Pod recevrait-il du trafic ? Expliquez pourquoi.

### 💬 Q3 – Résilience et mise à jour :

Lors du rolling update (étape 7), la configuration `maxUnavailable: 0` et `maxSurge: 1` a été définie.
Qu'est-ce que cela garantit concrètement pendant la mise à jour ?
Quelle serait la différence avec `maxUnavailable: 1` et `maxSurge: 0` ?

### 💬 Q4 – CronJob et réseau interne :

Le CronJob appelle `http://svc-web/healthz` sans préciser de namespace dans l'URL.
Pourquoi cela fonctionne-t-il ici, alors que le même appel depuis `tp-client` aurait échoué ?

---

## ✅ Récapitulatif

| Concept                   | Objet utilisé          | Ce qui a été validé                                      |
| ------------------------- | ---------------------- | -------------------------------------------------------- |
| Organisation              | Namespace + Labels     | Isolation, filtrage, annotations dynamiques              |
| Résilience                | Deployment + RS        | Auto-réparation après suppression de Pod                 |
| Scalabilité               | `kubectl scale`        | Scale up/down sans recréer le Deployment                 |
| Mise à jour contrôlée     | Rolling update         | Nouveau RS créé, Pods remplacés progressivement          |
| Retour arrière            | `rollout undo`         | Ancien RS réactivé en une commande                       |
| Accès interne             | Service ClusterIP      | DNS court dans le namespace, DNS FQDN inter-namespace    |
| Accès externe             | Service NodePort       | Accès via IP du nœud + port statique                     |
| Tâche planifiée           | CronJob → Job → Pod    | Exécution périodique avec appel réseau interne           |
| Filtrage avancé           | Labels multi-critères  | Sélection précise avec plusieurs labels simultanément    |
