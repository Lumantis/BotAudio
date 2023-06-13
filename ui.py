from discord import ui, ButtonStyle

class PauseResumeButton(ui.Button['PauseResumeButton']):
    def __init__(self):
        super().__init__(style=ButtonStyle.secondary, label="Pause/Resume", custom_id="pause_resume")

    async def callback(self, interaction):
        player = players.get(interaction.guild.id)
        if player:
            if player.voice_client.is_playing():
                await interaction.response.send_message('Mise en pause.', ephemeral=True)
                await player.pause_or_resume('pause')
            elif player.voice_client.is_paused():
                await interaction.response.send_message('Reprise.', ephemeral=True)
                await player.pause_or_resume('resume')

class SkipButton(ui.Button['SkipButton']):
    def __init__(self):
        super().__init__(style=ButtonStyle.primary, label="Passer", custom_id="skip")

    async def callback(self, interaction):
        player = players.get(interaction.guild.id)
        if player:
            await player.stop_or_skip('skip')
        await interaction.response.send_message('Skip.', ephemeral=True)

class MusicButtonsView(ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(PauseResumeButton())
        self.add_item(SkipButton())
