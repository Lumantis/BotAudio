# Bot Audio

Ce bot Discord, écrit en Python, permet aux utilisateurs de lire des vidéos YouTube dans un canal vocal. Il utilise la bibliothèque discord.py ainsi que yt_dlp pour télécharger l'audio des vidéos YouTube.

## Fonctionnalités

- Jouer de l'audio à partir de vidéos YouTube dans un canal vocal.
- Mise en pause, reprise, et passage à la prochaine piste.
- Gestion de la file d'attente de lecture.
- Nettoyage du dossier de playlist.
- Déconnexion du canal vocal.

## Comment utiliser

1. Clonez ce repo sur votre machine locale.
2. Installez les dépendances nécessaires (voir REQUIREMENTS.txt).
3. Assurez-vous de remplacer le token fictif dans `main.py` par le token de votre bot Discord.
4. Exécutez `main.py`.

## Commandes

- `/lire <url>` : Joue l'audio de la vidéo YouTube à l'URL spécifiée.
- `/clean` : Nettoie le dossier de la playlist. Cette commande nécessite la permission de gérer les messages.
- `/find <track_name>` : Recherche une vidéo YouTube avec le nom de la piste donné et joue son audio.
- `/quitter` : Déconnecte le bot du canal vocal.

## Note

Ce bot a été conçu à des fins éducatives et n'est pas destiné à un usage commercial.
