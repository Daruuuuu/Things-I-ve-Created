import discord
import random

keywords = ["league", "League","LEAGUE", "Nertz" "nertz" "NERTZ"]


TOKEN = 'OTY5MDIwOTUyMTU3NTE5OTEy.YmnVFg.1O9TiSGYNExsiAAJsAZgEqtM27A'

client = discord.Client()

#Lets user know when logged in.
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')


    if message.author == client.user:
        return
#replies with shitty game bro if certain words are input.
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            for j in range(1):
                await message.delete()
                await message.channel.send("shitty game bro")
    
#bot responds to these
    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return
    
    #command that can be used anywhere
    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return
        



client.run(TOKEN)