# **📝 Exercice 6 : Différencier `CMD` et `ENTRYPOINT` dans un `Dockerfile`**

## **📌 Objectif**
Cet exercice a pour but d’aider à comprendre la différence entre **CMD** et **ENTRYPOINT** dans un `Dockerfile`.  
Vous allez :  
✅ **Créer deux images Docker** : une utilisant `CMD` et l'autre `ENTRYPOINT`.  
✅ **Lancer des conteneurs et observer le comportement**.  
✅ **Modifier les commandes au lancement et comparer les résultats**.  

---

## **🎯 Partie 1 : Création d’une image avec `CMD`**
1. **Créez un dossier `cmd_test/` et ajoutez un fichier `Dockerfile`** :
   ```dockerfile
   FROM ubuntu:latest

   CMD ["echo", "Bonjour, ceci est une exécution par défaut avec CMD !"]
   ```
2. **Construisez l’image Docker** :
   ```sh
   docker build -t cmd-example ./cmd_test
   ```
3. **Lancez un conteneur et observez le comportement** :
   ```sh
   docker run cmd-example
   ```
   **Question :** Quel est le message affiché dans le terminal ?

4. **Essayez d’écraser la commande au lancement du conteneur** :
   ```sh
   docker run cmd-example ls -l
   ```
   **Question :** Que se passe-t-il et pourquoi ?

---

## **🎯 Partie 2 : Création d’une image avec `ENTRYPOINT`**
1. **Créez un dossier `entrypoint_test/` et ajoutez un fichier `Dockerfile`** :
   ```dockerfile
   FROM ubuntu:latest

   ENTRYPOINT ["echo", "Bonjour, ceci est une exécution forcée avec ENTRYPOINT !"]
   ```
2. **Construisez l’image Docker** :
   ```sh
   docker build -t entrypoint-example ./entrypoint_test
   ```
3. **Lancez un conteneur et observez le comportement** :
   ```sh
   docker run entrypoint-example
   ```
   **Question :** Quel est le message affiché dans le terminal ?

4. **Essayez d’écraser la commande au lancement du conteneur** :
   ```sh
   docker run entrypoint-example ls -l
   ```
   **Question :** Pourquoi la commande `ls -l` n’a-t-elle pas été exécutée ?

---

## **🎯 Partie 3 : Utiliser `ENTRYPOINT` avec `CMD` pour plus de flexibilité**
1. **Créez un dossier `entrypoint_cmd_test/` et ajoutez un fichier `Dockerfile`** :
   ```dockerfile
   FROM ubuntu:latest

   ENTRYPOINT ["echo"]
   CMD ["Ceci est un message par défaut avec CMD"]
   ```
2. **Construisez l’image Docker** :
   ```sh
   docker build -t entrypoint-cmd-example ./entrypoint_cmd_test
   ```
3. **Lancez un conteneur et observez le comportement** :
   ```sh
   docker run entrypoint-cmd-example
   ```
   **Question :** Pourquoi voit-on `Ceci est un message par défaut avec CMD` ?

4. **Écrasez uniquement `CMD` avec une autre commande** :
   ```sh
   docker run entrypoint-cmd-example "Un autre message"
   ```
   **Question :** Que se passe-t-il et pourquoi ?

5. **Essayez d’écraser `ENTRYPOINT` au lancement** :
   ```sh
   docker run --entrypoint "/bin/bash" entrypoint-cmd-example -c "ls -l"
   ```
   **Question :** Quelle est la différence avec l’écrasement de `CMD` ?

---

## **✅ Conclusion**
Dans cet exercice, vous avez appris que :  
✔️ **`CMD` est une commande par défaut qui peut être remplacée au runtime**.  
✔️ **`ENTRYPOINT` définit une commande obligatoire qui ne peut pas être remplacée facilement**.  
✔️ **`CMD` peut être utilisé en complément de `ENTRYPOINT` pour plus de flexibilité**. 
