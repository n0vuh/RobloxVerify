# made by novuh.dev/github
# NEED HELP? -> https://github.com/n0vuh/RobloxVerify/blob/master/README.md
# NEED HELP? -> https://github.com/n0vuh/RobloxVerify/blob/master/README.md
# NEED HELP? -> https://github.com/n0vuh/RobloxVerify/blob/master/README.md

import discord, requests, time, random
from discord.ext import commands

BOT_TOKEN = "bot token here"
BOT_PREFIX = "!"
MAX_REQUESTS = 20
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=BOT_PREFIX, help_command=None, intents=intents)

@client.event
async def on_ready(): 
    print('Bot Online!')

@client.command()
async def verify(ctx):
    t = 0
    while True:
        await ctx.send(f'{ctx.message.author.mention}: Step 1/3 | Please enter your ROBLOX username.')
        robloxUsername = await client.wait_for('message', check=lambda message: message.author == ctx.message.author).content
        try:
            robloxId = requests.get(f'https://api.roblox.com/users/get-by-username?username={robloxUsername}').json()['Id']
            break
        except: await ctx.send(f'{ctx.message.author.mention}: Sorry! I was unable to retrieve your user ID!')
        
    privKey = ' '.join(random.choices([line.strip() for line in open('words.txt', 'r')], k=5))
    await ctx.send(f'{ctx.message.author.mention}: Step 2/3 | Please put the phrase `{privKey}` in your ROBLOX status. [https://i.imgur.com/qH6nvmZ.gif]')
    while True:
        if requests.get(f'https://users.roblox.com/v1/users/{robloxId}/status').json()['status'] == privKey: 
            await ctx.send(f'{ctx.message.author.mention}: Step 3/3 | Thank you for verifying!')
            break
        else:
            if t >= MAX_REQUESTS: 
                await ctx.send(f"{ctx.message.author.mention}: You did not verify in time, please try again.")
                break
            else:
                time.sleep(3);t+=1
    
    # -- YOUR CODE BELOW -- Note: you can call their username with "robloxUsername"
    
client.run(BOT_TOKEN)
