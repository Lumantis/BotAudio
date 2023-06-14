import asyncio
import os
import shutil
import discord
import yt_dlp
from dotenv import load_dotenv
from discord.ext import commands
from MusicPlayer import MusicPlayer
from ui import MusicButtonsView
from youtube_utils import search_youtube

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='/', intents=intents)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'playlist/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

players = {}

@bot.event
async def on_ready():
    print('Bot is ready!')
    # Vérifier si le dossier "playlist" existe, sinon le créer.
    if not os.path.exists('playlist'):
        os.makedirs('playlist')

@bot.command()
async def lire(ctx, url):
    player = players.get(ctx.guild.id)

    if not player:
        if not ctx.author.voice:
            return await ctx.send('Vous devez être dans un canal vocal pour utiliser cette commande.')

        player = MusicPlayer(ctx, ydl_opts)
        players[ctx.guild.id] = player

    if not player.voice_client:
        await player.connect_to_voice_channel()

    if player.voice_client:
        await player.add_to_queue(url)

        if not player.voice_client.is_playing() and len(player.queue) > 0:
            await player.play()
    else:
        await ctx.send('Je ne peux pas me connecter au canal vocal.')

@bot.command()
async def clean(ctx):
    if ctx.author.guild_permissions.manage_messages:
        shutil.rmtree('playlist', ignore_errors=True)
        os.makedirs('playlist', exist_ok=True)
        await ctx.send('Le dossier de la playlist a été nettoyé.')
    else:
        await ctx.send('Vous devez avoir la permission de gérer les messages pour utiliser cette commande.')

@bot.command()
async def playlist(ctx, url):
    player = players.get(ctx.guild.id)

    if not player:
        if not ctx.author.voice:
            return await ctx.send('Vous devez être dans un canal vocal pour utiliser cette commande.')

        player = MusicPlayer(ctx, ydl_opts)
        players[ctx.guild.id] = player

    if not player.voice_client:
        await player.connect_to_voice_channel()

    if player.voice_client:
        # Les options de yt-dlp, avec 'ignoreerrors' défini sur True
        ydl_opts_with_ignore_errors = {**ydl_opts, 'ignoreerrors': True}

        # Extraire les URLs des vidéos de la playlist
        with yt_dlp.YoutubeDL(ydl_opts_with_ignore_errors) as ydl:
            try:
                playlist_info = ydl.extract_info(url, download=False)
                video_urls = [f"https://www.youtube.com/watch?v={video['id']}" for video in playlist_info["entries"] if video is not None]
            except yt_dlp.utils.DownloadError:
                return await ctx.send("Impossible d'extraire les informations de la playlist. Vérifiez l'URL et réessayez.")

        added_videos = 0  # Initialiser le compteur de vidéos ajoutées
        # Ajouter chaque vidéo à la file d'attente
        for video_url in video_urls:
            await player.add_to_queue(video_url)
            added_videos += 1  # Incrémenter le compteur à chaque ajout de vidéo

        # Si le bot ne joue pas et que la file d'attente n'est pas vide, commencer à jouer
        if not player.voice_client.is_playing() and len(player.queue) > 0:
            await player.play()

        # Envoyer un message lorsque toutes les vidéos de la playlist ont été ajoutées à la file d'attente
        await ctx.send(f"{added_videos} vidéos de la playlist ont été ajoutées à la file d'attente. Il y a maintenant {len(player.queue)} vidéos en file d'attente.")
    else:
        await ctx.send('Je ne peux pas me connecter au canal vocal.')
       
@bot.command()
async def find(ctx, *, track_name):
    youtube_url = search_youtube(track_name)
    if youtube_url:
        await lire(ctx, youtube_url)
    else:
        await ctx.send("Track not found.")

@bot.command()
async def quitter(ctx):
    player = players.get(ctx.guild.id)
    if player and player.voice_client:
        await player.disconnect_from_voice_channel()
        await ctx.send('Déconnexion.')
        players[ctx.guild.id] = None
    else:
        await ctx.send('Je ne suis pas connecté à un canal vocal.')

@bot.event
async def on_disconnect():
    shutil.rmtree('playlist')
    os.mkdir('playlist')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(TOKEN)
