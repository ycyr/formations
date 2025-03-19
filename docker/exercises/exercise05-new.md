<<<<<<< HEAD
=======
## **🛠 Exercice 5 : Créer et utiliser un volume Docker**
>>>>>>> 309d184949078e0d1184982e050dd86bf993347a

# **📝 Exercice 9 : Utilisation des Variables d'Environnement dans Docker 🚀**

## **📌 Objectif**
Cet exercice vous permettra de comprendre comment utiliser les **variables d’environnement** dans un `Dockerfile` et lors de l’exécution d’un conteneur.

✅ **Définir des variables d’environnement dans un `Dockerfile`**  
✅ **Passer des variables lors du lancement d’un conteneur**  
✅ **Utiliser un fichier `.env` pour gérer les variables**  

---

## **🎯 Partie 1 : Définition des variables d’environnement dans un `Dockerfile`**
1. **Créez un dossier `env_test/` et ajoutez un fichier `Dockerfile`** :
   ```dockerfile
   FROM ubuntu:latest

<<<<<<< HEAD
   # Définition d'une variable d'environnement
   ENV MESSAGE="Bonjour depuis Docker !"

   CMD ["bash", "-c", "echo $MESSAGE"]
   ```
2. **Construisez l’image Docker** :
   ```sh
   docker build -t env-example ./env_test
   ```
3. **Lancez un conteneur et observez le message affiché** :
   ```sh
   docker run env-example
   ```
   **Question :** Quelle est la valeur affichée et d’où vient-elle ?
=======
7️⃣ **Supprimer un volume (après suppression des conteneurs qui l’utilisent)**
```sh
docker volume rm mon-volume
```
>>>>>>> 309d184949078e0d1184982e050dd86bf993347a

4. **Essayez de passer une nouvelle valeur à `MESSAGE` lors de l’exécution** :
   ```sh
   docker run -e MESSAGE="Salut les étudiants ! 🚀" env-example
   ```
   **Question :** Pourquoi la valeur de `MESSAGE` a-t-elle changé ?

---

<<<<<<< HEAD
## **🎯 Partie 2 : Définition des variables via un fichier `.env`**
1. **Créez un fichier `.env` dans `env_test/`** avec le contenu suivant :
   ```ini
   MESSAGE="Bonjour depuis le fichier .env !"
   ```
2. **Lancez un conteneur en chargeant les variables depuis le fichier `.env`** :
   ```sh
   docker run --env-file ./env_test/.env env-example
   ```
3. **Explication** :  
   - `--env-file` charge automatiquement **les variables définies dans le fichier `.env`**.
   - Cela permet de **gérer proprement des variables sensibles** comme des mots de passe.

   **Question :** Quels sont les avantages d’utiliser un fichier `.env` plutôt que `-e` ?

---

## **🎯 Partie 3 : Passer des variables d’environnement à une application Python**
1. **Créez un fichier `app.py` dans `env_test/`** avec le contenu suivant :
   ```python
   import os

   message = os.getenv("MESSAGE", "Valeur par défaut !")
   print(f"Le message est : {message}")
   ```
2. **Modifiez votre `Dockerfile` pour exécuter le script Python** :
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY app.py .

   ENV MESSAGE="Message par défaut dans le Dockerfile"

   CMD ["python", "app.py"]
   ```
3. **Recréez l’image Docker** :
   ```sh
   docker build -t env-python-example ./env_test
   ```
4. **Testez l’exécution avec différentes valeurs de variables** :
   ```sh
   docker run env-python-example
   docker run -e MESSAGE="Nouveau message !" env-python-example
   docker run --env-file ./env_test/.env env-python-example
   ```

   **Question :** Comment la variable est-elle récupérée dans Python ?

---

## **✅ Conclusion**
Dans cet exercice, vous avez appris que :  
✔️ **Les variables d’environnement peuvent être définies dans un `Dockerfile` avec `ENV`**.  
✔️ **On peut les passer dynamiquement avec `-e` lors de l’exécution**.  
✔️ **Les fichiers `.env` permettent de centraliser les variables sans les écrire dans le `Dockerfile`**.  
✔️ **Les applications peuvent lire ces variables avec `os.getenv()` en Python**.  
=======
[Aide Mémoire Dockerfile](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/dockerfile-cheatsheet.md)
>>>>>>> 309d184949078e0d1184982e050dd86bf993347a
