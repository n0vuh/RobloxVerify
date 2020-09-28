# made by novuh.dev/github

import discord, requests, time, random
from discord.ext import commands

BOT_TOKEN = "bot token here"
BOT_PREFIX = "!"

client = commands.Bot(command_prefix=BOT_PREFIX, help_command=None)

@client.event
async def on_ready(): print('Bot Online. - novuh.dev')

@client.command()
async def verify(ctx):
    await ctx.send(f'{ctx.message.author.mention}: Step 1/3 | Please enter your ROBLOX username.')
    msg = await client.wait_for('message', check=lambda message: message.author == ctx.message.author)
    robloxUsername = msg.content
    robloxId = requests.get(f'https://api.roblox.com/users/get-by-username?username={msg.content}').json()['Id']
    privKey = ' '.join(random.choices([line.strip() for line in open('words.txt', 'r')], k=5))
    await ctx.send(f'{ctx.message.author.mention}: Step 2/3 | Please put the phrase `{privKey}` in your ROBLOX status. [https://i.imgur.com/qH6nvmZ.gif]')
    while True:
        if requests.get(f'https://users.roblox.com/v1/users/{robloxId}/status').json()['status'] == privKey: break
        else: time.sleep(3)
    await ctx.send(f'{ctx.message.author.mention}: Step 3/3 | Thank you for verifying!')
    # AFTER VERIFY TASKS HERE, YOU CAN CALL THEIR USERNAME WITH robloxUsername

client.run(BOT_TOKEN)