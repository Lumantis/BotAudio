from discord import ui, ButtonStyle

class PauseResumeButton(ui.Button['PauseResumeButton']):
    def __init__(self, player):
        super().__init__(style=ButtonStyle.secondary, label="Pause/Lecture", custom_id="pause_resume")
        self.player = player

    async def callback(self, interaction):
        if self.player and self.player.voice_client:
            if self.player.voice_client.is_playing():
                await interaction.response.send_message('Mise en pause de la musique en cours.', ephemeral=True)
                await self.player.pause_or_resume('pause')
            elif self.player.voice_client.is_paused():
                await interaction.response.send_message('Reprise de la musique en cours.', ephemeral=True)
                await self.player.pause_or_resume('resume')


class SkipButton(ui.Button['SkipButton']):
    def __init__(self, player):
        super().__init__(style=ButtonStyle.primary, label="Passer", custom_id="skip")
        self.player = player

    async def callback(self, interaction):
        if self.player and self.player.voice_client:
            await self.player.stop_or_skip('skip')
        await interaction.response.send_message('La musique a bien été passée.', ephemeral=True)

class MusicButtonsView(ui.View):
    def __init__(self, player):
        super().__init__()
        self.add_item(PauseResumeButton(player))
        self.add_item(SkipButton(player))
