![Cover](https://github.com/Lumantis/BotAudio/blob/bugged-do-not-use-master/NikouliMakouli.png)

# Nikouli Makouli Audio Bot

Le Nikouli Makouli Audio Bot est un bot Discord qui permet de lire de la musique provenant de YouTube sur un canal vocal.

## Caractéristiques
* Rejoindre et quitter des canaux vocaux ;
* Télécharger et lire des liens à partir de YouTube ;
* Télécharger et lire des playlists YouTube ;
* Mettre en pause, reprendre et passer des pistes ;

## Installation
1. Clonez ce dépôt
2. Installez les dépendances en exécutant `pip install -r requirements.txt`
3. Configurez vos variables d'environnement dans un fichier `.env`. Voir [Exemple de fichier .env](#exemple-de-fichier-env)
4. Lancez le bot avec `python main.py`

## Exemple de fichier `.env`
```env
DISCORD_TOKEN=Votre-Token-Discord
```
## Commandes
/lire <url> : Fait lire une piste de musique par le bot à partir de l'URL de YouTube spécifiée
/find <track_name> : Recherche une piste sur YouTube et la met en file d'attente pour être lue
/playlist <url> : Fait lire une playlist de musique par le bot à partir de l'URL de YouTube spécifiée
/twitch : permet la lecture d'un flux audio twitch sur un channel vocal discord.

/quitter : Fait quitter le canal vocal au bot
/clean : Nettoie le dossier de la playlist (nécessite des permissions de gestion des messages)

/net : permet de nettoyer un salon textuel (nécéssite des permissions de gestion de messages)

## Patchnotes
<details> 
  <summary><i>Version 1.0.4.1 (24 juin 2023) :</i></summary>
- Ajout de la commande /twitch <lien du live> permettant la lecture d'une vidéo twitch en mode radio sur un channel vocal discord.
- Optimisation du code.
  </details>
<details> 
  <summary><i>Version 1.0.4 (23 juin 2023) :</i></summary>
- Optimisation de la gestion de la file d'attente : Le téléchargement de la chanson suivante est désormais effectué pendant que la chanson actuelle est en train de jouer, afin de réduire le délai de lecture.
- Modification des options yt-dlp : Les options ont été modifiées pour télécharger directement le fichier audio au format MP3, ce qui réduit le temps de traitement et l'utilisation du CPU.
- Ajout de la gestion des erreurs de téléchargement : En cas d'échec du téléchargement, un message est renvoyé.
- Correction de bugs mineurs et améliorations générales.
- Ajout de la commande /net permettant de nettoyer les messages d'un serveur textuel Discord.
  </details>
 <details> 
  <summary><i>Version 1.0.3 (22 juin 2023) :</i></summary>
- Correction d'un bug où le bot ne se connectait pas correctement à un canal vocal lors de l'utilisation de la commande /lire.
- Amélioration de la gestion des exceptions lors de l'extraction des informations de la playlist.
- Utilisation de chemins relatifs pour les fichiers afin d'améliorer la portabilité du code.
- Optimisation de l'utilisation des fonctions asynchrones pour les opérations d'E/S.
- Ajout de la gestion des exceptions spécifiques lors de la connexion au canal vocal dans la commande /lire.
- Utilisation de la méthode disconnect() pour déconnecter le bot du canal vocal dans la classe MusicPlayer.
- Utilisation de l'événement on_voice_state_update pour gérer les actions à effectuer lorsque le bot est déconnecté d'un canal vocal.
- Utilisation de discord.AutoShardedClient pour la gestion automatique des sessions shardless.
- Amélioration de la fonction add_to_queue dans la classe MusicPlayer pour éviter le spam du canal textuel lors de l'ajout de titres. (encore expérimental)
  </details>
 <details> 
  <summary><i>Version 1.0.2 (15 juin 2023) :</i></summary>
- Ajout de la fonctionnalité de gestion de playlist : /playlist + url (expérimental)
- Gestion des exceptions lors de l'extraction des informations de la playlist pour éviter les blocages.
- Ajout de la prise en charge de la dernière version de la bibliothèque yt_dlp.
- Correction de bugs mineurs et améliorations générales.
</details>
 <details> 
  <summary><i>Version 1.0.1 (14 juin 2023) :</i></summary>
- Ajout de la fonctionnalité de lecture de pistes individuelles à partir de liens YouTube.
- Gestion des erreurs lors de l'extraction des informations des vidéos YouTube.
- Ajout de la commande /find pour rechercher et ajouter une piste à la file d'attente.
- Correction de bugs mineurs et améliorations générales.
</details>
</details>
