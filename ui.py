import discord
from discord import ButtonStyle, Interaction
from discord.ext import commands
from discord.ui import View, Button
from discord.errors import HTTPException

class PauseResumeButton(Button['PauseResumeButton']):
    def __init__(self, player):
        super().__init__(style=ButtonStyle.secondary, emoji="⏸️", label="Pause/Lecture", custom_id="pause_resume")
        self.player = player

    async def callback(self, interaction: Interaction):
        if self.player and self.player.voice_client:
            if self.player.voice_client.is_playing():
                try:
                    await interaction.response.send_message('Mise en pause de la musique en cours.', ephemeral=True)
                    await self.player.pause_or_resume('pause')
                except HTTPException:
                    await interaction.response.send_message('Impossible de mettre la musique en pause.', ephemeral=True)
            elif self.player.voice_client.is_paused():
                try:
                    await interaction.response.send_message('Reprise de la musique en cours.', ephemeral=True)
                    await self.player.pause_or_resume('resume')
                except HTTPException:
                    await interaction.response.send_message('Impossible de reprendre la musique.', ephemeral=True)
        else:
            await interaction.response.send_message('Je ne suis pas connecté à un canal vocal.', ephemeral=True)


class SkipButton(Button['SkipButton']):
    def __init__(self, player):
        super().__init__(style=ButtonStyle.primary, emoji="⏭️", label="Passer", custom_id="skip")
        self.player = player

    async def callback(self, interaction: Interaction):
        if self.player and self.player.voice_client:
            try:
                await self.player.stop_or_skip('skip')
                await interaction.response.send_message('La musique a bien été passée.', ephemeral=True)
            except HTTPException:
                await interaction.response.send_message('Impossible de passer la musique.', ephemeral=True)
        else:
            await interaction.response.send_message('Je ne suis pas connecté à un canal vocal.', ephemeral=True)


class MusicButtonsView(View):
    def __init__(self, player):
        super().__init__()
        self.add_item(PauseResumeButton(player))
        self.add_item(SkipButton(player))
