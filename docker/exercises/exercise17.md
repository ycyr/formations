

# **📝 Exercice : Déployer une application multi-conteneurs avec Docker Compose 🚀**

## **📌 Objectif**
Cet exercice vous aidera à **gérer un projet complet avec Docker Compose**, comprenant :  
✅ **Une API Flask (backend)**  
✅ **Une base de données PostgreSQL**  
✅ **Un serveur web Nginx comme reverse proxy**  
✅ **Un réseau personnalisé pour la communication entre les services**  

---

## **🎯 Partie 1 : Préparation du projet**
1. **Créez un dossier `docker-compose-advanced/` et placez-vous dedans** :
   ```sh
   mkdir docker-compose-advanced && cd docker-compose-advanced
   ```
2. **Créez un sous-dossier `backend/` et ajoutez un fichier `app.py`** :
   ```python
   from flask import Flask
   import os
   import psycopg2

   app = Flask(__name__)

   def get_db_connection():
       conn = psycopg2.connect(
           host=os.getenv("DB_HOST", "database"),
           database=os.getenv("DB_NAME", "mydb"),
           user=os.getenv("DB_USER", "user"),
           password=os.getenv("DB_PASSWORD", "password")
       )
       return conn

   @app.route('/')
   def home():
       return "Bienvenue sur l'API Flask 🚀"

   @app.route('/db')
   def db_test():
       conn = get_db_connection()
       cur = conn.cursor()
       cur.execute("SELECT version();")
       data = cur.fetchone()
       cur.close()
       conn.close()
       return f"Version PostgreSQL: {data}"

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

3. **Créez un fichier `requirements.txt` pour le backend** :
   ```
   flask
   psycopg2-binary
   ```

4. **Créez un `Dockerfile` pour le backend dans `backend/`** :
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt requirements.txt
   RUN pip install -r requirements.txt

   COPY . .

   EXPOSE 5000

   CMD ["python", "app.py"]
   ```

---

## **🎯 Partie 2 : Configuration de Docker Compose**
1. **Dans le dossier `docker-compose-advanced/`, créez un fichier `docker-compose.yml`** :
   ```yaml
   version: '3.8'

   services:
     database:
       image: postgres:13
       container_name: database
       restart: always
       environment:
         POSTGRES_DB: mydb
         POSTGRES_USER: user
         POSTGRES_PASSWORD: password
       volumes:
         - pgdata:/var/lib/postgresql/data
       networks:
         - app-network

     backend:
       build: ./backend
       container_name: backend
       restart: always
       depends_on:
         - database
       environment:
         DB_HOST: database
         DB_NAME: mydb
         DB_USER: user
         DB_PASSWORD: password
       ports:
         - "5000:5000"
       networks:
         - app-network

     nginx:
       image: nginx:latest
       container_name: nginx
       restart: always
       depends_on:
         - backend
       volumes:
         - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
       ports:
         - "8080:80"
       networks:
         - app-network

   networks:
     app-network:

   volumes:
     pgdata:
   ```

2. **Créez un dossier `nginx/` et ajoutez un fichier `default.conf` pour configurer le reverse proxy** :
   ```nginx
   server {
       listen 80;
       server_name localhost;

       location / {
           proxy_pass http://backend:5000/;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
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
   curl http://localhost:5000
   ```
   **Question :** Que renvoie cette requête ?

4. **Testez la connexion avec PostgreSQL** :
   ```sh
   curl http://localhost:5000/db
   ```
   **Question :** Que renvoie cette requête ?

5. **Testez l'accès à l'API via le reverse proxy Nginx** :
   ```sh
   curl http://localhost:8080
   ```
   **Question :** Pourquoi cette requête passe-t-elle par Nginx ?

---

## **🎯 Partie 4 : Gestion des logs et maintenance**
1. **Afficher les logs d’un service spécifique** :
   ```sh
   docker-compose logs backend
   ```
2. **Vérifier la connectivité entre les conteneurs** :
   ```sh
   docker exec -it backend ping database
   ```
3. **Redémarrer un service spécifique sans affecter les autres** :
   ```sh
   docker-compose restart nginx
   ```
4. **Arrêter tous les services et nettoyer les volumes** :
   ```sh
   docker-compose down --volumes
   ```

---

## **✅ Conclusion**
Dans cet exercice, vous avez appris à :  
✔️ **Créer et configurer une application multi-conteneurs avec Docker Compose**.  
✔️ **Gérer une base de données PostgreSQL et un backend Flask**.  
✔️ **Mettre en place un reverse proxy Nginx pour exposer l'API**.  
✔️ **Démarrer, tester et maintenir les services avec Docker Compose**.  


