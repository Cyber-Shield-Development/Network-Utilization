"""
        [ Cyber Shield Discord Bot ]

    @author: Algorithm / Jeffery
    @since: 5/3/24
    @github: @AdvancedAlgorithm
"""
import discord
from discord.ext import commands  
class Config:
    prefix = "&"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        msgdata = message.content
        cmd = msgdata
        args = []
        if not msgdata.startswith(Config.prefix): return
        if " " in msgdata:
            args = msgdata.split(" ")
            cmd = args[0]

        if cmd == f"{Config.prefix}status":
            await message.channel.send("WORKING")
        if cmd == f"{Config.prefix}ban" or cmd == f"{Config.prefix}Ban":
            if message.author.guild_permissions.ban_members:
                if len(message.mentions) == 0:
                    await message.channel.send("Please Mention the specified member.")
                else:
                    member  = message.mentions[0]
                    await member.ban(member)




    


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents )
client.run('MTIzNjA0MzgxMDM3MTI3NjgzMA.GOZKXC.jIE59Q0uyzQMWtGGPJeeHqVOeDpTNLp098Qa-A')