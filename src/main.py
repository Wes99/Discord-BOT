from http import client
from discord.ext import commands
import discord
import random


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 294070978269544450  # Change to your discord id 


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

@bot.command()
async def d6(ctx):
    await ctx.send(str(random.randint(1,6)))

@bot.event
async def on_message(msg):
    if (msg.content == "Salut tout le monde"):
        await msg.channel.send("Salut tout seul")
        await msg.channel.send(msg.author.mention)
    await bot.process_commands(msg)

@bot.command()
async def admin(msg):
    role = discord.utils.get(intents.role, name="Admin")
    await bot.process_commands(msg)

token = ""
bot.run(token)  # Starts the bot