
# 🧪 Cheat Sheet – `kubectl` pour Kubernetes (Complet)

> Ce mémo résume toutes les commandes `kubectl` utiles couvertes durant la formation.

---

## 📦 OBJETS GÉNÉRAUX

```bash
kubectl get all
kubectl get pods,svc,deploy,ingress,statefulset
kubectl get <ressource> -n <namespace>
kubectl describe <ressource> <nom>
kubectl delete <ressource> <nom>
kubectl apply -f fichier.yaml
```

---

## 🏷️ LABELS & ANNOTATIONS

```bash
kubectl get pods --show-labels
kubectl get pods -l app=web
kubectl label pod mon-pod environment=dev
kubectl annotate pod mon-pod description='pod de test'

kubectl get pods -o jsonpath='{.items[*].metadata.annotations}'
```

---

## 📁 CONFIGMAPS & SECRETS

### 🔹 Créer un ConfigMap

```bash
kubectl create configmap mon-config --from-literal=MODE=prod
kubectl create configmap mon-config --from-file=monfichier.conf
```

### 🔹 Créer un Secret

```bash
kubectl create secret generic mon-secret --from-literal=DB_USER=admin
kubectl create secret generic mon-secret --from-file=credentials.txt
```

### 🔹 Lire et décoder

```bash
kubectl get configmap mon-config -o yaml
kubectl get secret mon-secret -o yaml
echo <valeur_base64> | base64 -d
```

---

## 💾 VOLUMES / PV / PVC

```bash
kubectl get pvc
kubectl get pv
kubectl describe pvc mon-pvc
```

---

## 🧬 STATEFULSET

```bash
kubectl get statefulsets
kubectl get pvc -l app=web
kubectl delete pod web-0  # recréation avec persistance
```

---

## ⏱️ JOBS / CRONJOBS

```bash
kubectl get jobs
kubectl get cronjobs
kubectl logs job/<job-name>
```

---

## 🧱 DEPLOYMENTS & PODS

```bash
kubectl create deployment mon-app --image=nginx
kubectl scale deployment mon-app --replicas=3
kubectl exec -it mon-pod -- sh
kubectl logs mon-pod
kubectl rollout status deployment mon-app
```

---

## 📡 SERVICES

```bash
kubectl expose deployment mon-app --type=NodePort --port=80
kubectl get svc
kubectl describe svc mon-service
```

---

## 🌐 INGRESS

```bash
kubectl apply -f ingress.yaml
kubectl get ingress
kubectl describe ingress mon-ingress
```

---

## 🧩 DNS & COMMUNICATION

```bash
kubectl exec -it pod-name -- nslookup service-name
kubectl exec -it pod-name -- curl http://service-name
kubectl exec -it pod-name -- curl http://service.namespace
```

---

## 🌐 NODES & PLANIFICATION

```bash
kubectl get nodes
kubectl describe node <node-name>
```

### 🔹 Affinité / Sélection par label

```bash
kubectl get nodes --show-labels
kubectl label node <node> disktype=ssd
```

Dans un Pod :
```yaml
nodeSelector:
  disktype: ssd
```

---

## 🗃️ NAMESPACES

```bash
kubectl get ns
kubectl create ns demo
kubectl delete ns demo
kubectl get pods -n demo
```

---

## 🧪 DEBUG

```bash
kubectl exec -it mon-pod -- sh
kubectl logs mon-pod
kubectl describe pod mon-pod
kubectl port-forward svc/mon-service 8080:80
```

---

## 🛠️ EXPLORATION & YAML

```bash
kubectl explain pod.spec.containers
kubectl create deployment mon-app --image=nginx --dry-run=client -o yaml > deploy.yaml
```

---

## ✅ RÉSUMÉ RAPIDE

| Ressource      | Créer           | Obtenir infos     | Supprimer        |
|----------------|------------------|--------------------|------------------|
| Pod            | `kubectl run`    | `get pods`         | `delete pod`     |
| Deployment     | `create deploy`  | `get deployments`  | `delete deploy`  |
| Service        | `expose`         | `get svc`          | `delete svc`     |
| Ingress        | `apply -f`       | `get ingress`      | `delete ingress` |
| PVC            | `apply -f`       | `get pvc`          | `delete pvc`     |
| ConfigMap      | `create configmap`| `get configmap`    | `delete configmap`|
| Secret         | `create secret`  | `get secret`       | `delete secret`  |
| Job / CronJob  | `apply -f`       | `get jobs` / `cronjobs` | `delete`     |

---

📌 *Utilise `-n <namespace>` pour travailler dans l’espace de noms approprié.*

