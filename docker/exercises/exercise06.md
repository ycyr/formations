## **🛠 Exercice 6 : Monter un fichier spécifique en bind mount**
📌 **Objectif** : Monter **un seul fichier** de l’hôte dans un conteneur et observer son comportement.

### **💡 Étapes :**
1️⃣ **Créer un fichier sur l’hôte** :
   ```sh
   echo "Contenu initial du fichier" > mon-fichier.txt
   ```
2️⃣ **Lancer un conteneur et monter ce fichier en bind mount** :
   ```sh
   docker run -dit --name conteneurFichier -v $(pwd)/mon-fichier.txt:/data/mon-fichier.txt ubuntu bash
   ```
3️⃣ **Modifier le fichier à partir du conteneur** :
   ```sh
   docker exec -it conteneurFichier bash -c "echo 'Modifié depuis le conteneur' >> /data/mon-fichier.txt"
   ```
4️⃣ **Vérifier que la modification est visible depuis l’hôte** :
   ```sh
   cat mon-fichier.txt
   ```
5️⃣ **Modifier le fichier depuis l’hôte et voir les changements dans le conteneur** :
   ```sh
   echo "Modifié depuis l'hôte" >> mon-fichier.txt
   docker exec -it conteneurFichier cat /data/mon-fichier.txt
   ```

📌 **Questions** :
- Que se passe-t-il si le conteneur est supprimé ?
- Que se passe-t-il si on relance le conteneur sans le bind mount ?


## *Références*

[Aide Mémoire Docker cli](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/docker-cli-cheatsheet.md)

[Aide Mémoire Dockerfile](https://github.com/ycyr/formations/blob/main/docker/aide-memoire/dockerfile-cheatsheet.md)