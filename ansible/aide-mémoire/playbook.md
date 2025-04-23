
---

## 🧾 **Cheat Sheet – Playbooks Ansible**

---

### 📚 **Structure Générale d’un Playbook**
```yaml
- name: Nom du playbook
  hosts: groupe_ou_hôte
  become: true               # Élévation de privilèges
  gather_facts: true         # Collecte automatique de facts

  vars:                      # Variables internes
    fichier: "/etc/motd"

  tasks:                     # Liste des tâches
    - name: Affiche un message
      debug:
        msg: "Hello depuis {{ inventory_hostname }}"

    - name: Créer un fichier
      file:
        path: "{{ fichier }}"
        state: touch

  handlers:                  # Déclenchés par notify
    - name: restart service
      service:
        name: apache2
        state: restarted
```

---

### 🔑 **Paramètres Clés d’un Playbook**

| Paramètre         | Description |
|------------------|-------------|
| `name:`          | Nom lisible du playbook ou tâche |
| `hosts:`         | Groupe ou hôte cible |
| `become:`        | Permet d’agir avec les droits root |
| `gather_facts:`  | Active la collecte automatique des facts |
| `vars:`          | Variables internes |
| `tasks:`         | Liste ordonnée de tâches |
| `handlers:`      | Actions déclenchées avec `notify` |
| `when:`          | Condition pour exécuter une tâche |
| `tags:`          | Marque une tâche pour exécution sélective |
| `register:`      | Capture la sortie d’une tâche |
| `loop:` / `with_`:| Boucle sur des listes ou dictionnaires |

---

### 💡 **Exemples Courants**

#### 🔁 Utilisation de `loop`
```yaml
- name: Crée plusieurs fichiers
  file:
    path: "/tmp/{{ item }}"
    state: touch
  loop:
    - fichier1
    - fichier2
```

#### 🎯 Condition avec `when`
```yaml
- name: Redémarrer uniquement sous Ubuntu
  service:
    name: apache2
    state: restarted
  when: ansible_distribution == "Ubuntu"
```

#### 🧠 Utiliser `register` et `debug`
```yaml
- name: Vérifie un fichier
  command: ls /tmp
  register: resultat_ls

- debug:
    var: resultat_ls.stdout_lines
```

#### 📦 Inclure un rôle
```yaml
- hosts: all
  roles:
    - nom_du_role
```

---

### 📁 **Répertoires Externes de Variables**

- `group_vars/<nom_groupe>.yml` : variables propres à un groupe
- `host_vars/<nom_hôte>.yml` : variables propres à un hôte

---

### 🧪 **Conseils Bonus**

- Utilise `ansible-playbook --check` pour simuler
- Utilise `ansible-doc <module>` pour l’aide rapide
- Factorise les tâches récurrentes avec des **rôles**

---

