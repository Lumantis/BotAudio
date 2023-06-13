![Cover](https://github.com/Lumantis/BotAudio/blob/main/NikouliMakouli.png)

# Nikouli Makouli Bot

Ce bot Discord, écrit en Python, permet aux utilisateurs de lire des vidéos YouTube dans un canal vocal. Il utilise la bibliothèque discord.py ainsi que yt_dlp pour télécharger l'audio des vidéos YouTube.

## Fonctionnalités

- Jouer de l'audio à partir de vidéos YouTube dans un canal vocal.
- Mise en pause, reprise, et passage à la prochaine piste.
- Gestion de la file d'attente de lecture.
- Nettoyage du dossier de playlist.
- Déconnexion du canal vocal.

### Comment l'installer et l'utiliser

1. Clonez ce repo sur votre machine locale.
2. Installez les dépendances nécessaires (voir REQUIREMENTS.txt).
3. Creez un fichier .env à la racine du projet et ajoutez le token du bot (DISCORD_TOKEN=Le-token-de-votre-bot)
4. Exécutez `main.py`.

#### Commandes

- `/lire [url]`: Le bot rejoint votre canal vocal et commence à lire la vidéo YouTube à l'URL donnée.
- `/find [nom_de_la_piste]`: Le bot recherche le nom de la piste sur YouTube et joue la première correspondance.
- `/clean`: Supprime tous les fichiers dans le dossier de la playlist. Nécessite des permissions de gestion des messages.
- `/quitter`: Le bot quitte le canal vocal.

##### Note

Ce bot a été conçu à des fins éducatives et n'est pas destiné à un usage commercial.
