import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('Bot is Ready.')
	
@client.command(aliases=['소라고둥','Que'])
async def _소라고둥(ctx, * , question):
    responses = ['안돼.','안.돼.','당연하지.','확실해.','아마도.','그래.','나중에 다시 물어봐.','아직 때가 아냐.','말하기 싫어.','꿈도 꾸지마.','말도 안돼는 소리.','미쳤어?','싫어.']
    await ctx.send(f'뭐? {question} 라고? \n{random.choice(responses)}')
 
access_token = os.environ["BOT.TOKEN"]
client.run(access_token)
