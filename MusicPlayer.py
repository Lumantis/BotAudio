import asyncio
import yt_dlp
import discord
from ui import MusicButtonsView

class MusicPlayer:
    def __init__(self, ctx, ydl_opts):
        self.ctx = ctx
        self.ydl_opts = ydl_opts
        self.queue = []
        self.voice_client = None
        self.current_file_path = None
        self.is_playing = False
        self.track_end = asyncio.Event()

    async def play(self):
        if self.is_playing:
            return

        self.is_playing = True
        while len(self.queue) > 0:
            url = self.queue.pop(0)

            # Execute download in background
            loop = asyncio.get_event_loop()
            info = await loop.run_in_executor(None, self._download, url)

            if info:
                # Reset l'événement à chaque nouvelle piste
                self.track_end.clear()
                self.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(self.current_file_path)),
                                       after=lambda e: self.ctx.bot.loop.call_soon_threadsafe(self.track_end.set))
                await self.ctx.send(f'Lecture en cours : {info["title"]}')

                # Create and send the soundboard view here
                view = MusicButtonsView(self)
                await self.ctx.send("Contrôleur de lecture :", view=view)

                # Attendez que la piste se termine avant de continuer
                await self.track_end.wait()
            else:
                self.is_playing = False
                continue

        self.is_playing = False

    async def connect_to_voice_channel(self):
        if self.ctx.author.voice:
            self.voice_client = await self.ctx.author.voice.channel.connect()

    async def disconnect_from_voice_channel(self):
        if self.voice_client:
            await self.voice_client.disconnect(force=True)
            self.voice_client = None

    async def add_to_queue(self, url):
        if len(self.queue) < 100:
            self.queue.append(url)
        else:
            await self.ctx.send('La file d\'attente est pleine.')

        # Mettre à jour les informations de chaque titre ajouté
        added_titles = []
        for track_url in self.queue[-1::-1]:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                try:
                    info = ydl.extract_info(track_url, download=False)
                    track_title = info.get('title', 'Titre inconnu')
                    added_titles.append(track_title)
                except Exception:
                    added_titles.append('Titre inconnu')

        # Construire le message de file d'attente
        queue_message = "\n".join(f"{i + 1} - \"{title}\" a été mis en file d'attente." for i, title in enumerate(added_titles[::-1]))
        total_added = len(self.queue)

        # Mettre à jour le nombre total de titres ajoutés et envoyer le message de file d'attente
        if total_added > 0:
            await self.ctx.send(f"{queue_message}\nIl y a maintenant {total_added} titres en file d'attente.")

    def _download(self, url):
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                duration = info.get('duration', 0) / 60

                if duration > 30:
                    asyncio.run_coroutine_threadsafe(self.ctx.send('La vidéo est trop longue pour être lue.'), self.ctx.bot.loop)
                    return None

                info = ydl.extract_info(url, download=True)
                file_path = ydl.prepare_filename(info)
                file_path = file_path.rsplit(".", 1)[0] + ".mp3"
                self.current_file_path = file_path

                return info
        except Exception as e:
            asyncio.run_coroutine_threadsafe(self.ctx.send(f'Une erreur s\'est produite: {str(e)}'), self.ctx.bot.loop)
            return None

    async def pause_or_resume(self, action):
        if self.voice_client:
            if action == 'pause' and self.voice_client.is_playing():
                self.voice_client.pause()
                await self.ctx.send('Mise en pause de la lecture en cours.')
            elif action == 'resume' and self.voice_client.is_paused():
                self.voice_client.resume()
                await self.ctx.send('Reprise de la lecture en cours.')
        else:
            await self.ctx.send('Aucune lecture en cours.')

    async def stop_or_skip(self, action):
        if self.voice_client and self.voice_client.is_playing():
            self.voice_client.stop()
            message = 'Arrêt.' if action == 'stop' else 'Chanson passée.'
            await self.ctx.send(message)
            if action == 'stop':
                self.is_playing = False
        else:
            await self.ctx.send('Aucune lecture en cours.')
