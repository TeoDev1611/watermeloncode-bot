from os import getenv
from discord.ext import commands
from dotenv import load_dotenv

# Load enviroments from .env file
load_dotenv()

# Create bot client
prefix = getenv("BOT_PREFIX")
description = getenv("BOT_DESCRIPTION")
client = commands.Bot(command_prefix=prefix, description=description)


# On bot ready
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


# Load the extensions or cogs
cogs = ["cogs.ping","cogs.joke"]
for i in cogs:
    try:
        client.load_extension(i)
    except Exception as err:
        print(f"An error has occurred {err}")

# Run the bot
if __name__ == "__main__":
    client.run(getenv("BOT_TOKEN"))
