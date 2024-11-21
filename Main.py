import discord
from discord.ext import commands
from datetime import datetime

TOKEN = 'abc'
RESPONSE_CHANNEL_ID = abv
ROLE_ID = abc
LOG_CHANNEL_ID = abc

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

applications = {}

async def ask_questions(ctx, user):
    def check(m):
        return m.author == user and isinstance(m.channel, discord.DMChannel)
    
    await user.send("📝 **Question 1:** What is your character's name?")
    character_name = await bot.wait_for('message', check=check)
    
    await user.send("📝 **Question 2:** What is your character's backstory? (Type 'No' if you don't have one)")
    backstory = await bot.wait_for('message', check=check)
    
    applications[user.id] = {
        'character_name': character_name.content,
        'backstory': backstory.content or "No backstory provided."
    }

    await user.send("✅ **Your application has been submitted successfully!**\n\nModerators will review it shortly.")

    role = ctx.guild.get_role(ROLE_ID)
    if role:
        await user.add_roles(role)
        await user.send(f"You have been given the **{role.name}** role!")
    else:
        await user.send("❌ I couldn't assign the role. Please contact a moderator.")
        print(f"Role with ID {ROLE_ID} not found.")

    response_channel = bot.get_channel(RESPONSE_CHANNEL_ID)
    if response_channel:
        embed = discord.Embed(
            title="Application Response",
            description=f"🎉 Congratulations {user.mention}! Your application has been accepted!",
            color=discord.Color.purple()
        )
        embed.set_image(url="https://media.discordapp.net/attachments/1295675759242776588/1302948350903193612/Black_Red_Modern_Miracle_Moon_Premiere_Movie_Ticket_1.png?format=webp&quality=lossless&width=1440&height=465")
        await response_channel.send(content=user.mention, embed=embed)
    else:
        print(f"Response channel with ID {RESPONSE_CHANNEL_ID} not found.")
    
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = (
            f"📅 **Application Log**\n"
            f"**User:** {user.mention} ({user.name})\n"
            f"**Time:** {current_time}\n"
            f"**Character Name:** {character_name.content}\n"
            f"**Backstory:** {backstory.content}\n"
        )
        await log_channel.send(log_message)
    else:
        print(f"Log channel with ID {LOG_CHANNEL_ID} not found.")

@bot.command()
async def apply(ctx):
    user = ctx.author
    try:
        await user.send("Welcome to the allowlist application! Please answer the following questions:")
        await ask_questions(ctx, user)
    except discord.Forbidden:
        await ctx.send(f"{user.mention}, I couldn't DM you. Please enable DMs from server members.")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run(TOKEN)
