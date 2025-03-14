## **🛠 Exercice 1 : Identifier les Composants Docker**
📌 **Objectif** : Vérifier la présence de Docker et explorer ses composants.  

### **1️⃣ Vérifier si Docker est installé**
Exécutez dans un terminal :  
```
docker --version
```
👉 **Résultat attendu** : Affiche la version installée de Docker.  

### **2️⃣ Tester le fonctionnement de Docker**
Exécutez :  
```
docker run hello-world
```
👉 **Résultat attendu** : Un conteneur s'exécute et affiche un message de succès.

### **3️⃣ Explorer les composants Docker**
Listez les images disponibles :  
```
docker images
```
Listez les conteneurs en cours d’exécution :  
```
docker ps
```
Affichez tous les conteneurs (y compris arrêtés) :  
```
docker ps -a
```
## *Références*

[Aide Mémoire Docker cli](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/docker-cli-cheatsheet.md)