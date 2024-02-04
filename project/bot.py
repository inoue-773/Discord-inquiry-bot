import discord
from discord.ext import commands
from pymongo import MongoClient

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Connect to MongoDB
mongo_client = MongoClient("your-mongodb-link")
db = mongo_client["newmessagelog"]
collection = db["messages"]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages sent by the bot itself
    
    if message.channel.id == your-discord-channel-id:
        await process_message(message)
    
    await bot.process_commands(message)

async def process_message(message):
    # Check if the message content is not an empty string
    if message.content.strip():  # strip() removes leading and trailing whitespaces
        # Check if the message content is already in the database
        existing_message = collection.find_one({"content": message.content})

        if existing_message:
            await message.reply("The data has already been registered to the database.")
        else:
            # If not, add the non-empty message content to the database
            collection.insert_one({"content": message.content})
            await message.reply("The data has successfully been registered to the database.")

bot.run('your-discord-token')  # Replace YOUR_BOT_TOKEN with the actual bot token
