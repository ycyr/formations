### **🛠 Exercice 10 : Tester la connexion entre deux conteneurs**
1️⃣ **Lancer un conteneur "serveur"** :
```sh
docker run -d --name serveur nginx
```

2️⃣ **Lancer un second conteneur et tester la connexion** :
```sh
docker run --rm -ti alpine ping -c 3 serveur
```
📌 **Question** :
- Pourquoi le ping échoue ?  
- Quelle serait la solution ?

3️⃣ **Détruire le conteneur serveur** :
```sh
docker stop serveur 
docker rm serveur
```

### **💡 Solution : Utiliser un réseau personnalisé**
Un réseau personnalisé permet à Docker d'ajouter un **DNS interne**.

1️⃣ **Créer un réseau personnalisé** :
```sh
docker network create mon-reseau
```
2️⃣ **Crée le conteneur serveur dans ce réseau** :
```sh
docker run -d --name serveur --network mon-reseau nginx
```
3️⃣ **Lancer le client dans le même réseau et tester la connexion** :
```sh
docker run --rm --network mon-reseau alpine ping -c 3 serveur
```
📌 **Résultat attendu** : Le ping fonctionne car Docker gère les **résolutions DNS**.

✅ **Pourquoi faire ça ?**  
- Permet une **communication propre et sécurisée** entre conteneurs.
- Les conteneurs peuvent **se trouver par nom**, au lieu d’utiliser des IP statiques.

## *Références*

[Aide Mémoire Docker cli](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/docker-cli-cheatsheet.md)

[Aide Mémoire Dockerfile](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/dockerfile-cheatsheet.md)