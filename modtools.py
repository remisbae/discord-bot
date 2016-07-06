import discord
import asyncio

def has_msg(message):
    for role in message.author.roles:
        if role.permissions.manage_messages:
            return True
            break

def has_move(message):
    for role in message.author.roles:
        if role.permissions.move_members:
            return True
            break

async def purge(message, client):
    while True:
        await client.send_typing(message.channel)

        if not has_msg(message):
            await client.send_message(message.channel, 'You need the "Manage Messages" permission to call this command.')
            break

        parse = message.content.split()
        try:
            name = parse[1]
        except IndexError:
            await client.send_message(message.channel, 'No name specified')
            break

        user = discord.utils.find(lambda o: o.display_name.lower() == name, message.channel.server.members)

        def is_usr(message):
            return message.author == user

        try:
            param = int(parse[2])
        except IndexError:
            param = 100

        deleted = await client.purge_from(message.channel, limit=param, check=is_usr)

        await client.send_message(message.channel, 'Done deleting {0} messages by {1}.'.format(len(deleted),user.display_name))
        break

async def mvmembers(message, client):
    while True:
        await client.send_typing(message.channel)

        if not has_move(message):
            await client.send_message(message.channel, 'You need the "Move Members" permission to call this command.')
            break

        usr_error = 'Please provide users to move.'

        if '"' in message.content:
            parse = message.content.split('"')
            for i in range(0, len(parse)):
                parse[i] = parse[i].strip()
            cname = parse[1]
            if parse[2] != '':
                members = parse[2].split(';')
            else:
                await client.send_message(message.channel, usr_error)
                break
        else:
            parse = message.content.split()
            try:
                cname = parse[1]
            except IndexError:
                await client.send_message(message.channel, 'Please provide a name for the channel to move to.')
                break
            try:
                members = parse[2].split(';')
            except IndexError:
                await client.send_message(message.channel, usr_error)
                break

        try:
            channel = discord.utils.get(message.server.channels, name=cname, type=discord.ChannelType.voice)
            for member in members:
                user = discord.utils.find(lambda o: o.display_name.lower() == member.lower(), message.channel.server.members)
                await client.move_member(user, channel)
        except AttributeError:
            await client.send_message(message.channel, 'Channel not found')
            break

        await client.send_message(message.channel, 'Successfully moved users.')
        break