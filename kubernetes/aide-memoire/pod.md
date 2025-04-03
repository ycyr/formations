
# 📄 Cheat Sheet – Structure YAML d’un Pod Kubernetes

> Ce mémo liste les principaux champs qu’on retrouve dans un manifeste de Pod (`kind: Pod`), avec explications et exemples.

---

## 🎯 Structure globale d’un Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mon-pod
  namespace: default
  labels:
    app: demo
  annotations:
    description: "Pod de test"
spec:
  containers:
  - name: app
    image: nginx:1.25
```

---

## 🔹 `metadata`

| Champ       | Rôle                                           |
|-------------|------------------------------------------------|
| `name`      | Nom unique du Pod                              |
| `namespace` | Espace logique dans le cluster (`default`, ...)|
| `labels`    | Tags pour la sélection (`app=demo`, ...)       |
| `annotations` | Infos libres non utilisées pour le scheduling |

---

## 🔹 `spec`

C’est ici que se définissent les **containers**, **volumes**, **nodeSelector**, etc.

---

### ✅ `containers`

```yaml
spec:
  containers:
  - name: app
    image: nginx
    command: ["nginx", "-g", "daemon off;"]
    ports:
    - containerPort: 80
    env:
    - name: ENV
      value: "prod"
    volumeMounts:
    - name: mon-volume
      mountPath: /usr/share/nginx/html
```

| Champ             | Rôle                                    |
|-------------------|-----------------------------------------|
| `name`            | Nom du conteneur                        |
| `image`           | Image Docker utilisée                   |
| `command`         | Commande exécutée dans le conteneur     |
| `ports`           | Ports exposés dans le conteneur         |
| `env`             | Variables d’environnement               |
| `volumeMounts`    | Points de montage de volumes            |

---

### ✅ `volumes`

```yaml
volumes:
- name: mon-volume
  persistentVolumeClaim:
    claimName: mon-pvc
```

| Type            | Description                          |
|-----------------|--------------------------------------|
| `emptyDir`      | Volume éphémère (durée de vie du Pod)|
| `hostPath`      | Montage local du nœud (⚠️ fragile)    |
| `configMap`     | Lecture de fichiers de config        |
| `secret`        | Injection de données sensibles       |
| `persistentVolumeClaim` | Stockage persistant (PVC)    |

---

### ✅ Autres champs utiles dans `spec`

| Champ            | Description                                  |
|------------------|----------------------------------------------|
| `restartPolicy`  | `Always` (par défaut), `OnFailure`, `Never`  |
| `nodeSelector`   | Contraindre à certains nœuds (`key: value`)  |
| `tolerations`    | Accepter des nœuds avec `taints` spécifiques |
| `affinity`       | Règles avancées de placement                 |
| `securityContext`| UID/GID, droits, capabilities                |

---

### ✅ Sidecar / Init / Multi-container

```yaml
spec:
  initContainers:
  - name: init-db
    image: busybox
    command: ["sh", "-c", "echo Init OK"]
  
  containers:
  - name: app
    image: nginx

  - name: sidecar
    image: busybox
    command: ["sh", "-c", "tail -f /dev/null"]
```

| Type            | Rôle                                          |
|-----------------|-----------------------------------------------|
| `initContainers`| S’exécutent **avant** les `containers`        |
| `containers`    | Les conteneurs principaux                     |
| `sidecars`      | Pas un champ dédié : un conteneur secondaire |

---

Parfait ✅ Tu fais bien d’ajouter ça : les **`resources`** (`requests` & `limits`) et les **probes** (`livenessProbe`, `readinessProbe`) sont des **bonnes pratiques de prod**, même si pas encore vues.

Je complète donc le **cheatsheet YAML du Pod** avec ces deux blocs supplémentaires :

---

## ✅  `resources` – CPU & Mémoire

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
  limits:
    cpu: "250m"
    memory: "256Mi"
```

| Champ        | Rôle                                         |
|--------------|----------------------------------------------|
| `requests`   | Minimum garanti (réservation sur le nœud)    |
| `limits`     | Maximum autorisé (coupure si dépassé)        |
| `cpu`        | Exprimé en millicores (ex: `500m` = 0.5 CPU) |
| `memory`     | Exprimé en Mi, Gi                            |

---

✅ Exemple dans un conteneur :

```yaml
containers:
- name: api
  image: my-api
  resources:
    requests:
      cpu: "200m"
      memory: "128Mi"
    limits:
      cpu: "500m"
      memory: "256Mi"
```

---

## ✅  Probes – Health checks

```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 2
  periodSeconds: 5
```

| Probe              | But                                               |
|--------------------|----------------------------------------------------|
| `livenessProbe`    | ⚠️ Est-ce que le conteneur est encore **vivant** ? Sinon → restart |
| `readinessProbe`   | 📡 Est-ce qu’il est **prêt à recevoir du trafic** ? Sinon → pas dans le Service |

---

✅ Exemple dans un conteneur :

```yaml
containers:
- name: app
  image: my-api
  ports:
  - containerPort: 8080
  livenessProbe:
    httpGet:
      path: /healthz
      port: 8080
    initialDelaySeconds: 5
    periodSeconds: 10
  readinessProbe:
    httpGet:
      path: /ready
      port: 8080
    initialDelaySeconds: 3
    periodSeconds: 5
```

---

📌 Autres types de probes :
- `exec` : lance une commande
- `tcpSocket` : vérifie si un port est ouvert

---

### ✅ Mise à jour : Résumé visuel final




---

## ✅ Commandes utiles

```bash
kubectl explain pod.spec
kubectl explain pod.spec.containers
```

---

📌 Astuce : Pour générer un squelette rapidement :

```bash
kubectl run demo --image=nginx --dry-run=client -o yaml > pod.yaml
```

---

## ✅ Résumé visuel (structure hiérarchique)

```
Pod
├── metadata
├── spec
│   ├── containers[]
│   │   ├── image, ports, env
│   │   ├── volumeMounts[]
│   │   ├── resources (CPU/memory)
│   │   ├── livenessProbe
│   │   └── readinessProbe
│   ├── volumes[]
│   ├── initContainers[]
│   ├── nodeSelector
│   ├── restartPolicy
│   └── tolerations / affinity
```

---
