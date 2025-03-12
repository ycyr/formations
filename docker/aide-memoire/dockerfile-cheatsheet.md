# 🐳 Cheatsheet Dockerfile en Français 

## 📜 Structure de Base d'un Dockerfile

```dockerfile
# Définir l'image de base
FROM ubuntu:latest

# Définir le mainteneur (optionnel)
LABEL maintainer="ton.email@example.com"

# Définir le répertoire de travail
WORKDIR /app

# Copier des fichiers de la machine hôte vers le conteneur
COPY . /app

# Télécharger et installer des dépendances
RUN apt-get update && apt-get install -y curl

# Définir une variable d'environnement
ENV APP_ENV=production

# Exposer un port du conteneur
EXPOSE 8080

# Définir la commande par défaut
CMD ["bash"]
```

---

## 🚀 Instructions Principales

### `FROM`
Spécifie l’image de base à utiliser.

```dockerfile
FROM debian:latest
```

---

### `LABEL`
Ajoute des métadonnées à l'image.

```dockerfile
LABEL version="1.0"
LABEL description="Une image de test"
LABEL maintainer="ton.email@example.com"
```

---

### `WORKDIR`
Change le répertoire de travail.

```dockerfile
WORKDIR /mon_dossier
```

---

### `COPY`
Copie des fichiers depuis la machine hôte vers le conteneur.

```dockerfile
COPY fichier.txt /app/
```

---

### `ADD`
Copie des fichiers, mais permet aussi l'extraction d'archives.

```dockerfile
ADD archive.tar.gz /app/
```

---

### `RUN`
Exécute une commande pendant la construction de l’image.

```dockerfile
RUN apt-get update && apt-get install -y python3
```

---

### `CMD`
Définit la commande exécutée par défaut lors du démarrage du conteneur.

```dockerfile
CMD ["python3", "app.py"]
```

---

### `ENTRYPOINT`
Définit une commande de démarrage **non modifiable**.

```dockerfile
ENTRYPOINT ["python3"]
```

---

### `EXPOSE`
Indique un port utilisé par le conteneur.

```dockerfile
EXPOSE 8080
```

---

### `ENV`
Définit une variable d’environnement.

```dockerfile
ENV NODE_ENV=production
```

---

### `ARG`
Définit une variable utilisable **uniquement pendant la construction**.

```dockerfile
ARG VERSION=1.0
RUN echo "Version: $VERSION"
```

---

### `VOLUME`
Crée un volume pour la persistance des données.

```dockerfile
VOLUME /data
```

---

### `USER`
Spécifie l’utilisateur sous lequel le conteneur s’exécute.

```dockerfile
USER 1001
```

---

### `HEALTHCHECK`
Ajoute un test pour vérifier si le conteneur fonctionne correctement.

```dockerfile
HEALTHCHECK --interval=30s CMD curl -f http://localhost || exit 1
```

---

## 🔥 Exemple Complet

```dockerfile
FROM node:14
LABEL maintainer="email@example.com"

WORKDIR /app
COPY . /app
RUN npm install

ENV PORT=3000
EXPOSE 3000

CMD ["node", "server.js"]
```

---
