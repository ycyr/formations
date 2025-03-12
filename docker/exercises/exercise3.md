## **🛠 Exercice 1 : Manipuler les Conteneurs**
📌 **Objectif** : Prendre en main les commandes de base Docker.

### **💡 Étapes :**
1️⃣ **Lancer un conteneur Ubuntu en mode détaché (`-d`)**  
   ```sh
   docker run -dit --name mon-container ubuntu bash
   ```
2️⃣ **Lister les conteneurs en cours d’exécution**  
   ```sh
   docker ps
   ```
3️⃣ **Entrer dans le conteneur en cours d'exécution**  
   ```sh
   docker exec -it mon-container bash
   ```
   👉 **Vérifiez que vous êtes bien dans un environnement Ubuntu.**
4️⃣ **Sortir du conteneur sans l’arrêter (`Ctrl + P + Q`)**  
5️⃣ **Arrêter le conteneur**  
   ```sh
   docker stop mon-container
   ```
6️⃣ **Le redémarrer**  
   ```sh
   docker start mon-container
   ```
7️⃣ **Supprimer le conteneur**  
   ```sh
   docker rm mon-container
   ```

📌 **Résultat attendu** : Vous aurez manipulé un conteneur de A à Z ! 
