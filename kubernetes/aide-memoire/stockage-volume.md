# 📄 Cheat Sheet – Volumes : PV, PVC, StorageClass dans Kubernetes

> Résumé des objets YAML liés au stockage dans Kubernetes : `PersistentVolume`, `PersistentVolumeClaim` et `StorageClass`

---

## 📦 PersistentVolume (PV) – Volume disponible

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-exemple
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /mnt/data
```

| Champ                        | Description                                   |
|-----------------------------|-----------------------------------------------|
| `capacity.storage`          | Capacité du volume (ex: 1Gi)                  |
| `accessModes`               | `ReadWriteOnce`, `ReadOnlyMany`, `ReadWriteMany` |
| `reclaimPolicy`             | `Retain`, `Delete` (après suppression PVC)    |
| `hostPath`, `nfs`, etc.     | Backend réel du volume                        |

---

## 📥 PersistentVolumeClaim (PVC) – Demande d’espace

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mon-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

📌 Kubernetes cherchera un PV **compatible** pour le lier.

---

## ⚙️ StorageClass – Provisionnement dynamique

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: slow
provisioner: kubernetes.io/host-path
reclaimPolicy: Delete
volumeBindingMode: Immediate
```

| Champ               | Description                                              |
|---------------------|----------------------------------------------------------|
| `provisioner`       | Le plugin utilisé pour créer le volume (`csi-...`)       |
| `reclaimPolicy`     | Supprime ou retient le PV après usage                    |
| `volumeBindingMode` | `Immediate` ou `WaitForFirstConsumer`                    |

📌 Pour la plupart des clusters cloud, une StorageClass est fournie par défaut.

---

## 🔗 Relation entre les objets

```
PVC → demande de stockage
    ↓
Liaison automatique avec un PV compatible
    ↓
Montage du PV dans le Pod via `volumes`
```

---

## 🧠 Résumé des AccessModes

| Mode             | Description                                   |
|------------------|-----------------------------------------------|
| `ReadWriteOnce`  | Lecture/écriture par un seul Pod              |
| `ReadOnlyMany`   | Lecture seule par plusieurs Pods              |
| `ReadWriteMany`  | Lecture/écriture par plusieurs Pods           |

---

## ✅ Exemple : utilisation dans un Pod

```yaml
volumes:
- name: data
  persistentVolumeClaim:
    claimName: mon-pvc

containers:
- name: app
  image: nginx
  volumeMounts:
  - name: data
    mountPath: /usr/share/nginx/html
```

---

## 🛠️ Commandes utiles

```bash
kubectl get pv
kubectl get pvc
kubectl describe pvc mon-pvc
kubectl get sc
kubectl describe sc standard
```

---

## 🧪 Pour tester rapidement :

```bash
kubectl create pvc mon-pvc --storage-class=standard --access-mode=ReadWriteOnce --resources=requests.storage=1Gi
```

---

## 🖼️ Schéma visuel

```
Pod
 └── PVC (demande)
       └── PV (volume réel)
             └── Stockage physique (disque, NFS, cloud...)
```

---

📌 *Utilisez `volumeClaimTemplates` dans les StatefulSets pour créer 1 PVC par Pod.*
