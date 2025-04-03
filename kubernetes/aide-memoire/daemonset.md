# 📄 Cheat Sheet – Définition YAML d’un DaemonSet Kubernetes

> Résumé de la structure YAML pour un `DaemonSet`, utilisé pour déployer un Pod sur chaque nœud du cluster.

---

## 🔹 Exemple minimal de DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-agent
spec:
  selector:
    matchLabels:
      app: agent
  template:
    metadata:
      labels:
        app: agent
    spec:
      containers:
      - name: agent
        image: busybox
        command: ["sh", "-c", "echo Running on $(hostname); sleep 3600"]
```

---

## ✅ Comportement du DaemonSet

| Fonction                             | Description                            |
|--------------------------------------|----------------------------------------|
| 1 Pod / nœud                         | Déployé automatiquement                |
| Ajout d’un nœud                      | Nouveau Pod créé                       |
| Suppression d’un nœud               | Pod supprimé                           |


---

## 🧠 Cas d’usage typiques

| Besoin               | Exemple d’agent                   |
|----------------------|----------------------------------|
| Logging              | Fluentd, Filebeat                |
| Monitoring           | Prometheus Node Exporter         |
| Réseau               | Calico, Cilium                   |
| Sécurité             | Falco, auditd                    |
| Disques / Systèmes   | CSI node plugins, config système |

---

## 🔍 Commandes utiles

```bash
kubectl get daemonsets
kubectl describe daemonset node-agent
kubectl get pods -o wide  # Pour voir sur quels nœuds les Pods sont déployés
```

---

## ✅ Différence avec un Deployment

| Deployment            | DaemonSet                       |
|-----------------------|----------------------------------|
| Gère un **nombre de réplicas** | Gère **1 Pod par nœud**          |
| S’adapte à la charge  | S’adapte à l’architecture des nœuds |
| Usage : apps frontend | Usage : agents techniques       |

---

## ✅ Pour générer un DaemonSet vide (dry-run)

```bash
kubectl create daemonset agent --image=busybox --dry-run=client -o yaml
```

---

📌 *Le DaemonSet n'a pas de champ `replicas` : il agit selon la topologie du cluster.*
