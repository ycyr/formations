**🔥 Exercice avancé 13 : Sécuriser et optimiser un conteneur Nginx**
📌 **Objectif** :
- Lancer un serveur **Nginx sécurisé**.
- **Limiter les droits et ses ressources**.
- **Bloquer l’accès Internet**.


### **💡 Étapes**
1️⃣ **Créer un conteneur sécurisé** :
```sh
docker run -ti --name secure-nginx --cap-drop=ALL nginx
```
📌 **Attendu :** Le conteneur ne fonctionne pas, tu l'as enlevé tous ses privilèges avec --cap-drop=ALL

2️⃣ **Ajouter les options suivantes: --cap-add=CHOWN  --cap-add=SETGID --cap-add=SETUID** :

👉 **Attendu :** Le contenur secure-nginx est fonctionnel


3️⃣ **Vérifier l’utilisateur en cours d’exécution** :
```sh
docker run -d --user 1000 --name non-root ubuntu sleep 600
docker exec -it non-root whoami
```
👉 **Attendu :** Un utilisateur non-root.

4️⃣ **Essayer de donner plus de privilèges au conteneur** :
Créer une nouvelle image 

Fichier Dockerfile
```
FROM ubuntu:22.04
RUN apt update && apt -y install sudo
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
USER docker
CMD /bin/bash
```

Construire l'image

```
docker build -t nosecure-image .
```

Essayer d'obtenir plus de privilège

```
docker run -it --security-opt no-new-privileges nosecure-image
sudo su -
```

📌 **Attendu :**Cela ne fonctionne pas**

[Aide Mémoire Docker cli](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/docker-cli-cheatsheet.md)

[Aide Mémoire Dockerfile](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/dockerfile-cheatsheet.md)

[Aide Mémoire Linux Capabilities](https://docs.docker.com/engine/containers/run/#runtime-privilege-and-linux-capabilities)
