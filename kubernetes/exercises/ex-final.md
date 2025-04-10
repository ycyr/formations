# 🧪 TP Final – Synthèse Kubernetes

Ce TP vous permet de réutiliser l'ensemble des notions abordées dans la formation : objets de base, persistance, planification, routage, Ingress, Services, ConfigMap, Secrets, etc.

---

## 🟦 Étape 1 – Préparer l'environnement de travail

🎯 Objectif :
Créer un environnement isolé pour vos ressources.

💬 Contexte :
Vous allez créer tous les objets dans un `namespace` spécifique afin d'éviter les conflits avec les autres ressources du cluster.

📝 À faire :
- Créez un `Namespace` appelé `tp-final`
- Travaillez exclusivement dans ce namespace pour le reste du TP

---

## 🟦 Étape 2 – Configuration via ConfigMap et Secret

🎯 Objectif :
Injecter de la configuration et des données sensibles dans vos Pods sans les coder en dur.

💬 Contexte :
Vous allez fournir des valeurs de configuration à votre application via deux méthodes :
- Un `ConfigMap` pour les variables d'environnement non sensibles
- Un `Secret` pour stocker un token API (ex : clé d'accès privée)

🧩 À créer :
- Un `ConfigMap` nommé `app-config` contenant une variable :
  - `VAR1="hello"`
- Un `Secret` nommé `api-secret` contenant une clé :
  - `API_KEY="topsecret123"`


---

## 🟦 Étape 3 – Déployer une application stateless avec persistance

🎯 Objectif :
Déployer une application classique qui persiste des données sur un volume.

💬 Contexte :
Vous allez déployer `podinfo`, une application containerisée légère, exposée sur le port 9898.

🧩 À intégrer :
- Utilisez un `Deployment` avec 2 réplicas
- Montez un volume via un `PersistentVolumeClaim` de 1Gi
- Montez le volume dans `/data`
- Injectez la variable `VAR1` depuis la `ConfigMap`
- Injectez la variable `API_KEY` depuis le `Secret`
- Exposez le `Deployment` avec un `Service` de type `NodePort`

📝 À faire :
- Créez le YAML du `PVC`
- Créez le `Deployment` avec les bonnes sections :
  - `volumeMounts`
  - `envFrom` ou `env`
- Vérifiez que les Pods lisent bien les variables
---

### 🟦 Étape 4 – Déployer une base de données avec StatefulSet

🎯 Objectif :  
Utiliser un StatefulSet pour déployer une application **stateful** avec stockage persistant **par Pod**.

💬 Contexte :  
Vous allez déployer une instance de Redis ou similaire, qui nécessite :
- Des Pods avec **noms stables**
- Un **PVC par Pod**
- Une résolution DNS de type `pod-0.svc`

🧩 À intégrer :
- Un `StatefulSet` avec 2 réplicas
- Un `volumeClaimTemplate` de 1Gi monté dans `/data`
- Un `Service` de type **Headless** associé (`clusterIP: None`)
- Une image de type `redis` ou autre application simple

📝 À faire :
- Créez un `Service` nommé `db` (headless)
- Vérifiez le nom des Pods (`<nom>-0`, `<nom>-1`)
- Vérifiez la création automatique des PVC (`data-<nom>-0`, etc.)

---

### 🟦 Étape 5 – Créer un Job ponctuel

🎯 Objectif :  
Utiliser un Job pour exécuter un traitement **éphémère** une seule fois.

💬 Contexte :  
Vous allez simuler un script de migration ou d’init qui écrit la date courante dans un fichier partagé.

🧩 À intégrer :
- Utilisez l’image `busybox`
- Écrivez `date > /data/date.txt`
- Le Pod doit redémarrer si l'exécution échoue (`restartPolicy: OnFailure`)
- Utilisez le même PVC que dans l’étape 3 (podinfo)

📝 À faire :
- Créez le Job en YAML
- Exécutez-le manuellement (pas de CronJob ici)
- Vérifiez que le fichier `date.txt` est bien présent via un `kubectl exec` dans un autre Pod

---

### 🟦 Étape 6 – Créer un CronJob

🎯 Objectif :  
Mettre en place une tâche planifiée qui s’exécute régulièrement.

💬 Contexte :  
Vous allez créer un CronJob qui **ajoute une ligne horodatée** dans un fichier log à chaque exécution.

🧩 À intégrer :
- Image : `busybox`
- Commande : `date >> /cron/data.log`
- Planning : toutes les 2 minutes (`*/2 * * * *`)
- Même volume partagé que l'étape précédente
- Garder 2 historiques de succès, 1 d’échec

📝 À faire :
- Créez un `PVC` ou réutilisez le précédent
- Vérifiez les logs des Jobs créés par le CronJob
- Observez la rotation des Jobs dans l’historique

---

### 🟦 Étape 7 – Créer les Services nécessaires

🎯 Objectif :  
Créer les Services nécessaires pour exposer vos applications.

💬 Contexte :
Vous devez rendre accessibles :
- `podinfo` (externe)
- `redis` (interne, utilisé uniquement dans le cluster)

🧩 À créer :
- Service `podinfo-svc` de type `NodePort`, exposant le port 9898
- Service `redis` de type `ClusterIP` (port 6379)
- Vérifiez que les Services sont bien liés à leurs Pods

📝 À faire :
- Créez les manifestes YAML
- Obtenez le `nodePort` de `podinfo` pour test via curl ou navigateur
- Testez `nslookup` et `curl` entre Pods

---

### 🟦 Étape 8 – Créer un Ingress HTTP

🎯 Objectif :  
Créer un point d’entrée unique pour exposer `podinfo` via HTTP avec routage par chemin.

💬 Contexte :  
Un IngressController NGINX est déjà installé dans le cluster.

🧩 À intégrer :
- Un Ingress qui route `/app` vers le Service `podinfo-svc`
- Host : `demo.local`
- Utilisez `ingressClassName: nginx`
- Ajoutez une annotation `nginx.ingress.kubernetes.io/rewrite-target: /`

📝 À faire :
- Créez le manifeste YAML de l’Ingress
- Ajoutez `demo.local` à votre `/etc/hosts` avec l’IP du IngressController
- Testez l’accès via `curl http://demo.local/app`

---

### 🟦 Étape 9 – Déployer un DaemonSet

🎯 Objectif :  
Déployer un agent sur **chaque nœud** du cluster.

💬 Contexte :  
Vous allez créer un DaemonSet minimal qui affiche un message avec le hostname du nœud.

🧩 À intégrer :
- Image : `busybox`
- Commande : `echo "Hello from $(hostname)"; sleep 3600`
- Labels pour l’identification

📝 À faire :
- Vérifiez que le Pod est **présent sur chaque nœud**
- Observez la correspondance Pods <-> Nœuds via :
  ```bash
  kubectl get pods -o wide -n tp-final
  ```

---

### 🟦 Étape 10 – Nettoyage (optionnel)

🎯 Objectif :  
Nettoyer l’environnement si vous souhaitez libérer les ressources.

📝 À faire :
- Supprimez le namespace complet :
  ```bash
  kubectl delete ns tp-final
  ```





