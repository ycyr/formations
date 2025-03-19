## **🛠 Exercice 5 : Créer et utiliser un volume Docker **


<<<<<<< HEAD
1️⃣ **Créer un volume**
```sh
docker volume create mon-volume
```
2️⃣ **Monter un volume dans un conteneur**
```sh
docker run -d --name conteneur1 -v mon-volume:/data nginx
```
📌 **Explication** :
- `-v mon-volume:/data` → Monte `mon-volume` dans `/data` du conteneur.
=======
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
   docker run --rm --network bridge apline/curl <IP-DU-CONTENEUR>:80
   ```
   **Question :** Pourquoi ce test fonctionne-t-il uniquement depuis un autre conteneur du même réseau ?
>>>>>>> 309d184949078e0d1184982e050dd86bf993347a

3️⃣ **Écrire dans le volume**
```sh
docker exec -it conteneur1 sh -c "echo 'Hello Docker Volume' > /data/test.txt"
```
4️⃣ **Lancer un autre conteneur avec le même volume**
```sh
docker run --rm -it -v mon-volume:/data alpine cat /data/test.txt
```
📌 **Résultat attendu** : Le fichier `test.txt` est toujours là !

5️⃣ **Lister les volumes existants**
```sh
docker volume ls
```

6️⃣ **Inspecter un volume**
```sh
docker volume inspect mon-volume
```
📌 Cette commande affiche l’**emplacement du volume** sur l’hôte.

<<<<<<< HEAD
7️⃣ **Supprimer un volume (après suppression des conteneurs qui l’utilisent)**
```sh
docker volume rm mon-volume

=======
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
   **Question :** Pourquoi cette Docker attribue-t-il un port différent chaque fois ?

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
   **Question :** Pourquoi cela ne fonctionne pas qu'est-ce qu'il faut faire pour le conteneur `alpine` peut-il accéder à `webserver` avec `mon-serveur` ?

---

## **✅ Conclusion**
Dans cet exercice, vous avez appris :
- **Le mode `bridge` et comment les conteneurs peuvent communiquer entre eux**.
- **La différence entre `-p` et `-P` pour l’exposition des ports**.
- **Pourquoi un conteneur en `bridge` n’est pas directement accessible depuis l’hôte sans port mapping**.
- **Comment utiliser `--link` pour connecter des conteneurs entre eux**.
>>>>>>> 309d184949078e0d1184982e050dd86bf993347a

## *Références*

[Aide Mémoire Docker cli](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/docker-cli-cheatsheet.md)

[Aide Mémoire Dockerfile](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/dockerfile-cheatsheet.md)