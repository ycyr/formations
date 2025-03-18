## **🛠 Exercice 5 : Créer et utiliser un volume Docker**


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

7️⃣ **Supprimer un volume (après suppression des conteneurs qui l’utilisent)**
```sh
docker volume rm mon-volume
```

## *Références*

[Aide Mémoire Docker cli](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/docker-cli-cheatsheet.md)

[Aide Mémoire Dockerfile](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/dockerfile-cheatsheet.md)
