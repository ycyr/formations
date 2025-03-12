# 📜 Cheatsheet Docker Compose en Français 

## 🐳 Introduction à `docker-compose.yml`

Docker Compose permet de gérer plusieurs conteneurs avec un seul fichier YAML.

---

## 📄 Structure de Base

```yaml
version: '3.8'  # Définir la version de Docker Compose

services:
  web:
    image: nginx:latest  # Utilisation de l'image Nginx
    ports:
      - "8080:80"  # Redirection des ports
    volumes:
      - ./html:/usr/share/nginx/html  # Montage d'un volume
    environment:
      - NGINX_HOST=localhost
    restart: always  # Politique de redémarrage automatique
```

---

## 🚀 Commandes Principales

```sh
# Lancer les services en arrière-plan
docker-compose up -d

# Lancer et afficher les logs
docker-compose up

# Arrêter les services
docker-compose down

# Redémarrer les services
docker-compose restart

# Voir les logs des services
docker-compose logs -f

# Lister les services en cours d'exécution
docker-compose ps

# Arrêter un seul service
docker-compose stop web

# Supprimer un seul service
docker-compose rm -f web

# Construire les images définies dans le fichier compose
docker-compose build

# Mettre à jour un service (sans tout relancer)
docker-compose up -d --no-deps web
```

---

## 🔧 Détails des Sections

### `version`
Indique la version de `docker-compose.yml`.

```yaml
version: '3.8'
```

---

### `services`
Définit les services (conteneurs) à exécuter.

```yaml
services:
  app:
    image: myapp:latest
    build: .
    ports:
      - "5000:5000"
```

---

### `build`
Construit une image depuis un `Dockerfile`.

```yaml
build:
  context: .
  dockerfile: Dockerfile
```

---

### `ports`
Expose les ports entre le conteneur et l’hôte.

```yaml
ports:
  - "8080:80"
```

---

### `volumes`
Monte un volume pour la persistance des données.

```yaml
volumes:
  - ./data:/var/lib/mysql
```

---

### `environment`
Définit des variables d’environnement.

```yaml
environment:
  - MYSQL_ROOT_PASSWORD=secret
```

---

### `networks`
Associe un conteneur à un réseau personnalisé.

```yaml
networks:
  mon_reseau:
    driver: bridge
```

---

### `depends_on`
Spécifie les dépendances entre services.

```yaml
depends_on:
  - db
```

---

### `restart`
Définit la politique de redémarrage.

```yaml
restart: always  # Autre option : "no", "on-failure", "unless-stopped"
```

---

## 🔥 Exemple Complet

```yaml
version: '3.8'

services:
  db:
    image: mysql:5.7
    environment:
      - MYSQL_ROOT_PASSWORD=secret
    volumes:
      - db_data:/var/lib/mysql

  web:
    image: nginx:latest
    ports:
      - "8080:80"
    depends_on:
      - db

volumes:
  db_data:
```

---

Avec ce **cheatsheet Docker Compose**, tu peux orchestrer tes conteneurs facilement ! 🚀🐳  
Besoin d'autres précisions ? 😊
