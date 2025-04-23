
---
## **Accès au laboratoire**

### **🔑 Préparation de la clé ssh**

Vous avez tous reçu un courriel pour votre accès au laboratoire qui contien un fichier appelé: lq-20250423

Téléversé le  dans votre environnement AWS cloud9 ou AWS CloudShell (upload)

Dans le terminal fait:

Changer les permissions du fichier  lq-20250423


```bash
chmod 600  lq-20250423
```

### **🔄 Accès au laboraoire**

Toujours dans le même courriel, vous avez une commande ssh personnalisée qui vous permette de vous connecter à votre environnement de laboratoire. La commande ssh ressemble à ceci:

```bash
ssh -p 2222 ansible@ubuntu-c.user-1099+ycyr@1.2.3.4 -i lq-20250423
```

Si tout va bien, vous serez connecté au serveur `ubuntu-c` avec l'usager `ansible`


### **📤 Tester le ping vers les serveur centos(1-3) et ubuntu(1-3)**

```bash
ansible@ubuntu-c:~$ ping centos1
PING centos1.incus (10.4.142.149) 56(84) bytes of data.
64 bytes from centos1.incus (10.4.142.149): icmp_seq=1 ttl=64 time=0.188 ms
```

### **📂 Mots de passe**
- Usager: `root`, mot de passe: `password`
- Usager: `ansible`, mot de passe: `password` 
