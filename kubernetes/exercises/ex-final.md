

### ✅ Structure du TP (résumé rapide)

---

### 🟦 Étape 1 – Créer un `namespace` dédié

```bash
kubectl create namespace tp-final
```

---

### 🟦 Étape 2 – Créer un `ConfigMap` et un `Secret`

- ConfigMap avec une variable d'environnement
- Secret contenant une clé API (base64-encodée)

---

### 🟦 Étape 3 – Déployer une app web avec `Deployment` + `PVC`

- `podinfo` comme app principale  
- Volume monté pour persister `/data`  
- Lire le ConfigMap et Secret via env

---

### 🟦 Étape 4 – Déployer une base avec `StatefulSet`

- Exemple : mini Redis  
- PVC automatique par Pod via `volumeClaimTemplates`  
- Headless service pour DNS

---

### 🟦 Étape 5 – Créer un `Job` ponctuel

- `busybox` qui écrit un fichier avec `date` dans un volume partagé

---

### 🟦 Étape 6 – Créer un `CronJob` toutes les 2 minutes

- Écrit une ligne horodatée dans `/cron/data.log`

---

### 🟦 Étape 7 – Créer des `Services`

- `ClusterIP` pour redis  
- `NodePort` pour accéder à `podinfo` (test avec curl ou navigateur)

---

### 🟦 Étape 8 – Créer un `Ingress`

- Routage `/app` vers podinfo  
- Host `demo.local` à ajouter dans `/etc/hosts`  
- (IngressController déjà installé)

---

### 🟦 Étape 9 – Déployer un `DaemonSet`

- `busybox` qui affiche `Hello from $(hostname)`  
- Tester avec `kubectl get pods -o wide`

---

### 🟦 Étape 10 – Nettoyage final (optionnel)

```bash
kubectl delete ns tp-final
```

---

📘 Chaque étape est accompagnée de :

- Commandes `kubectl`
- Fichiers YAML d’exemple
- Questions pour valider la compréhension

---
