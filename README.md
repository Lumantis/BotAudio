![Cover](https://github.com/Lumantis/BotAudio/blob/main/NikouliMakouli.png)

# Nikouli Makouli Audio Bot

Un bot Discord qui peut lire de la musique provenant de YouTube. Ce bot a été développé en Python en utilisant la bibliothèque discord.py.

## Caractéristiques

- Rejoindre et quitter des canaux vocaux
- Lire de la musique à partir de YouTube
- Mettre en pause, reprendre et passer des pistes
- Télécharger et lire des playlists YouTube

## Instructions d'installation

1. Clonez ce dépôt
2. Installez les dépendances en exécutant `pip install -r requirements.txt`
3. Configurez vos variables d'environnement dans un fichier `.env` (voir exemple ci-dessous)
4. Lancez le bot avec `python main.py`

### Exemple de fichier `.env`

DISCORD_TOKEN=Votre-Token-Discord

## Commandes

- `/lire <url>` : Fait lire une piste de musique par le bot à partir de l'URL de YouTube spécifiée
- `/playlist <url>` : Fait lire une playlist de musique par le bot à partir de l'URL de YouTube spécifiée
- `/quitter` : Fait quitter le canal vocal au bot
- `/clean` : Nettoie le dossier de la playlist (nécessite des permissions de gestion des messages)
- `/find <track_name>` : Recherche une piste sur YouTube et la met en file d'attente pour être lue

##### Note

Ce bot a été conçu à des fins éducatives et n'est pas destiné à un usage commercial.

###### Patchnotes :

Version 1.0.1 (14 juin 2023) :

- Ajout de la fonctionnalité de gestion de playlist. (expérimental)
- Gestion des exceptions lors de l'extraction des informations de la playlist pour éviter les blocages.
- Ajout de la prise en charge de la dernière version de la bibliothèque yt_dlp.
- Correction de bugs mineurs et améliorations générales.
