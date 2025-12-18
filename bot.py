import discord
from discord.ext import commands

import dotenv
import os
import logging
import asyncio

dotenv.load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

# -------------------
# File Handler (Log File)
# -------------------
file_handler = logging.FileHandler("log.log")
file_handler.setLevel(logging.INFO)
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

# -------------------
# Stream Handler (Terminal)
# -------------------
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents, help_command=None)

# -------------------
# Events
# -------------------
@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user} (ID: {bot.user.id})')
    logging.info('------')
    try:
        synced = await bot.tree.sync()
        logging.info(f'Synced {len(synced)} command(s)')
    except Exception as e:
        logging.error(f'Error syncing commands: {e}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"❌ `{ctx.invoked_with}` existiert nicht.")
        return
    
    logging.error(f'Error in command {ctx.command}: {error}')
    await ctx.send(f'An error occurred: {str(error)}')
    return

async def load_cogs():
    # for cog in ['cogs.words']:
    #     try:
    #         await bot.load_extension(cog)
    #         logging.info(f'Loaded cog: {cog}')
    #     except Exception as e:
    #         logging.error(f'Failed to load cog {cog}: {e}')
    # for cog in ['cogs.help']:
    #     try:
    #         await bot.load_extension(cog)
    #         logging.info(f'Loaded cog: {cog}')
    #     except Exception as e:
    #         logging.error(f'Failed to load cog {cog}: {e}')
    try:
        await bot.load_extension('cogs.words')
        logging.info('Loaded cog: cogs.words')
        await bot.load_extension('cogs.help')
        logging.info('Loaded cog: cogs.help')
    except Exception as e:
        logging.error(f'Failed to load cogs: {e}')

async def main():
    await load_cogs()
    await bot.start(TOKEN)

asyncio.run(main())