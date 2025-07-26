import nextcord
from nextcord.ext import commands
import config
import json

CONFIG_FILE = "data/alerts_config.json"

intents = nextcord.Intents.default()
intents.message_content = True  # REQUIRED for prefix commands

bot = commands.Bot(command_prefix="!", intents=intents)

def save_channel_id(channel_id: int):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"channel_id": channel_id}, f)

def load_channel_id() -> int | None:
    try:
        with open(CONFIG_FILE) as f:
            data = json.load(f)
            return data.get("channel_id")
    except (FileNotFoundError, json.JSONDecodeError):
        return None


@bot.command()
async def register(ctx):
    channel_id = ctx.channel.id
    save_channel_id(channel_id)
    print(f"Received !register from {ctx.author} in #{ctx.channel}")
    await ctx.send(f"✅ Registered this channel for alerts! (ID: {channel_id})")
    


@bot.event
async def on_ready():
    print("bot is live!")
    channel_id = load_channel_id()
    if channel_id:
        await send_message(channel_id, "✅ Bot is live and registered!")
    else:
        print("⚠️ No registered channel found.")


async def send_message(channel_id: int, message: str) -> None:
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(message)
    else:
        print(f"Channel with ID {channel_id} not found.")

bot.run(config.DISCORD_BOT_TOKEN)
