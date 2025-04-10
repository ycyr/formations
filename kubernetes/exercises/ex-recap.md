

# 🧪 TP – Révision Jour 1 avec `httpbin`

## 🎯 Objectifs pédagogiques

- Créer un namespace isolé
- Déployer un Pod avec des labels et annotations
- Gérer la scalabilité avec un ReplicaSet et un Deployment
- Observer la distribution des Pods sur les nœuds
- Créer un Service ClusterIP et tester la connectivité
- Comprendre l'utilité d'une image comme `httpbin`

---

## 🟦 Étape 1 – Créer le namespace

```bash
kubectl create namespace tp-revision-jour1
```

---

## 🟦 Étape 2 – Créer un Pod `httpbin` avec labels et annotations

✅ Fichier : `pod-httpbin.yaml`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: httpbin-pod
  namespace: tp-revision-jour1
  labels:
    app: httpbin
  annotations:
    version: "v1"
spec:
  containers:
  - name: httpbin
    image: kennethreitz/httpbin
    ports:
    - containerPort: 80
```

```bash
kubectl apply -f pod-httpbin.yaml
kubectl get pods -n tp-revision-jour1 --show-labels
```

---

## 🟦 Étape 3 – Créer un ReplicaSet avec 2 réplicas

✅ Fichier : `rs-httpbin.yaml`
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: httpbin-rs
  namespace: tp-revision-jour1
spec:
  replicas: 2
  selector:
    matchLabels:
      app: httpbin
  template:
    metadata:
      labels:
        app: httpbin
    spec:
      containers:
      - name: httpbin
        image: kennethreitz/httpbin
        ports:
        - containerPort: 80
```

```bash
kubectl apply -f rs-httpbin.yaml
kubectl get pods -n tp-revision-jour1 -l app=httpbin
```

---

## 🟦 Étape 4 – Déployer avec un Deployment (rolling update + scaling)

✅ Fichier : `deployment-httpbin.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: httpbin-deploy
  namespace: tp-revision-jour1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: httpbin
      version: stable
  template:
    metadata:
      labels:
        app: httpbin
        version: stable
    spec:
      containers:
      - name: httpbin
        image: kennethreitz/httpbin
        ports:
        - containerPort: 80
```

```bash
kubectl apply -f deployment-httpbin.yaml
kubectl get deployments,replicasets,pods -n tp-revision-jour1
```

---

## 🟦 Étape 5 – Créer un Service pour exposer httpbin

✅ Fichier : `svc-httpbin.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: httpbin-svc
  namespace: tp-revision-jour1
spec:
  selector:
    app: httpbin
    version: stable
  ports:
  - port: 80
    targetPort: 80
```

```bash
kubectl apply -f svc-httpbin.yaml
kubectl get svc -n tp-revision-jour1
```

---

## 🟦 Étape 6 – Tester depuis un Pod dans le cluster

Lance un Pod client :
```bash
kubectl run curl --rm -it --image=curlimages/curl --namespace=tp-revision-jour1 -- sh
```

Depuis le shell :
```sh
curl http://httpbin-svc/ip
curl http://httpbin-svc/headers
curl http://httpbin-svc/get
```

🔍 Tu verras les infos suivantes :
- Ton IP (vue par le serveur)
- Les en-têtes HTTP
- Les paramètres de la requête

---

## 🟦 Étape 7 – Observer la distribution des Pods sur les nœuds

```bash
kubectl get pods -n tp-revision-jour1 -o wide
```

> ✅ Tu vois sur quels nœuds les Pods sont planifiés

---

## 🟦 Étape 8 – Nettoyage (optionnel)

```bash
kubectl delete ns tp-revision-jour1
```

---

## ✅ Résumé des notions utilisées

| Concept         | Ressource mise en œuvre              |
|------------------|--------------------------------------|
| Namespace         | `tp-revision-jour1`                  |
| Pod               | `httpbin-pod`                        |
| Labels / Annotations | Pour filtre & métadonnées       |
| ReplicaSet        | `httpbin-rs`                         |
| Deployment        | `httpbin-deploy`                     |
| Service           | `httpbin-svc`                        |
| DNS / Réseau      | Via Pod client + `curl`              |
| Nodes             | Répartition observée (`kubectl get pods -o wide`) |

---


