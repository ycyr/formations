# 📄 Cheat Sheet – Définition YAML d’un StatefulSet Kubernetes

> Résumé des champs spécifiques à `kind: StatefulSet`, avec exemples et rappels pratiques.

---

## 🔹 Exemple minimal de StatefulSet

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: "web"         # 👈 Headless service obligatoire
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
        volumeMounts:
        - name: data
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
```

---

## 🔹 Champs spécifiques à un StatefulSet

| Champ                | Rôle                                                   |
|----------------------|--------------------------------------------------------|
| `serviceName`        | Nom du **headless service** utilisé pour le DNS        |
| `volumeClaimTemplates`| Génére un **PVC dédié** pour chaque Pod               |
| `replicas`           | Nombre de Pods (ex: `web-0`, `web-1`, `web-2`)         |

---

## 🔄 Nom des objets générés

| Ressource     | Format                         |
|---------------|--------------------------------|
| Pods          | `web-0`, `web-1`, `web-2`      |
| PVCs          | `data-web-0`, `data-web-1`, …  |
| DNS           | `web-0.web.default.svc`        |

---

## ✅ Différences clés avec un Deployment

| Aspect              | Deployment          | StatefulSet         |
|---------------------|---------------------|----------------------|
| Noms de Pods        | Dynamiques          | Stables (`web-0`)    |
| Ordre de démarrage  | Parallèle           | Séquentiel           |
| PVCs                | Partagés possibles  | 1 PVC / Pod unique   |
| Usage               | Frontend, stateless | BDD, Kafka, Redis…   |

---

## 📘 Schéma structurel

```
StatefulSet "web"
├── Pod: web-0 ── PVC: data-web-0
├── Pod: web-1 ── PVC: data-web-1
└── Pod: web-2 ── PVC: data-web-2

Résolution DNS : web-0.web.default.svc.cluster.local
```

---

## ✅ Commandes utiles

```bash
kubectl get statefulsets
kubectl describe statefulset web
kubectl get pods -l app=web
kubectl get pvc -l app=web
kubectl delete pod web-0  # recréation automatique
```

---

## 📥 Générer le YAML (base) :

```bash
kubectl create statefulset demo --image=nginx --dry-run=client -o yaml > statefulset.yaml
```

---

📌 *N’oubliez pas : un Service headless (`clusterIP: None`) est requis avec le nom `serviceName` du StatefulSet.*
