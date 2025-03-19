

# **📝 Exercice 18: Déploiement sécurisé et optimisé avec Docker Compose 🚀**

## **📌 Objectif**
Dans cet exercice, vous allez apprendre à **mettre en place une application robuste avec Docker Compose** en intégrant :  
✅ **Volumes et Bind Mounts** (gestion des données)  
✅ **Restrictions CPU et Mémoire** (optimisation des ressources)  
✅ **Bonnes pratiques de sécurité** (permissions, utilisateurs non-root, variables d’environnement sécurisées)  
✅ **Gestion avancée des réseaux** (isolation des services)  
✅ **Exposition des ports** (accès contrôlé aux services)  

L’application se compose de :  
- Un **backend Python Flask** avec une base de données SQLite.  
- Un **serveur Nginx** en tant que proxy inverse.  
- Un **stockage persistant pour les logs et la base de données**.  

---

## **🎯 Partie 1 : Préparation du projet**
1. **Créez un dossier `secure-compose-project/` et placez-vous dedans** :
   ```sh
   mkdir secure-compose-project && cd secure-compose-project
   ```
2. **Créez un sous-dossier `backend/` et ajoutez un fichier `app.py`** :
   ```python
   from flask import Flask
   import os

   app = Flask(__name__)

   @app.route('/')
   def home():
       return "Bienvenue sur l'API Sécurisée 🚀"

   @app.route('/secret')
   def secret():
       return f"Clé secrète : {os.getenv('SECRET_KEY', 'default_key')}"

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

3. **Créez un fichier `requirements.txt` pour le backend** :
   ```
   flask
   ```

4. **Créez un `Dockerfile` pour le backend dans `backend/`** :
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt requirements.txt
   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   RUN adduser --disabled-password --gecos '' appuser
   USER appuser

   EXPOSE 5000

   CMD ["python", "app.py"]
   ```

---

## **🎯 Partie 2 : Configuration de Docker Compose**
1. **Dans le dossier `secure-compose-project/`, créez un fichier `docker-compose.yml`** :
   ```yaml
   version: '3.8'

   services:
     backend:
       build: ./backend
       container_name: backend_secure
       restart: always
       environment:
         SECRET_KEY: "super_secret_key"
       ports:
         - "5001:5000"
       networks:
         - private_network
       deploy:
         resources:
           limits:
             cpus: "0.5"
             memory: "256M"
       security_opt:
         - no-new-privileges:true
       volumes:
         - backend_data:/app/data
         - ./logs:/app/logs

     nginx:
       image: nginx:latest
       container_name: nginx_proxy
       restart: always
       depends_on:
         - backend
       volumes:
         - ./nginx/default.conf:/etc/nginx/conf.d/default.conf:ro
       ports:
         - "8080:80"
       networks:
         - public_network
         - private_network
       security_opt:
         - no-new-privileges:true

   networks:
     public_network:
     private_network:
       internal: true

   volumes:
     backend_data:
   ```

2. **Créez un dossier `nginx/` et ajoutez un fichier `default.conf` pour le reverse proxy** :
   ```nginx
   server {
       listen 80;
       server_name localhost;

       location / {
           proxy_pass http://backend_secure:5000/;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

3. **Créez un dossier `logs/` pour stocker les logs** :
   ```sh
   mkdir logs
   ```

---

## **🎯 Partie 3 : Démarrage et test des services**
1. **Démarrez l'application avec Docker Compose** :
   ```sh
   docker-compose up -d --build
   ```
2. **Vérifiez que les services sont bien démarrés** :
   ```sh
   docker ps
   ```
3. **Testez l'API Flask directement via le backend** :
   ```sh
   curl http://localhost:5001
   ```
4. **Testez l'accès via Nginx (reverse proxy)** :
   ```sh
   curl http://localhost:8080
   ```

---

## **🎯 Partie 4 : Vérifications de sécurité et de performances**
1. **Vérifiez l’utilisateur exécutant le processus dans le conteneur backend** :
   ```sh
   docker exec -it backend_secure whoami
   ```
   **Question :** Pourquoi ce n’est pas `root` ?

2. **Vérifiez la consommation CPU et mémoire** :
   ```sh
   docker stats
   ```

3. **Testez l’isolation réseau** :  
   - Depuis **le conteneur `nginx`**, testez la connectivité avec `backend_secure` :
     ```sh
     docker exec -it nginx_proxy ping backend_secure
     ```
   - Depuis **le conteneur `backend_secure`**, essayez de contacter l’extérieur (ex: `google.com`) :
     ```sh
     docker exec -it backend_secure ping -c 2 google.com
     ```
   **Question :** Pourquoi `backend_secure` ne peut pas contacter l’extérieur ?

4. **Vérifiez que les logs sont bien stockés dans le dossier bind mount `logs/`** :
   ```sh
   ls logs/
   ```

---

## **🎯 Partie 5 : Arrêt et nettoyage**
1. **Arrêter les services sans perdre les données** :
   ```sh
   docker-compose down
   ```
2. **Supprimer tous les conteneurs et volumes** (attention, cela supprime aussi la base de données) :
   ```sh
   docker-compose down --volumes --remove-orphans
   ```

---

## **✅ Conclusion**
Dans cet exercice, vous avez appris à :  
✔️ **Créer et configurer une application sécurisée avec Docker Compose**.  
✔️ **Restreindre l’accès réseau en utilisant des réseaux internes**.  
✔️ **Appliquer les bonnes pratiques de sécurité (`no-new-privileges`, utilisateurs non-root)**.  
✔️ **Limiter la consommation CPU et mémoire d’un conteneur**.  
✔️ **Utiliser des volumes et bind mounts pour persister les données et logs**.  



