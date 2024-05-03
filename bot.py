"""
        [ Cyber Shield Discord Bot ]

    @author: Algorithm / Jeffery
    @since: 5/3/24
    @github: @AdvancedAlgorithm
"""
import discord

class Config:
    prefix = "-"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):

        data = message.content
        cmd = data
        args = []
        if not data.startswith(Config.prefix): return
        if " " in data:
            args = data.split(" ")
            cmd = args[0]

        if cmd == f"{Config.prefix}help":
            await message.channel.send("WORKING")
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTIzNjA0MzgxMDM3MTI3NjgzMA.GAaz1l.Rsavj8et4rgwllDlHzFUQrJxAFq-OG4qGOrwG0')