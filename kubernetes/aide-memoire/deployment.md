# 📄 Cheat Sheet – Définition YAML d’un Deployment Kubernetes

> Résumé des champs spécifiques au `kind: Deployment`, avec explications et structure commentée.

---

## 🔹 Exemple minimal de Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
  labels:
    app: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
        ports:
        - containerPort: 80
```

---

## 🔹 Champs spécifiques à un Deployment

| Champ          | Description                                         |
|----------------|-----------------------------------------------------|
| `replicas`     | Nombre de Pods souhaités                            |
| `selector`     | Obligatoire. Associe le Deployment à ses Pods       |
| `template`     | Template de Pod (identique à `kind: Pod`)           |
| `strategy`     | Définit le type de déploiement (rolling, recreate)  |
| `revisionHistoryLimit` | Nombre de rollbacks conservés              |

---

### 📌 Rappel sur la structure imbriquée :

```
Deployment
└── spec
    ├── replicas
    ├── selector
    └── template
        ├── metadata.labels
        └── spec.containers[]
```

✅ Les `labels` dans `template.metadata` **doivent correspondre** à ceux dans `selector.matchLabels`.

---

## 🔄 Mise à jour, Rollout & Rollback

### ➕ Mettre à jour l’image :
```bash
kubectl set image deployment/webapp nginx=nginx:1.26
```

### ⏳ Suivre le déploiement :
```bash
kubectl rollout status deployment webapp
```

### 🔁 Rollback :
```bash
kubectl rollout undo deployment webapp
```

---

## 🧠 `strategy` – Rolling update (par défaut)

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 25%
    maxSurge: 25%
```

| Champ             | Description                                |
|-------------------|--------------------------------------------|
| `maxUnavailable`  | Max de Pods indisponibles durant la MAJ   |
| `maxSurge`        | Max de Pods en plus temporaires           |

---

## ✅ Commandes utiles

```bash
kubectl get deployment
kubectl describe deployment webapp
kubectl rollout history deployment webapp
kubectl scale deployment webapp --replicas=5
```

---

## 📘 Liens entre objets

```
Deployment
   └── ReplicaSet(s)
         └── Pod(s)
```

📌 Chaque mise à jour crée un **nouveau ReplicaSet**.  
Le Deployment gère l’historique.

---

## 🧪 Générer un template YAML à modifier

```bash
kubectl create deployment demo --image=nginx --dry-run=client -o yaml > deployment.yaml
```

---

📌 *Utilisez `kubectl explain deployment.spec.template.spec` pour explorer la structure interne.*
