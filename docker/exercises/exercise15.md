

# **📝 Exercice : Introduction à Docker Compose 🚀**

## **📌 Objectif**
Cet exercice va vous aider à comprendre comment **déployer une application multi-conteneurs** avec **Docker Compose**.  
Vous allez :  
✅ **Créer un `docker-compose.yml` pour lancer un serveur web et une base de données**.  
✅ **Apprendre à démarrer et arrêter plusieurs services simultanément**.  
✅ **Vérifier l’interconnexion entre les conteneurs**.  

---
## ** Installation de docker-compose 

Si la commande docker-compose n'est pas installé veuillez ces commandes

```sh
sudo curl -SL https://github.com/docker/compose/releases/download/v2.33.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

---

## **🎯 Partie 1 : Préparation du projet**
1. **Créez un dossier `docker-compose-test/` et placez-vous dedans** :
   ```sh
   mkdir docker-compose-test && cd docker-compose-test
   ```
2. **Créez un fichier `docker-compose.yml`** :
   ```yaml
   version: '3.8'

   services:
     web:
       image: nginx
       ports:
         - "8080:80"
       networks:
         - app-network

     database:
       image: mysql:5.7
       environment:
         MYSQL_ROOT_PASSWORD: rootpassword
         MYSQL_DATABASE: testdb
         MYSQL_USER: user
         MYSQL_PASSWORD: password
       networks:
         - app-network

   networks:
     app-network:
   ```

---

## **🎯 Partie 2 : Démarrer l’application avec Docker Compose**
1. **Lancer les services** :
   ```sh
   docker-compose up -d
   ```
2. **Vérifier que les conteneurs sont bien créés** :
   ```sh
   docker ps
   ```
3. **Accéder au serveur web depuis votre navigateur** en visitant :  
   ```sh
   http://localhost:8080
   ```
   **Question :** Pourquoi la page par défaut de Nginx s’affiche ?

4. **Vérifier que la base de données est accessible depuis un conteneur `mysql-client`** :
   ```sh
   docker run --rm --network docker-compose-test_app-network mysql mysql -h database -u user -ppassword -e "SHOW DATABASES;"
   ```

---

## **🎯 Partie 3 : Gestion des services**
1. **Arrêter tous les conteneurs sans supprimer les données** :
   ```sh
   docker-compose down
   ```
2. **Relancer les services** :
   ```sh
   docker-compose up -d
   ```
3. **Arrêter et supprimer tous les conteneurs et le réseau** :
   ```sh
   docker-compose down --volumes --remove-orphans
   ```

---

## **✅ Conclusion**
Dans cet exercice, vous avez appris à :  
✔️ **Créer un fichier `docker-compose.yml`**.  
✔️ **Démarrer et arrêter plusieurs services avec une seule commande**.  
✔️ **Connecter un serveur web et une base de données dans le même réseau**.  
✔️ **Gérer facilement les conteneurs sans `docker run` manuel**.  



