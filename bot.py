"""
        [ Cyber Shield Discord Bot ]

    @author: Algorithm / Jeffery
    @since: 5/3/24
    @github: @AdvancedAlgorithm
"""
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTIzNjA0MzgxMDM3MTI3NjgzMA.GfhIz4.xziGAjbc317Mi7eK5e9olpzAuOX3Sgmaq2Lwt4')