# **📝 Exercice complet : Révision des concepts  🚀**

## **📌 Objectif**
Cet exercice va vous permettre de pratiquer **toutes les notions vues jusqu’à présent** :
✅ **Gestion des conteneurs** (lancer, stopper, inspecter).  
✅ **Utilisation des volumes et bind mounts**.  
✅ **Création d’images personnalisées avec un `Dockerfile`**.  
✅ **Gestion des réseaux avec un réseau `bridge` personnalisé**.  
✅ **Exposition des ports pour accéder aux services**.  
✅ **Interaction entre plusieurs conteneurs**.  

---

## **🎯 Partie 1 : Préparation de l’environnement Docker**
1. **Vérifiez que Docker est installé** sur votre machine :
   ```sh
   docker version
   ```
2. **Supprimez tous les conteneurs en cours d’exécution (si nécessaire)** :
   ```sh
   docker rm -f $(docker ps -aq)
   ```
3. **Listez les images existantes et supprimez celles inutiles (optionnel)** :
   ```sh
   docker images
   docker rmi -f <IMAGE_ID>
   ```

---

## **🎯 Partie 2 : Création d'un réseau personnalisé**
1. **Créez un réseau Docker `my_custom_network`** en mode `bridge` :
   ```sh
   docker network create my_custom_network
   ```
2. **Listez les réseaux existants** et assurez-vous que `my_custom_network` est bien créé :
   ```sh
   docker network ls
   ```

---

## **🎯 Partie 3 : Création d'une image personnalisée avec un `Dockerfile`**
1. **Dans un nouveau dossier `my_custom_image/`, créez un fichier `Dockerfile`** avec le contenu suivant :
   ```dockerfile
   FROM ubuntu:latest

   # Installer curl et nginx
   RUN apt update && apt install -y curl nginx

   # Copier une page HTML personnalisée
   COPY index.html /var/www/html/index.html

   # Exposer le port 80
   EXPOSE 80

   # Démarrer nginx en mode foreground
   CMD ["nginx", "-g", "daemon off;"]
   ```
2. **Créez un fichier `index.html` dans `my_custom_image/`** avec :
   ```html
   <html>
   <body>
       <h1>Bienvenue sur mon serveur web Docker 🚀</h1>
   </body>
   </html>
   ```
3. **Construisez l’image Docker** :
   ```sh
   docker build -t my-webserver ./my_custom_image
   ```
4. **Vérifiez que l’image est bien créée** :
   ```sh
   docker images
   ```

---

## **🎯 Partie 4 : Lancer des conteneurs avec des volumes et des bind mounts**
1. **Créez un volume Docker nommé `my_data`** :
   ```sh
   docker volume create my_data
   ```
2. **Lancez un premier conteneur MySQL avec un volume pour la persistance des données** :
   ```sh
   docker run -d --name my_database --network my_custom_network      -v my_data:/var/lib/mysql      -e MYSQL_ROOT_PASSWORD=rootpassword      mysql:5.7
   ```
3. **Créez un dossier `logs/` sur votre hôte et montez-le comme bind mount dans un conteneur Alpine** :
   ```sh
   mkdir -p ~/docker_logs
   docker run -d --name my_logger --network my_custom_network      -v ~/docker_logs:/var/log      alpine tail -f /dev/null
   ```
4. **Ajoutez un fichier dans le dossier `logs/` et vérifiez qu'il apparaît dans le conteneur Alpine** :
   ```sh
   echo "Test log entry" > ~/docker_logs/test.log
   docker exec -it my_logger ls /var/log
   ```
5. **Vérifier que dans le dossier ~/docker_logs que le fichier test.log contienne le log crée à la section 4** :
   ```sh
   ls -l ~/docker_logs/test.log
   cat ~/docker_logs/test.log
   ```
---

## **🎯 Partie 5 : Lancer plusieurs conteneurs avec exposition de ports**
1. **Lancez le serveur web personnalisé (image `my-webserver`)** et ouvrez son port :
   ```sh
   docker run -d --name my_webserver --network my_custom_network      -p 8080:80 my-webserver
   ```
2. **Lancez un conteneur `alpine` qui joue le rôle d’un client et vérifiez la connexion** :
   ```sh
   docker run --rm --network my_custom_network alpine wget -qO- my_webserver
   ```
3. **Accédez au serveur web depuis votre navigateur** en allant sur :
   ```sh
   curl http://localhost:8080
   ```
   **Question :** Pourquoi cette URL fonctionne-t-elle ?

---

## **🎯 Partie 6 : Vérifications et debugging**
1. **Vérifiez les conteneurs en cours d’exécution** :
   ```sh
   docker ps
   ```
2. **Inspectez les logs du serveur web** :
   ```sh
   docker logs my_webserver
   ```
   **Question Expert :** Pourquoi on ne voit pas les logs ?
3. **Vérifiez la connectivité entre les conteneurs avec `ping`** :
   ```sh
   docker exec -it my_webserver ping my_database
   ```
   **Question :** Pourquoi ce ne fonctionne pas ?
---

## **✅ Conclusion**
Dans cet exercice, vous avez appris à :  
✔️ **Créer un réseau personnalisé en mode `bridge`**.  
✔️ **Construire une image Docker personnalisée avec un `Dockerfile`**.  
✔️ **Lancer des conteneurs avec des volumes et des bind mounts**.  
✔️ **Exposer des ports pour rendre un service accessible depuis l’hôte**.  
🚀

