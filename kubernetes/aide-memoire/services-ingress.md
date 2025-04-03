# 📄 Cheat Sheet – YAML des Services & Ingress Kubernetes

> Ce mémo résume la structure YAML des Services (`kind: Service`) et des Ingress (`kind: Ingress`)

---

## 📦 SERVICES

---

### 🔹 ClusterIP (par défaut)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mon-service
spec:
  selector:
    app: mon-app
  ports:
  - port: 80
    targetPort: 8080
```

| Champ       | Description                                  |
|-------------|----------------------------------------------|
| `port`      | Port exposé à l’intérieur du cluster         |
| `targetPort`| Port sur le conteneur ciblé                  |
| `selector`  | Fait le lien avec les Pods via les labels    |

---

### 🔹 NodePort

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mon-nodeport
spec:
  type: NodePort
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080  # Port accessible sur les nœuds
```

📌 Plage par défaut : 30000–32767  
📥 Accès : `http://<nodeIP>:30080`

---

### 🔹 LoadBalancer (en cloud)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mon-lb
spec:
  type: LoadBalancer
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 8080
```

📥 Expose le service via une IP publique (ou DNS cloud)

---

### 🔹 Headless Service (pour StatefulSets, DNS par pod)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mon-svc
spec:
  clusterIP: None
  selector:
    app: stateful
  ports:
  - port: 80
```

📌 Pas d’IP virtuelle → résolution DNS directe des Pods  
🧠 Utilisé pour `StatefulSet` : `pod-0.svc.namespace.svc`

---

### ✅ Résumé : `spec.ports[]` – structure

```yaml
ports:
- name: http
  port: 80           # Port du Service
  targetPort: 8080   # Port du conteneur
  nodePort: 30080    # (Optionnel) pour type: NodePort
  protocol: TCP
```

---

## 🌐 INGRESS

---

### 🔹 Ingress basique avec routage par chemin

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mon-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: demo.local
    http:
      paths:
      - path: /app
        pathType: Prefix
        backend:
          service:
            name: mon-service
            port:
              number: 80
```

📌 Accès : `http://demo.local/app`  
(Pense à ajouter `demo.local` dans `/etc/hosts`)

---

### 🔹 Avec annotations pour NGINX

```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
```

---

### 🔹 Ingress avec TLS

```yaml
spec:
  tls:
  - hosts:
    - secure.local
    secretName: tls-secret
```

📌 Le `secretName` doit référencer un `Secret` TLS existant (type `kubernetes.io/tls`)

---

### ✅ IngressClass (choix du controller)

```yaml
spec:
  ingressClassName: nginx
```

📌 (Remplace les anciennes annotations `kubernetes.io/ingress.class`)

---

## 🧠 Résumé final

| Type Service    | Visibilité       | IP publique ? | Exemple        |
|------------------|------------------|----------------|----------------|
| ClusterIP        | Interne cluster  | ❌             | `svc:80`       |
| NodePort         | Tous les nœuds   | ✅ Port manuel | `nodeIP:30080` |
| LoadBalancer     | Externe (cloud)  | ✅             | `LB IP:80`     |
| Headless         | DNS par Pod      | ❌             | `pod-0.svc`    |

| Type Ingress     | Routage            | Requiert un Controller |
|------------------|--------------------|-------------------------|
| par chemin       | `/app` → service A | ✅                      |
| par host         | `api.local`        | ✅                      |
| TLS              | HTTPS + certs      | ✅                      |

---

📌 Pour tester :

```bash
kubectl get svc
kubectl get ingress
kubectl describe ingress mon-ingress
```


