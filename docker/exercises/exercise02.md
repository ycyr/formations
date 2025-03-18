## **🛠 Exercice 2 : Créer et gérer des conteneurs**
📌 **Objectif** : Utilisez AWS Cloud9 pour lancer plusieurs conteneurs avec différentes images, arrêtez-les, redémarrez-les, et supprimez-les.
  

### **1️⃣ Lancer deux conteneurs**
Exécutez dans un terminal :  
```
docker run -d --name webserver nginx
docker run -d --name database redis
docker ps
```
👉 **Résultat attendu** : Vous devez voir vos conteneurs qui roulent  

### **2️⃣ Lancer la même commande pour la base de données**
Exécutez :  
```
docker run -d --name database redis
```
👉 **Résultat attendu** : Erreur le nom "database est déjà utilisé". 

Solution: 
  - Changer de nom pour le conteneur: ex: --name db
  - Ne pas mettre de nom spécific, Docker va générer un nom alétoire (non-recommandé en prod)

### **3️⃣ Arrêt et redémarrage de conteneurs Docker**
 
```
docker stop webserver
```
Listez les conteneurs en cours d’exécution :  
```
docker ps
```
Affichez tous les conteneurs (y compris arrêtés) :  
```
docker ps -a
```
Rédémarrer le conteneur webserver
```
docker start webserver
```

### **4️⃣ Arrêt et destruction du conteneur webserver**

```
docker rm  webserver
```

👉 **Résultat attendu** Erreur vous devez arrêter l'instance avant de la détruire.

```
docker stop webserver
docker rm  webserver
```
## *Références*

[Aide Mémoire Docker cli](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/docker-cli-cheatsheet.md)
