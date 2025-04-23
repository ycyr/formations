
---

## 🧾 **Cheat Sheet – `ansible-playbook`**

### 🛠️ **Structure de base d’un Playbook**
```yaml
- name: Nom du playbook
  hosts: nom_du_groupe
  become: true
  gather_facts: true

  vars:
    paquet: nginx

  tasks:
    - name: Installer un paquet
      apt:
        name: "{{ paquet }}"
        state: present
```

---

### 🧭 **Commande Générale**
```bash
ansible-playbook -i <fichier_inventaire> playbook.yml [options]
```

---

### 🔧 **Options Principales**

| Option | Description |
|--------|-------------|
| `-i <fichier>` | Spécifie le fichier d’inventaire |
| `-e var=val` | Définit ou surcharge une variable |
| `--ask-become-pass` | Demande le mot de passe sudo |
| `--check` | Mode simulation (dry run) |
| `--diff` | Affiche les différences de fichiers modifiés |
| `--syntax-check` | Vérifie la syntaxe du playbook |
| `--list-tasks` | Liste les tâches sans exécution |
| `--start-at-task="nom"` | Commence à une tâche précise |
| `--tags "tag1,tag2"` | N'exécute que les tâches taggées |
| `--skip-tags "tag"` | Ignore certaines tâches |
| `--step` | Interactivité : confirme chaque tâche |
| `--limit hôte` | Restreint aux hôtes spécifiés |
| `--vault-id` | Spécifie une clé ou fichier pour vault |
| `-v/-vv/-vvv/-vvvv` | Verbosité (niveau croissant) |

---

### 🚀 **Exemples de Commandes Utiles**

#### ✅ Lancer un playbook
```bash
ansible-playbook -i hosts.txt site.yml
```

#### 💡 Passer une variable à la volée
```bash
ansible-playbook playbook.yml -e "paquet=htop"
```

#### 📍 Exécuter un tag spécifique
```bash
ansible-playbook playbook.yml --tags "install"
```

#### 🚫 Ignorer des tags
```bash
ansible-playbook playbook.yml --skip-tags "restart"
```

#### 🔍 Tester sans exécuter
```bash
ansible-playbook playbook.yml --check --diff
```

#### 🎯 Limiter à un hôte ou groupe
```bash
ansible-playbook playbook.yml --limit centos1
```

#### 🧪 Liste des tâches sans exécution
```bash
ansible-playbook playbook.yml --list-tasks
```

#### 🚀 Exécuter en mode interactif
```bash
ansible-playbook playbook.yml --step
```

---

### 🧠 **Tips Supplémentaires**

- Utiliser `ansible.cfg` pour centraliser les configs
- Organiser vos rôles avec `ansible-galaxy init mon_role`
- Utilisez `ansible-vault` pour sécuriser des fichiers sensibles
- Regrouper les variables dans `group_vars` et `host_vars`

---