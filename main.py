import discord

TOKEN = "573672594947964969"

client = discord.Client()

@client.event
async def on_ready():
    print("BotBot is prepared.")
    await client.change_presence(game=discord.Game(name="Being the best bot"))
    
@client.event
async def on_message(message):
    #disable reply to self
    if message.author == client.user:
        return
    if message.content.startswith("%hello"):
        msg = "Hello {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

client.run(TOKEN)
