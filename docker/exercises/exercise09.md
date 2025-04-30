# **📝 Exercice 9 : Comprendre le mode `bridge`, l’exposition des ports avec `-p`, `-P`, et l’option `--link`**

## **Prérequis**
*Si vous utiliser Docker Desktop sous Windows, vous devez vous assurer d'avoir la commande `curl` d'installée. Sinon, vous pouvez utiliser votre fureteur*




## **🎯 Partie 1 : Utilisation du mode `bridge`**
1. Listez les réseaux existants sur votre machine Docker :
   ```sh
   docker network ls
   ```
2. Identifiez le réseau `bridge` et inspectez-le :
   ```sh
   docker network inspect bridge
   ```
3. Lancez un conteneur **nginx** dans le réseau `bridge` :
   ```sh
   docker run -d --name webserver --network bridge nginx
   ```
4. Vérifiez l’IP du conteneur et testez son accessibilité :
   ```sh
   docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' webserver
   ```
5. Depuis un **autre conteneur**, essayez d’accéder au service :
   ```sh
   docker run --rm --network bridge alpine/curl <IP-DU-CONTENEUR>:80
   ```
   **Question :** Pourquoi ce test fonctionne-t-il uniquement depuis un autre conteneur du même réseau ?

---

## **🎯 Partie 2 : Exposer des ports avec `-p` (port mapping manuel)**
1. Supprimez le conteneur précédent :
   ```sh
   docker rm -f webserver
   ```
2. Relancez `nginx` avec un **port exposé manuellement** (`-p`) :
   ```sh
   docker run -d --name webserver -p 8080:80 nginx
   ```
3. Depuis votre **navigateur ou en ligne de commande**, testez l’accès :
   ```sh
   curl http://localhost:8080
   ```
4. Listez les ports **exposés** du conteneur :
   ```sh
   docker ps
   ```
   **Question :** Pourquoi l’application est accessible depuis l’extérieur de Docker cette fois-ci ?

---

## **🎯 Partie 3 : Exposer des ports avec `-P` (port mapping automatique)**
1. Supprimez à nouveau le conteneur :
   ```sh
   docker rm -f webserver
   ```
2. Relancez `nginx` avec `-P` (exposition automatique des ports) :
   ```sh
   docker run -d --name webserver -P nginx
   ```
3. Listez les ports assignés par Docker :
   ```sh
   docker ps
   ```
   **Question :** Quelle différence voyez-vous avec `-p` ?
4. Testez l’accès au conteneur en utilisant le port assigné dynamiquement :
   ```sh
   curl http://localhost:<PORT_ASSIGNÉ>
   ```
   **Question :** Pourquoi Docker attribue-t-il un port différent chaque fois ?

---

## **🎯 Partie 4 : Connecter des conteneurs avec `--link`**
1. Supprimez tous les conteneurs existants :
   ```sh
   docker rm -f webserver
   ```
2. Lancez un conteneur **nginx** en arrière-plan :
   ```sh
   docker run -d --name webserver nginx
   ```
3. Lancez un autre conteneur et établissez un lien avec `webserver` :
   ```sh
   docker run -it --rm --link webserver:mon-serveur alpine sh
   ```
4. Testez la connexion au conteneur `webserver` :
   ```sh
   curl mon-serveur
   ```
   **Question :** Pourquoi le conteneur `alpine` peut-il accéder à `webserver` avec `mon-serveur` ?

---

## **✅ Conclusion**
Dans cet exercice, vous avez appris :
- **Le mode `bridge` et comment les conteneurs peuvent communiquer entre eux**.
- **La différence entre `-p` et `-P` pour l’exposition des ports**.
- **Pourquoi un conteneur en `bridge` n’est pas directement accessible depuis l’hôte sans port mapping**.
- **Comment utiliser `--link` pour connecter des conteneurs entre eux**.

## *Références*

[Aide Mémoire Docker cli](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/docker-cli-cheatsheet.md)

[Aide Mémoire Dockerfile](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/dockerfile-cheatsheet.md)
