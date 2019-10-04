#-*- coding: utf-8 -*-
import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
channel = client.get_channel("channel id")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('일하는척'))
    print('Bot is ready.')


@client.command(aliases=['주사위'])
async def _rollingdice(ctx, mnnum: int, mxnum: int):
    if mnnum >= mxnum:
        embed = discord.Embed(title="Error",description="최솟값이 최댓값보다 크거나 같습니다!",color=0xff0000)
        await ctx.send(embed=embed)
    else:
        roll = randint(mnnum,mxnum)
        embed = discord.Embed(title="주사위 결과",description="{mnnum}~{mxnum}의 주사위결과 {roll}이 나왔습니다.",color=0x00ff00)
        await ctx.send(embed=embed)


@client.command(aliases=['소라고둥'])
async def _sora(ctx, *, question):
    responses = ['안돼.',
                 '안.돼.',
                 '당연하지.',
                 '확실해.',
                 '아마도.',
                 '그래.',
                 '나중에 다시 물어봐.',
                 '아직 말해줄 때가 아냐.',
                 '말하기 싫어.',
                 '꿈도 꾸지마.',
                 '말도 안돼는 소리.',
                 '미쳤어?',
                 '싫어.']
    await ctx.send(f'뭐? {question} 라고? \n{random.choice(responses)}')

@client.command(aliases=['유니온'])
async def _Union(ctx, level: int):
    if level <= 0:
        embed = discord.Embed(title="Error",description="0레벨이 어딨노 시발련ㄴ아", color = 0xff0000)
        await ctx.send(embed=embed)

    if level > 0 and level < 30:
        embed = discord.Embed(title="유니온 1~30레벨",description="머쉬맘,블루머쉬맘", color = 0x00ff00)
        await ctx.send(embed=embed)
        
    if level >= 30 and level < 35:
        embed = discord.Embed(title="유니온 30~35레벨",description="골드비치 퀘스트 진행", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 35 and level < 42:
        embed = discord.Embed(title="유니온 35~42레벨",description="와일드보어의 땅\n사냥중 룬을 깠다면 46레벨까지 와일드보어의 땅에서 진행", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 42 and level < 46:
        embed = discord.Embed(
            title = '유니온 42~46레벨',
            description = '제1군영',
            colour = discord.Colour.green()
            )        
        await ctx.send(embed=embed) 
            
    if level >= 46 and level < 51:
        embed = discord.Embed(title="유니온 46~51레벨",description="조용한습지 카파드레이크", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 51 and level < 59: 
        embed = discord.Embed(title="유니온 51~59레벨",description="하늘계단1\n하늘계단에서의 사냥능력이 좋지않은직업(클레릭등)이라면 조용한습지", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 59 and level < 61:
        embed = discord.Embed(title="유니온 59~61레벨",description="경뿌,룬을 받은뒤 이지자쿰", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 61 and level < 70:
        embed = discord.Embed(title="유니온 61~70레벨",description="얼음골짜기2", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 70 and level < 75:
        embed = discord.Embed(title="유니온 70~75레벨",description="사헬지대2", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 75 and level < 80:
        embed = discord.Embed(title="유니온 75~80레벨",description="관계자외 출입금지", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 80 and level < 90:
        embed = discord.Embed(title="유니온 80~90레벨",description="엘린숲 이끼나무숲 오솔길\n텔마원킬 법사류나 스커같은 일자맵 사냥효율이 좋은직업이나 여기서의 사냥이 좋지않다면 관계자외 출입금지", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 90 and level < 110:
        embed = discord.Embed(title="유니온 90~110레벨",description="하늘둥지2", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 110 and level < 120:
        embed = discord.Embed(title="유니온 110~120레벨",description="사라진 시간 버닝10단계 채널(잊혀진 시간의길3 히든스트리트)", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 120 and level < 125:
        embed = discord.Embed(title="유니온 120~125레벨",description="폐광2 버닝10단계 채널", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 125 and level < 140:
        embed = discord.Embed(title="유니온 125~140레벨",description="시련의동굴3\n불독등의 반감속성직업이라면 시련의동굴1", color = 0x00ff00)
        await ctx.send(embed=embed)

    if level >= 140:
        embed = discord.Embed(title="Error",description="140넘었으면 알아서 좀 해", color = 0xff0000)
        await ctx.send(embed=embed)

@client.command()
async def 웃음벨(ctx):
    imglink = ['https://cdn.discordapp.com/attachments/629555651689054244/629571400327495710/i13124364945.gif',
               'https://cdn.discordapp.com/attachments/629555651689054244/629571983637741570/i13539237870.gif',
               'https://cdn.discordapp.com/attachments/629555651689054244/629572123832090624/i15934695138.gif',
               'https://cdn.discordapp.com/attachments/629555651689054244/629572252148695040/i14616872306.gif',
               'https://cdn.discordapp.com/attachments/598167258832830467/629572417496547328/i15748583659.gif',
               'https://cdn.discordapp.com/attachments/598167258832830467/629572534333079562/i14345778726.gif',
               'https://cdn.discordapp.com/attachments/598167258832830467/629572684493094935/i15424464768.gif',
               'https://cdn.discordapp.com/attachments/598167258832830467/629572800323125268/i14433790812.gif',
               'https://cdn.discordapp.com/attachments/598167258832830467/629572917214314498/i14763356644.gif',
               'https://cdn.discordapp.com/attachments/598167258832830467/629573061699436544/i14400997593.gif',
               'https://cdn.discordapp.com/attachments/629555651689054244/629567555719135232/maplestory-20191004-153613-000.gif',
               'https://cdn.discordapp.com/attachments/629555651689054244/629567571867336704/maplestory-20191004-153604-000.gif',
               'https://cdn.discordapp.com/attachments/629555651689054244/629569545731964928/Honeycam_2019-09-29_23-01-05.gif',
               'https://cdn.discordapp.com/attachments/629555651689054244/629567627626545162/maplestory-20191004-153215-000.gif',
               'https://cdn.discordapp.com/attachments/629555651689054244/629567643195539466/maplestory-20191004-153041-000.gif',
               'https://cdn.discordapp.com/attachments/629555651689054244/629567669259075584/maplestory-20191004-152833-000.gif',
               'https://cdn.discordapp.com/attachments/629555651689054244/629573808319103006/Honeycam_2019-10-04_15-53-31.gif',
               'https://cdn.discordapp.com/attachments/629555651689054244/629569549150191626/Honeycam_2019-10-04_15-44-00.gif',
               'https://cdn.discordapp.com/attachments/629555651689054244/629569548076449802/Honeycam_2019-10-04_15-43-36.gif',
               'https://cdn.discordapp.com/attachments/598167258832830467/629625292327092225/i14013796794.gif',
               'https://cdn.discordapp.com/attachments/598167258832830467/629625411797778432/i15715196150.gif']
    chosen_image = random.choice(imglink)
    embed = discord.Embed()
    embed.set_image(url=chosen_image)
    await ctx.send(embed=embed)

access_token = os.environ["BOT.TOKEN"]
client.run(access_token)
