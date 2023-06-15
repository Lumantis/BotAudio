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

Version 1.0.2 (15 juin 2023) :

- Correction d'un bug où le bot ne se connectait pas correctement à un canal vocal lors de l'utilisation de la commande /lire.
- Amélioration de la gestion des exceptions lors de l'extraction des informations de la playlist.
- Utilisation de chemins relatifs pour les fichiers afin d'améliorer la portabilité du code.
- Optimisation de l'utilisation des fonctions asynchrones pour les opérations d'E/S.
- Ajout de la gestion des exceptions spécifiques lors de la connexion au canal vocal dans la commande /lire.
- Utilisation de la méthode disconnect() pour déconnecter le bot du canal vocal dans la classe MusicPlayer.
- Utilisation de l'événement on_voice_state_update pour gérer les actions à effectuer lorsque le bot est déconnecté d'un canal vocal.
- Utilisation de discord.AutoShardedClient pour la gestion automatique des sessions shardless.
- Amélioration de la fonction add_to_queue dans la classe MusicPlayer pour éviter le spam du canal vocal lors de l'ajout de titres. (encore expérimental)


Version 1.0.1 (14 juin 2023) :

- Ajout de la fonctionnalité de gestion de playlist. (expérimental)
- Gestion des exceptions lors de l'extraction des informations de la playlist pour éviter les blocages.
- Ajout de la prise en charge de la dernière version de la bibliothèque yt_dlp.
- Correction de bugs mineurs et améliorations générales.
