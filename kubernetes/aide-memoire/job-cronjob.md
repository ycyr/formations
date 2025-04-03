# 📄 Cheat Sheet – Jobs et CronJobs dans Kubernetes

> Résumé YAML pour `Job` et `CronJob`, avec leurs champs importants.

---

## ⚡ `Job` – Exécution unique

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: hello-job
spec:
  backoffLimit: 3
  template:
    spec:
      containers:
      - name: hello
        image: busybox
        command: ["sh", "-c", "echo Hello World && sleep 5"]
      restartPolicy: OnFailure
```

---

### 🔹 Champs clés d’un `Job`

| Champ              | Description                                           |
|--------------------|-------------------------------------------------------|
| `backoffLimit`     | Nombre de réessais avant abandon                      |
| `template.spec`    | Identique à un Pod                                    |
| `restartPolicy`    | Doit être `OnFailure` ou `Never`                      |
| `ttlSecondsAfterFinished` | Auto-suppression après exécution (optionnel) |

---

## ⏱️ `CronJob` – Exécution planifiée

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello-cron
spec:
  schedule: "*/5 * * * *"
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 2
  failedJobsHistoryLimit: 1
  jobTemplate:
    spec:
      backoffLimit: 2
      template:
        spec:
          containers:
          - name: cron
            image: busybox
            command: ["sh", "-c", "date; echo Hello from cronjob"]
          restartPolicy: OnFailure
```

---

### 🔹 Champs clés d’un `CronJob`

| Champ                     | Description                                      |
|---------------------------|--------------------------------------------------|
| `schedule`                | Syntaxe cron (`* * * * *`)                       |
| `concurrencyPolicy`       | `Allow`, `Forbid`, `Replace`                    |
| `successfulJobsHistoryLimit` | Historique des jobs réussis à conserver    |
| `failedJobsHistoryLimit`  | Historique des jobs échoués à conserver         |
| `startingDeadlineSeconds` | Délai max pour démarrer un job planifié         |

---

## 📘 Exemples de `schedule` (cron)

| Schedule            | Fréquence                        |
|---------------------|----------------------------------|
| `"*/5 * * * *"`     | Toutes les 5 minutes             |
| `"0 * * * *"`       | Toutes les heures                |
| `"30 3 * * *"`      | Tous les jours à 03h30           |

---

## 📌 Différence visuelle : Job vs CronJob

```
Job
 └── Pod

CronJob
 └── Job (planifié à l'heure)
      └── Pod
```

---

## ✅ Commandes utiles

```bash
kubectl get jobs
kubectl get cronjobs
kubectl describe job hello-job
kubectl logs job/hello-job
```

```bash
kubectl create -f job.yaml
kubectl delete job hello-job
```

---

## 🧪 Génération rapide (Job)

```bash
kubectl create job test --image=busybox -- sh -c "echo Yo" --dry-run=client -o yaml
```

📌 `kubectl run` ne crée pas de Job si `--restart=Always`

---

## ✅ Best practices

- Utiliser `restartPolicy: OnFailure`
- Définir `backoffLimit` et `concurrencyPolicy`
- Nettoyer les Jobs avec `ttlSecondsAfterFinished`
