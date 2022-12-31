from discord.ext import commands
import discord

TOKEN = 'MTA1ODc0NDM0MjE0OTMzMzA5Mg.Gdox-g.jR-e6_a0gs2w323d_oAakYyvP0Q_-hm1w05sxI'
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    CHANNEL_ID = 570179814011437063
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('あけおめ！！！！')

client.run(TOKEN)