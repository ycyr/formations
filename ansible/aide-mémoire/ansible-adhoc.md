
---

## 🧾 **Ansible - Commandes Ad-Hoc (Cheat Sheet)**

### ✅ **Syntaxe Générale**
```bash
ansible <hôte|groupe> -i <inventory> -m <module> -a "<arguments>" [options]
```

---

### 📦 **Modules Fréquemment Utilisés**

#### 🔹 `ping` – Test de connectivité Ansible
```bash
ansible all -i hosts.txt -m ping
```

#### 🔹 `setup` – Afficher les facts (données système)
```bash
ansible all -i hosts.txt -m setup
```

#### 🔹 `command` – Exécuter une commande (pas de shell features)
```bash
ansible all -i hosts.txt -m command -a "uptime"
```

#### 🔹 `shell` – Exécuter des commandes shell (redir, pipes…)
```bash
ansible all -i hosts.txt -m shell -a "echo \$PATH | grep usr"
```

#### 🔹 `copy` – Copier un fichier local sur l'hôte distant
```bash
ansible all -i hosts.txt -m copy -a "src=~/fichier.txt dest=/tmp/"
```

#### 🔹 `file` – Créer ou supprimer fichiers/dossiers
```bash
ansible all -i hosts.txt -m file -a "path=/tmp/monfichier state=touch"
ansible all -i hosts.txt -m file -a "path=/tmp/dossier state=directory"
```

#### 🔹 `fetch` – Récupérer un fichier distant vers la machine locale
```bash
ansible all -i hosts.txt -m fetch -a "src=/etc/hosts dest=./backups/ flat=yes"
```

#### 🔹 `apt` (Ubuntu/Debian) – Installer un paquet
```bash
ansible ubuntu -i hosts.txt -m apt -a "name=htop state=present update_cache=yes"
```

#### 🔹 `yum` (RHEL/CentOS) – Installer un paquet
```bash
ansible centos -i hosts.txt -m yum -a "name=git state=latest"
```

#### 🔹 `package` – Interface commune à `apt`, `yum`, etc.
```bash
ansible all -i hosts.txt -m package -a "name=curl state=present"
```

#### 🔹 `service` – Gérer un service (start/stop/restart)
```bash
ansible all -i hosts.txt -m service -a "name=nginx state=restarted"
```

---

### ⚙️ **Options Utiles**

| Option                    | Description                                  |
|---------------------------|----------------------------------------------|
| `-u <user>`               | Spécifier l’utilisateur distant              |
| `-k`                      | Demande du mot de passe SSH                  |
| `-b`                      | Utiliser `become` pour privilèges root      |
| `--ask-become-pass`       | Demande le mot de passe sudo                 |
| `--private-key=~/.ssh/key.pem` | Utiliser une clé privée spécifique    |
| `--limit <hôte>`          | Limiter à un ou plusieurs hôtes              |
| `-e var=value`            | Passer une variable depuis la CLI            |

---

### 🧠 **Astuces**

- 🔍 **Lister les modules disponibles :**
  ```bash
  ansible-doc -l
  ```

- 📖 **Documentation sur un module :**
  ```bash
  ansible-doc file
  ```

- 💡 **Créer une tâche temporaire :**
  ```bash
  ansible all -i hosts.txt -m shell -a "date > /tmp/rapport.txt"
  ```

