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

- DISCORD_TOKEN=Votre-Token-Discord
- PLUGINS=True

## Commandes

- `/lire <url>` : Fait lire une piste de musique par le bot à partir de l'URL de YouTube spécifiée
- `/playlist <url>` : Fait lire une playlist de musique par le bot à partir de l'URL de YouTube spécifiée
- `/quitter` : Fait quitter le canal vocal au bot
- `/clean` : Nettoie le dossier de la playlist (nécessite des permissions de gestion des messages)
- `/find <track_name>` : Recherche une piste sur YouTube et la met en file d'attente pour être lue
- `/net` : supprime tous les messages textuels du chat dans lequel la commande a été envoyée. (plugin - nécessite des permissions de gestion des messages)


###### Patchnotes

Version 1.0.4 (18 juin 2023) :

- Ajout de la fonctionnalité d'activation et de désactivation des plugins via le fichier `.env`.
- Suppression de l'importation statique des plugins et ajout d'un système dynamique pour charger les plugins en fonction de la configuration.
- Ajout d'un plugin pour supprimer tous les messages dans un canal textuel à l'aide de la commande `/net`.
- Amélioration des boutons de contrôle de la musique en ajoutant un contrôle pour éviter l'usage de boutons quand il n'y a pas de musique en cours.
- Modification de l'affichage des boutons de contrôle de la musique pour utiliser des emojis au lieu de texte. (expérimental)


Version 1.0.3 (17 juin 2023) :

- Ajout de blocs `try/except` autour des appels de fonction qui pourraient échouer, comme le téléchargement de vidéos ou l'ajout de vidéos à la file d'attente. Lorsqu'une erreur se produit, un message est envoyé à l'utilisateur pour l'informer de l'erreur.
- Certaines fonctionnalités ont été déplacées dans des méthodes séparées pour améliorer la modularité du code. Par exemple, la logique pour ajouter une vidéo à la file d'attente a été déplacée dans une méthode séparée `add_to_queue`.
- Ajout de commentaires afin de rendre le code plus lisible.
- Le bot se déconnecte maintenant du canal vocal lorsqu'il est fermé pour s'assurer que les ressources sont correctement libérées.
- Utilisation des plugins pour ajouter des fonctionnalités supplémentaires. Cela permet d'encapsuler des fonctionnalités spécifiques dans des modules séparés. (experimental)
- Utilisation des événements pour gérer les interactions avec Discord. Cela permet au bot de réagir de manière plus flexible et dynamique aux actions des utilisateurs.
- Mise à jour du nombre maximal de titres pouvant être ajoutés à la liste d'attente. (100 => 50)


Version 1.0.2 (15 juin 2023) :

- Correction d'un bug où le bot ne se connectait pas correctement à un canal vocal lors de l'utilisation de la commande `/lire`.
- Amélioration de la gestion des exceptions lors de l'extraction des informations de la playlist.
- Utilisation de chemins relatifs pour les fichiers afin d'améliorer la portabilité du code.
- Optimisation de l'utilisation des fonctions asynchrones pour les opérations d'E/S.
- Ajout de la gestion des exceptions spécifiques lors de la connexion au canal vocal dans la commande /lire.
- Utilisation de la méthode `disconnect()` pour déconnecter le bot du canal vocal dans la classe `MusicPlayer`.
- Utilisation de l'événement `on_voice_state_update` pour gérer les actions à effectuer lorsque le bot est déconnecté d'un canal vocal.
- Utilisation de `discord.AutoShardedClient` pour la gestion automatique des sessions shardless.
- Amélioration de la fonction `add_to_queue` dans la classe `MusicPlayer` pour éviter le spam du canal textuel lors de l'ajout de titres. (encore expérimental)


Version 1.0.1 (14 juin 2023) :

- Ajout de la fonctionnalité de gestion de playlist : `/playlist + url` (expérimental)
- Gestion des exceptions lors de l'extraction des informations de la playlist pour éviter les blocages.
- Ajout de la prise en charge de la dernière version de la bibliothèque `yt_dlp`.
- Correction de bugs mineurs et améliorations générales.
