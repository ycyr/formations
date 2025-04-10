

# 🧪 TP – Révision Jour 1 avec `httpbin`

## 🎯 Objectifs pédagogiques

- Créer un namespace isolé
- Déployer un Pod avec des labels et annotations
- Gérer la scalabilité avec un ReplicaSet et un Deployment
- Observer la distribution des Pods sur les nœuds
- Créer un Service ClusterIP et tester la connectivité
- Comprendre l'utilité d'une image comme `httpbin`


*Vous aurez besoin des [aides-mémoires](https://github.com/ycyr/formations/tree/main/kubernetes/aide-memoire) pour ce travail pratique* 	

---

## 🟦 Étape 1 – Créer le namespace tp-revision-jour1



---

## 🟦 Étape 2 – Créer un Pod `httpbin` avec labels et annotations

- image: kennethreitz/httpbin
- nom du pod: httpbin-pod
- labels:  app: httpbin
- annotations: version: v1
- containerPort: 80



---

## 🟦 Étape 3 – Créer un ReplicaSet avec 2 réplicas avec le nom "httpbin-rs"


- replicas: 2
- nom: httpbin-rs

---

## 🟦 Étape 4 – Déployer avec un Deployment appelé "httpbin-deploy"


- nom: httpbin-deploy
- replicas: 2


---

## 🟦 Étape 5 – Créer un Service pour exposer httpbin appelé "httpbin-svc" avec le port 80

- nom: httpbin-svc
- port: 80

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


