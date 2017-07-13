# discord-bot
A bot for [Discord](https://discordapp.com/) written in Python with [discord.py](https://github.com/Rapptz/discord.py)!

## Functionality
As a TeamSpeak user, I can not imagine using something that doesn't let users create temporary Voice Channels. To do that in Discord, I not only have to trust my users, but also give them permissions for stuff they don't need (ie, permissions to edit ALL channels, as well as text channels).
As such, the main features of my bot are:
* Let's users create their own Voice channels and let's them set a client limit, or even make them whitelist-only, so they get to choose who joins their channel.
* Let's users delete only their own channels
* Let's users edit their channel's Name, User limit, or whitelist other users if it's a private channel.
* Saves a database of user-created channels locally, so even if the bot restarts it will still remember the owner of each channel etc.
* Tells you where it's High Noon at. Cool little feature I guess.
* Gives everyone with the move_members permission the ability to call a command to mass-move members to other channels.
* Gives everyone with the manage_messages permission the ability to mass-delete a user's messages
* Gives the ability to mark a server as a "WoW" Discord so WoW-related features are enabled.
  * When you add a server as a WoW Discord then the bot creates all the necesesary roles for every class (if they don't exist) without colors.
  * WoW features include:
    * Setting yourself to a class.

### Add to Discord
~~To add my bot to discord simply use the following [link](https://discordapp.com/oauth2/authorize?client_id=190034775170351104&scope=bot&permissions=0x0000010)
(This only grants Manage Channels which is the very basic feature of the bot, you might wanna give the Bot role "Manage Roles" and "Manage Messages" as well for other features.)~~
My bot is Offline since May 2017 since I can't really host it anymore, so you will have to host the bot yourself.

### Hosting The Bot
To host the bot follow these steps:
* Get Python3 from [here](https://www.python.org/downloads/)
* Download this directory as .zip and extract it somewhere.
* Open up a command prompt or terminal and change the directory to the one you extracted it in.
* Run `pip install -r requirements.txt`
* Make a Discord Bot Account [here](https://discordapp.com/developers/applications/me/create)
* Once you're done go to the bot's profile from [here](https://discordapp.com/developers/applications/me) 
  * From here you want to keep the `Bot ID` and also click on `click to reveal` next to `Token` and save that as well.
* Edit bot.py with a text editor of your choice and on the last line, replace `token here` in `'token here'` with the token from the discord bot account (make sure that the token is inside the quotations still)
* Run bot.py

To invite your own instance to your server you need to be logged in to browser discord and then in this link `https://discordapp.com/oauth2/authorize?client_id=ID_HERE&scope=bot&permissions=0x0000010` replace `ID_HERE` with the Bot ID from the discord bot account, then visit that link.
