# Module 5

## Démarrer

### Lancer le projet

La commande suivante permet de lancer le frontend, le backend, le grafana, et le Uptime Kuma du projet.

```bash
docker compose up
```

## Composants

### Backend (port 8000)

Une API HTTP exposant les *endpoints* suivants :

- **/calcul :** Permet d'obtenir le carré d'un nombre
- **/health :** Permet de connaître le statut de l'API

#### Tests unitaires

Le backend possède des tests unitaires sur la fonction `calcul`. Leur contenu peut être trouvé dans le fichier `backend/test/test_calcul.py`

**L'évaluation des tests unitaires est déclenchée par une GitHub Action à chaque nouveau commit.**

## Frontend (port 8080)

Interface *Streamlit* permettant d'interagir avec le backend.

![Interface Streamlit](./media/frontend.png)

## Grafana (port 3000)

Le Grafana permet de monitorer l'utilisation des ressources par le projet.

![grafana](./media/grafana.png)

## Uptime Kuma (port 3001)

L'interface Uptime Kuma permet de surveiller la disponibilité de l'API et d'envoyer des alerts Discord en cas de panne.

![uptime kuma](./media/uptime-kurma.png)

![discord alerting](./media/down-alert-discord.png)

## CI/CD

Les tests unitaires sont évalués à chaque commit sur `main`.

La construction et la publication des images Docker des composants Frontend et Backend sont réalisées à chaque publication de tag.

![Dockerhub](./media/dockerhub.png)