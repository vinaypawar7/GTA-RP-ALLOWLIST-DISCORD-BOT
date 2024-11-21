# Roleplay Allowlist Bot By AGx

A Discord bot designed to manage allowlists for GTA RP (Roleplay) servers, integrating seamlessly with Discord to automate the approval process and streamline server management.

## Features
- Automates allowlist approvals for GTA RP servers.
- Integrates with Discord roles and channels.
- Customizable approval workflows.
- Supports advanced logging and notifications.

## Author
Developed by **agx** (Vinay Pawar).

Notes - selling of this bot is not allowed. share with proper credits.


## To Buy Custom Paid Discord Bots DM - @agx_v77 On Discord

# Installation Guide

A Discord bot designed to manage allowlists for GTA RP (Roleplay) servers, integrating seamlessly with Discord to automate the approval process and streamline server management.

---

## Installation Instructions

Follow these steps to manually set up and run the Discord bot:

1. **Download the Code**  
   - Go to the project’s GitHub repository or source.  
   - Click on the **Code** button and then **Download ZIP**.  
   - Extract the ZIP file to a desired folder on your system.

2. **Install Python**  
   - Ensure you have Python 3.8 or higher installed.  
   - Download Python from the [official website](https://www.python.org/downloads/).  
   - Follow the installation instructions and add Python to your system's PATH.

3. **Install Required Libraries**  
   - Navigate to the folder where you extracted the project files.  
   - Open a terminal/command prompt and run:  
     ```bash
     pip install -r requirements.txt
     ```

4. **Configure the Bot**  
   - Create a `.env` file in the root directory of the project.  
   - Add the following configuration to the `.env` file:  
     ```env
     DISCORD_BOT_TOKEN=your_discord_bot_token
     ALLOWLIST_CHANNEL_ID=your_channel_id
     ```
   - Replace `your_discord_bot_token` with the token of your Discord bot.  
   - Replace `your_channel_id` with the ID of the channel where allowlist commands will be managed.

5. **Run the Bot**  
   - Start the bot by running:  
     ```bash
     python bot.py
     ```

6. **Add the Bot to Your Discord Server**  
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).  
   - Copy your bot's **Client ID** and use it to generate an invite link:  
     ```url
     https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=8&scope=bot
     ```  
   - Paste the link into your browser and add the bot to your Discord server.

---

## Requirements

This project depends on the following Python libraries. Install them by running this commands in the cmd file one by one:

pip install discord.py
pip install python-dotenv
pip install aiohttp


