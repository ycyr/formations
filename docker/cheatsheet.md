# 📜 Cheatsheet Docker en Français 

## 🐳 Commandes de Base

```sh
# Vérifier la version de Docker
docker --version

# Afficher l'aide générale
docker --help

# Lister les commandes disponibles
docker

# Afficher l'aide d'une commande spécifique
docker <commande> --help
```

---

## 🚀 Lancer un Conteneur avec `docker run`

```sh
# Lancer un conteneur interactif et éphémère (supprimé à la fin)
docker run --rm -it debian bash

# Lancer un conteneur en arrière-plan (détaché)
docker run -d nginx

# Nommer un conteneur au lancement
docker run --name mon-serveur -d nginx

# Associer un port du conteneur au port de la machine hôte
docker run -d -p 8080:80 nginx

# Monter un volume entre la machine hôte et le conteneur
docker run -d -v /mon/dossier:/dossier-conteneur nginx

# Fixer une variable d'environnement
docker run -d -e "ENV_VAR=valeur" nginx

# Fixer une limite mémoire
docker run -d --memory="256m" nginx

# Fixer une limite CPU
docker run -d --cpus="0.5" nginx

# Spécifier un réseau pour le conteneur
docker run -d --network mon-reseau nginx

# Exécuter un conteneur avec un utilisateur spécifique
docker run -d --user 1001 nginx
```

---

## 🏠 Gestion des Conteneurs

```sh
# Lister les conteneurs en cours d'exécution
docker ps

# Lister tous les conteneurs (même stoppés)
docker ps -a

# Démarrer un conteneur arrêté
docker start <id|nom>

# Arrêter un conteneur en cours d'exécution
docker stop <id|nom>

# Redémarrer un conteneur
docker restart <id|nom>

# Supprimer un conteneur (arrêté)
docker rm <id|nom>

# Supprimer un conteneur en cours d'exécution (forcé)
docker rm -f <id|nom>

# Voir les logs d'un conteneur
docker logs -f <id|nom>

# Voir les processus tournant dans un conteneur
docker top <id|nom>

# Exécuter une commande dans un conteneur en cours d'exécution
docker exec -it <id|nom> bash
```

---

## 📦 Gestion des Images

```sh
# Lister les images disponibles
docker images

# Télécharger une image depuis Docker Hub
docker pull nginx

# Supprimer une image
docker rmi nginx

# Construire une image depuis un Dockerfile
docker build -t mon-image .

# Lancer un conteneur et supprimer l’image après exécution
docker run --rm -it mon-image
```

---

## 🔗 Réseaux Docker

```sh
# Lister les réseaux disponibles
docker network ls

# Créer un réseau personnalisé
docker network create mon-reseau

# Supprimer un réseau
docker network rm mon-reseau

# Connecter un conteneur à un réseau
docker network connect mon-reseau <id|nom>

# Déconnecter un conteneur d'un réseau
docker network disconnect mon-reseau <id|nom>
```

---

## 🗂 Gestion des Volumes

```sh
# Lister les volumes existants
docker volume ls

# Créer un volume
docker volume create mon-volume

# Supprimer un volume
docker volume rm mon-volume

# Monter un volume au lancement d'un conteneur
docker run -d -v mon-volume:/chemin/conteneur nginx
```

---

## ⚡ Nettoyage & Maintenance

```sh
# Supprimer tous les conteneurs arrêtés
docker container prune

# Supprimer toutes les images inutilisées
docker image prune -a

# Supprimer tous les volumes inutilisés
docker volume prune

# Supprimer tous les réseaux inutilisés
docker network prune

# Supprimer tout ce qui est inutilisé (conteneurs, images, volumes, réseaux)
docker system prune -a
```