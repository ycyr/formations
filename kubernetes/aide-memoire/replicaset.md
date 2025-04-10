
# 📄 Kubernetes Cheat Sheet – ReplicaSet

---

## 🧠 Qu’est-ce qu’un ReplicaSet ?

Un **ReplicaSet** assure qu’un nombre souhaité de **Pods identiques** sont en exécution à tout moment.

- Contrôle les Pods via un **label selector**
- Peut recréer un Pod supprimé
- 📌 Utilisé **automatiquement** par les Deployments

---

## 🧩 Exemple minimal de ReplicaSet

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-replicaset
spec:
  replicas: 3
  selector:
    matchLabels:
      app: demo
  template:
    metadata:
      labels:
        app: demo
    spec:
      containers:
      - name: app
        image: httpd:2.4
        ports:
        - containerPort: 80
```

---

## 📘 Champs importants

| Champ         | Rôle                                                 |
|---------------|------------------------------------------------------|
| `replicas`    | Nombre de Pods souhaités                             |
| `selector`    | Critères de sélection des Pods                       |
| `template`    | Gabarit du Pod à créer (si manquant)                 |
| `matchLabels` | Doit **correspondre exactement** à `.template.labels`|

---

## ⚠️ Bonnes pratiques

- Évitez de modifier directement un ReplicaSet en production
- Utilisez un `Deployment` pour gérer les mises à jour
- Assurez-vous que le `selector` ne capture pas accidentellement d’autres Pods

---

## 🛠️ Commandes utiles

```bash
# Créer un RS depuis YAML
kubectl apply -f replicaset.yaml

# Lister les RS dans un namespace
kubectl get rs -n <namespace>

# Voir les Pods gérés par un RS
kubectl get pods -l app=demo

# Supprimer un Pod → il sera recréé
kubectl delete pod <nom>

# Supprimer le ReplicaSet (supprime aussi les Pods)
kubectl delete rs my-replicaset
```

---

## 🧠 Limitations du ReplicaSet seul

- ❌ Pas de gestion des mises à jour
- ❌ Pas de rollback automatique
- ✅ Gère uniquement la **disponibilité** (non la version)

➡️ Pour gérer le **cycle de vie applicatif complet**, utilisez un **Deployment**

---

## ✅ À retenir

| ✅ Utile pour...         | ❌ À éviter pour...           |
|--------------------------|------------------------------|
| Maintenir des Pods actifs| Mises à jour d’image         |
| Comportement déclaratif  | Rollback                     |
| Test simple ou démo      | Environnements de prod       |

```
