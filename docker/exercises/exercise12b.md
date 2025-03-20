# **🔹 Exercice avancé : Gérer les problèmes de permissions entre l'hôte et un conteneur Docker**  

📌 **Objectif** : Comprendre et résoudre les problèmes de **permissions** entre un conteneur et l’hôte lorsqu’on utilise un **bind mount**.

## **💡 Contexte du problème**
Lorsqu’un conteneur écrit des fichiers dans un répertoire monté depuis l’hôte (`bind mount`), **les UID/GID (identifiants d’utilisateur et de groupe) ne correspondent pas forcément** entre l’hôte et le conteneur. Cela peut entraîner :
- 🚫 **Fichiers inaccessibles sur l’hôte** après exécution du conteneur.
- 🚫 **Problèmes de permissions en écriture** depuis le conteneur.
- 🚫 **Conflits entre les utilisateurs hôte et conteneur**.

---

## **🛠 Étapes de l'exercice**
### **1️⃣ Créer un répertoire de stockage sur l’hôte**
Sur la machine hôte, créez un dossier et définissez un propriétaire utilisateur :
```sh
mkdir -p /home/ec2-user/docker-data
sudo chown $USER:$USER /home/ec2-user/docker-data
chmod 700 /home/ec2-user/docker-data
```
📌 Ici, **seul votre utilisateur peut lire et écrire** (`chmod 700`).

---

### **2️⃣ Lancer un conteneur avec un bind mount**
Démarrons un conteneur Alpine qui **monte ce répertoire** :
```sh
docker run -it --name test-permissions -v /home/ec2-user/docker-data:/data alpine  ls -l | grep /data
```
📌 **Problème potentiel :**  
Le conteneur tourne souvent avec un **UID différent** de votre utilisateur.

---

### **3️⃣ Écrire un fichier depuis le conteneur**
Accédez au conteneur et créez un fichier :
```sh
docker exec -it test-permissions sh -c "echo 'Test de permissions' > /data/test.txt"
```
📌 **Questions** :
- Le fichier a-t-il bien été créé ?
- Quels sont les **propriétaires et permissions** du fichier sur l’hôte ?
```sh
ls -l /home/user/docker-data/test.txt
```

---

### **4️⃣ Identifier le problème des UID/GID**
Dans le conteneur, vérifions **l'utilisateur courant** :
```sh
docker exec -it test-permissions id
```
📌 **Résultat attendu** :
- L’UID et le GID **du processus dans le conteneur** ne correspondent pas forcément à votre utilisateur hôte.

Sur l’hôte, vérifiez **les permissions du fichier écrit** :
```sh
ls -l /home/ec2-user/docker-data
```
📌 **Problème possible** :
- Si l’utilisateur dans le conteneur a un **UID inconnu sur l’hôte**, le fichier appartient à **un UID inexistant**.

---

## **🛠 Solutions et corrections des permissions**
### **✅ Solution 1 : Changer les UID/GID dans le conteneur**
**Lancer un conteneur avec le même UID/GID que l’utilisateur hôte** :
```sh
docker run -d --name test-fix -v /home/ec2-user/docker-data:/data --user $(id -u):$(id -g) alpine sleep 3600
```
📌 **Explication** :
- `--user $(id -u):$(id -g)` exécute le conteneur **avec le même UID/GID que l’hôte**.

Testons maintenant :
```sh
docker exec -it test-fix sh -c "echo 'Fix avec UID' > /data/fix.txt"
ls -l /home/ec2-user/docker-data
``` 
📌 **Résultat attendu** : Le fichier `fix.txt` appartient à votre utilisateur hôte.

---

### **✅ Solution 2 : Modifier les permissions sur l’hôte**
Si vous voulez autoriser **tous les utilisateurs** à écrire dans le répertoire :
```sh
chmod 777 /home/ec2-user/docker-data
```
📌 **Attention !** ❗  
- **Cette solution est moins sécurisée**, car **tout utilisateur sur l’hôte peut modifier les fichiers**.

---

### **✅ Solution 3 : Utiliser `chown` dans le conteneur**
Vous pouvez modifier l’UID des fichiers générés par le conteneur :
```sh
docker exec -it test-permissions chown 1000:1000 /data/test.txt
```
📌 **Problème** :
- Vous devez connaître **l’UID/GID de l’utilisateur hôte** à l’avance.

---

## **🛠 Exercice avancé : Gestion des permissions avec un serveur web (NGINX)**
📌 **Objectif** : Monter un dossier hôte pour servir un site statique avec NGINX, tout en gérant **les problèmes de permissions**.
