import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# Load .env file containing DISCORD_TOKEN
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set up bot with default intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# On ready: sync commands & set status
@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(
        activity=discord.Game(name="made by reverse || v.1.0")
    )
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

# /start command: Full instructions
@bot.tree.command(name="start", description="How to get the Active Developer Badge + Hosting Help")
async def start(interaction: discord.Interaction):
    guide = (
        "**🏅 How to Get the Discord Active Developer Badge**\n\n"
        "To qualify, Discord checks if:\n"
        "• You registered a bot\n"
        "• It has at least one **slash command**\n"
        "• That command was used within the last 30 days\n\n"
        "**✅ What to do:**\n"
        "1. Go to the [Developer Portal](https://discord.com/developers/applications)\n"
        "2. Create an application and add a bot\n"
        "3. Copy the token and paste it into a `.env` file like:\n"
        "```\nDISCORD_TOKEN=your-token-here\n```\n"
        "4. Clone the source code (see `/source`)\n"
        "5. Run this in your terminal:\n"
        "```bash\npip install -U discord.py python-dotenv\npython bot.py\n```\n"
        "6. Add the bot to your server and use `/start`\n"
        "7. Wait ~24 hours and check: [Badge Page](https://discord.com/developers/active-developer)\n\n"
        "💡 Tip: You can host the bot free on **Replit**, **Railway**, or **Render**."
    )
    await interaction.response.send_message(guide, ephemeral=True)

# /source command: Send GitHub link
@bot.tree.command(name="source", description="Get the source code link to host your own bot")
async def source(interaction: discord.Interaction):
    await interaction.response.send_message(
        "📂 Source code available at: <https://github.com/YOUR_USERNAME/YOUR_REPO>",
        ephemeral=True
    )

# Run the bot
bot.run(TOKEN)
