import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("완료")
    game = discord.Game("'+도움말'로 명령어 확인")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("+도움말"):
        await message.channel.send("```css\n성섭봇 사용법\n#1. '성섭아'를 붙어 봇을 사용한다\n#2. '성섭아 안녕'등 명령어들이 있다(점점 추가 함)\n#3. '+문의'로 문의\n...```")
    elif message.content.startswith("+문의"):
        atr = message.guild.get_member(653172394499768322)
        atr1 = message.guild.get_member(336425833403252746)
        msg = message.content[4:]
        await atr1.send(message.author.mention + " : " + msg)
        await atr.send(message.author.mention + " : " + msg)
        await message.channel.send(message.author.mention + " 정상적으로 문의를 보냈습니다.")
    elif message.content.startswith("성섭아 안녕"):
        await message.channel.send("ㅎㅇ")
    elif message.content.startswith("성섭아 뭐해"):
        await message.channel.send("영옥이방에서 노동중 ㅎ")
    elif message.content.startswith("성섭아 엄마"):
        await message.channel.send("? 선넘네")
    elif message.content.startswith("성섭아 바보"):
        await message.channel.send("지는 ㅋ")
    elif message.content.startswith("성섭아 병신"):
        await message.channel.send("지는 ㅋ")
    elif message.content.startswith("성섭아 ㅂㅅ"):
        await message.channel.send("지는 ㅋ")
    elif message.content.startswith("성섭아 시발"):
        await message.channel.send("ㅇ")
    elif message.content.startswith("성섭아 ㅅㅂ"):
        await message.channel.send("ㅇ")
    elif message.content.startswith("성섭아 씨발"):
        await message.channel.send("ㅇ")
    elif message.content.startswith("성섭아 넌 누구야"):
        await message.channel.send("영옥이방의 노예")
    elif message.content.startswith("성섭아"):
        await message.channel.send("?")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
















