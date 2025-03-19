## **🛠 Exercice 4 : Créer un image personnalisée**


### **1️⃣ Créer une image per à partie de *ubuntu:latest* qui affiche l'heure du contenue à chaque 2 secondes**
 
*Astuce: Dans linux pour afficher l'heure à chaque 5 secondes*

```
while date; do sleep 5; done
````

### **2️⃣ Tester le fonctionnement de votre image, et que voyez-vous**


### **3️⃣ Ajouter le package nano dans votre image et un tag *v2***

* Astuce: Dans ubuntu pour installer le package *"nano"*
```
apt update
apt install -y NOM_PACKAGE
````

### **4️⃣ Afficher les couches de votre image** 

* Astuce: utiliser la commande suivante pour afficher les couches *
```
docker history ID_IMAGE
````



### **5️⃣ Créer un autre image à partir de alpine:latest** 

* Astuce: Dans Alpine pour installer un package *

```
apk add   NOM_PACKAGE
```

### **6️⃣ Comparer la taille de vos trois images**

## *Références*

[Aide Mémoire Docker cli](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/docker-cli-cheatsheet.md)

[Aide Mémoire Dockerfile](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/dockerfile-cheatsheet.md)
