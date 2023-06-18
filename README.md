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

`DISCORD_TOKEN=Votre-Token-Discord`

## Commandes

- `/lire <url>` : Fait lire une piste de musique par le bot à partir de l'URL de YouTube spécifiée
- `/playlist <url>` : Fait lire une playlist de musique par le bot à partir de l'URL de YouTube spécifiée
- `/quitter` : Fait quitter le canal vocal au bot
- `/clean` : Nettoie le dossier de la playlist (nécessite des permissions de gestion des messages)
- `/find <track_name>` : Recherche une piste sur YouTube et la met en file d'attente pour être lue

##### Note

Ce bot a été conçu à des fins éducatives et n'est pas destiné à un usage commercial.

# Patch Notes

## Version 1.0.4 (18 juin 2023) :

- Ajout d'une gestion de plugins pour le bot. Vous pouvez maintenant activer et désactiver l'utilisation des plugins en modifiant la valeur de la variable d'environnement PLUGINS dans le fichier .env.
- Modification de la structure du code pour séparer la logique des plugins du reste du code.
- Ajout de la fonction `load_plugins` qui charge tous les plugins situés dans le dossier plugins si l'utilisation des plugins est activée.
- Modification de la structure du dossier : un nouveau dossier plugins a été créé pour stocker les plugins. Le bot vérifiera et créera ce dossier au démarrage si l'utilisation des plugins est activée.
- Modification de la méthode `on_ready` : le bot vérifie et crée maintenant les dossiers playlist et plugins au démarrage.
- Suppression du bloc de code initial de chargement des plugins et remplacement par l'appel à la fonction `load_plugins`.
- Modification du fichier `.env` pour inclure la nouvelle variable d'environnement PLUGINS. Vous pouvez la définir sur True ou False pour activer ou désactiver l'utilisation des plugins.
- Refonte du système de gestion des fichiers de plugins pour utiliser un format plus propre et plus efficace. Chaque plugin est maintenant dans son propre fichier dans le dossier plugins, ce qui permet une organisation et une maintenance plus faciles.
- Ajout d'une nouvelle structure pour les plugins, qui leur permet de se définir comme une sous-classe de `commands.Cog`, facilitant ainsi leur intégration avec le bot.

## Version 1.0.3 (17 juin 2023) :

- Ajout de blocs `try/except` autour des appels de fonction qui pourraient échouer, comme le téléchargement de vidéos ou l'ajout de vidéos à la file d'attente. Lorsqu'une erreur se produit, un message est envoyé à l'utilisateur pour l'informer de l'erreur.
- Certaines fonctionnalités ont été déplacées dans des méthodes séparées pour améliorer la modularité du code. Par exemple, la logique pour ajouter une vidéo à la file d'attente a été déplacée dans une méthode séparée `add_to_queue`.
- Ajout de commentaires afin de rendre le code plus lisible.
- Le bot se déconnecte maintenant du canal vocal lorsqu'il est fermé pour s'assurer que les ressources sont correctement libérées.
- Utilisation des plugins pour ajouter des fonctionnalités supplémentaires. Cela permet d'encapsuler des fonctionnalités spécifiques dans des modules séparés. (experimental)
- Utilisation des événements pour gérer les interactions avec Discord. Cela permet au bot de réagir de manière plus flexible et dynamique aux actions des utilisateurs.
- Mise à jour du nombre maximal de titres pouvant être ajoutés à la liste d'attente. (100 => 50)

## Version 1.0.2 (15 juin 2023) :

- Correction d'un bug où le bot ne se connectait pas correctement à un canal vocal lors de l'utilisation de la commande `/lire`.
- Amélioration de la gestion des exceptions lors de l'extraction des informations de la playlist.
- Utilisation de chemins relatifs pour les fichiers afin d'améliorer la portabilité du code.
- Optimisation de l'utilisation des fonctions asynchrones pour les opérations d'E/S.
- Ajout de la gestion des exceptions spécifiques lors de la connexion au canal vocal dans la commande /lire.
- Utilisation de la méthode `disconnect()` pour déconnecter le bot du canal vocal dans la classe `MusicPlayer`.
- Utilisation de l'événement `on_voice_state_update` pour gérer les actions à effectuer lorsque le bot est déconnecté d'un canal vocal.
- Utilisation de `discord.AutoShardedClient` pour la gestion automatique des sessions shardless.
- Amélioration de la fonction `add_to_queue` dans la classe `MusicPlayer` pour éviter le spam du canal textuel lors de l'ajout de titres. (encore expérimental)

## Version 1.0.1 (14 juin 2023) :

- Ajout de la fonctionnalité de gestion de playlist : `/playlist + url` (expérimental)
- Gestion des exceptions lors de l'extraction des informations de la playlist pour éviter les blocages.
- Ajout de la prise en charge de la dernière version de la bibliothèque `yt_dlp`.
- Correction de bugs mineurs et améliorations générales.
