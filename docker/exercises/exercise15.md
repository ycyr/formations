# **📝 Exercice 15 : Optimisation d’image Docker avec Multi-Stage Build 🚀**

## **📌 Objectif**
Cet exercice va vous permettre d’**optimiser vos images Docker** en utilisant **Multi-Stage Build**.  
Vous allez apprendre à :  
✅ **Séparer l’étape de build et d’exécution** pour alléger l’image finale  
✅ **Construire une image optimisée et sécurisée**  
✅ **Réduire la taille de l’image tout en conservant les fichiers nécessaires**  

---

## **🎯 Partie 1 : Création d’une application Node.js**
1. **Créez un dossier `multi-stage-app/` et placez-vous dedans** :
   ```sh
   mkdir multi-stage-app && cd multi-stage-app
   ```
2. **Créez un fichier `server.js` contenant une simple API Express.js** :
   ```javascript
   const express = require("express");
   const app = express();

   app.get("/", (req, res) => {
       res.send("Hello, Docker Multi-Stage Build!");
   });

   app.listen(3000, () => {
       console.log("Server running on port 3000");
   });
   ```
3. **Créez un fichier `package.json` contenant les dépendances** :
   ```json
   {
       "name": "multi-stage-app",
       "version": "1.0.0",
       "description": "A simple Node.js app optimized with Multi-Stage Build",
       "main": "server.js",
       "scripts": {
           "start": "node server.js"
       },
       "dependencies": {
           "express": "^4.18.2"
       }
   }
   ```

4. **Installez les dépendances** (optionnel pour tester en local) :
   ```sh
   npm install
   ```

---

## **🎯 Partie 2 : Création d’un Dockerfile non optimisé**
1. **Créez un `Dockerfile` initial** sans optimisation :  
   ```dockerfile
   FROM node:18

   WORKDIR /app

   COPY package.json .
   RUN npm install

   COPY . .

   CMD ["node", "server.js"]
   ```

2. **Construisez l’image et observez sa taille** :  
   ```sh
   docker build -t node-unoptimized .
   docker images
   ```  
   **Question** : Quelle est la taille de l’image ? Pourquoi est-elle aussi grande ?

---

## **🎯 Partie 3 : Optimisation avec Multi-Stage Build**
1. **Modifiez le `Dockerfile` pour utiliser une approche Multi-Stage** :  
   ```dockerfile
   # Étape 1 : Build
   FROM node:18 AS builder
   WORKDIR /app
   COPY package.json .
   RUN npm install
   COPY . .
   RUN npm run build

   # Étape 2 : Image finale optimisée
   FROM node:18-alpine
   WORKDIR /app
   COPY --from=builder /app/dist /app/dist
   COPY --from=builder /app/node_modules /app/node_modules
   CMD ["node", "dist/server.js"]
   ```

2. **Construisez cette nouvelle image et observez la différence de taille** :  
   ```sh
   docker build -t node-optimized .
   docker images
   ```  
   **Question** : Quelle est la réduction de taille ? Pourquoi cette approche est-elle plus efficace ?

---

## **🎯 Partie 4 : Vérifications et tests**
1. **Lancez l’image non optimisée en arrière-plan** :  
   ```sh
   docker run -d --name unoptimized -p 3000:3000 node-unoptimized
   ```

2. **Testez l’application en accédant à `http://localhost:3000`**  
   **Question** : L’application fonctionne-t-elle correctement ?

3. **Arrêtez et supprimez l’ancien conteneur** :  
   ```sh
   docker stop unoptimized && docker rm unoptimized
   ```

4. **Lancez l’image optimisée** :  
   ```sh
   docker run -d --name optimized -p 3000:3000 node-optimized
   ```

5. **Comparez les performances et la consommation mémoire des deux versions** :  
   ```sh
   docker ps -a
   docker stats
   ```  
   **Question** : Voyez-vous une différence dans la consommation de ressources ?

---

## **✅ Conclusion**
🎯 **Vous avez appris à optimiser une image Docker en utilisant Multi-Stage Build !**  
🎯 **Votre image est plus légère et sécurisée, tout en conservant les fichiers essentiels.**  
🎯 **Cette approche est idéale pour les environnements de production !** 🚀  


