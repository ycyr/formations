

# **📝 Exercice avancé : Dockerisation complète  🚀**

## **📌 Objectif**
Cet exercice va vous permettre de **maîtriser Docker** en **créant et déployant une application multi-conteneurs avancée** 

✅ **Créer un réseau bridge personnalisé pour isoler les services**  
✅ **Construire plusieurs images Docker personnalisées avec un `Dockerfile`**  
✅ **Utiliser des volumes et bind mounts pour persister les données**  
✅ **Gérer les connexions entre plusieurs conteneurs**  
✅ **Exposer certains services à l'extérieur via les ports**  
✅ **Faire communiquer un backend Python avec une base de données MySQL et un serveur web Nginx**  

---

## **🎯 Partie 1 : Création du réseau personnalisé**
1. **Créez un réseau Docker `app_network`** en mode `bridge` :
   ```sh
   docker network create app_network
   ```
2. **Listez les réseaux existants** et assurez-vous que `app_network` est bien créé :
   ```sh
   docker network ls
   ```

---

## **🎯 Partie 2 : Création d'une image personnalisée pour le Backend (Flask)**
1. **Créez un dossier `backend/` et ajoutez un fichier `app.py`** avec le contenu suivant :
   ```python
   from flask import Flask
   import pymysql

   app = Flask(__name__)

   @app.route('/')
   def home():
       return "API Backend en Flask est fonctionnelle 🚀"

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```
2. **Créez un `requirements.txt`** dans `backend/` :
   ```
   flask
   pymysql
   ```
3. **Créez un `Dockerfile` dans `backend/`** :
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt requirements.txt
   RUN pip install -r requirements.txt

   COPY . .

   EXPOSE 5000

   CMD ["python", "app.py"]
   ```
4. **Construisez l’image du backend** :
   ```sh
   docker build -t my-backend ./backend
   ```

---

## **🎯 Partie 3 : Création du conteneur de base de données MySQL**
1. **Créez un volume Docker pour stocker les données** :
   ```sh
   docker volume create mysql_data
   ```
2. **Lancez un conteneur MySQL avec persistance des données** :
   ```sh
   docker run -d --name my_database --network app_network      -v mysql_data:/var/lib/mysql      -e MYSQL_ROOT_PASSWORD=rootpassword      -e MYSQL_DATABASE=mydb      -e MYSQL_USER=user      -e MYSQL_PASSWORD=password      mysql:5.7
   ```
3. **Vérifiez que la base est bien créée** :
   ```sh
   docker logs my_database
   ```

---

## **🎯 Partie 4 : Création d'un serveur web Nginx**
1. **Créez un dossier `nginx/` et ajoutez un fichier `default.conf`** :
   ```nginx
   server {
       listen 80;
       server_name localhost;

       location / {
           proxy_pass http://my_backend:5000/;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```
2. **Créez un `Dockerfile` dans `nginx/`** :
   ```dockerfile
   FROM nginx:latest

   COPY default.conf /etc/nginx/conf.d/default.conf

   EXPOSE 80
   ```
3. **Construisez l’image du serveur Nginx** :
   ```sh
   docker build -t my-nginx ./nginx
   ```

---

## **🎯 Partie 5 : Lancer tous les conteneurs et tester l'application**
1. **Lancer le backend et l’ajouter au réseau** :
   ```sh
   docker run -d --name my_backend --network app_network      -p 5000:5000 my-backend
   ```
2. **Lancer le serveur Nginx avec une connexion au backend** :
   ```sh
   docker run -d --name my_nginx --network app_network      -p 8080:80 my-nginx
   ```
3. **Vérifier que tout fonctionne** :
   - Accéder à l’API Flask en local :  
     ```sh
     curl http://localhost:5000
     ```
   - Accéder au site via Nginx :  
     ```sh
     curl http://localhost:8080
     ```

---

## **🎯 Partie 6 : Debugging et maintenance**
1. **Lister les conteneurs en cours d'exécution** :
   ```sh
   docker ps
   ```
2. **Afficher les logs du backend** :
   ```sh
   docker logs my_backend
   ```
3. **Vérifier la connexion entre les conteneurs** :
   ```sh
   docker exec -it my_nginx ping my_backend
   ```

---

## **✅ Conclusion**
Dans cet exercice, vous avez appris à :  
✔️ **Créer un réseau personnalisé `bridge`**.  
✔️ **Construire une image Docker pour un backend Flask**.  
✔️ **Lancer un conteneur MySQL avec persistance des données**.  
✔️ **Utiliser un serveur web Nginx pour interagir avec un backend**.  
✔️ **Faire communiquer plusieurs conteneurs**
