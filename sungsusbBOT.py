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
    if message.author.bot:
        return None

    id = message.author.id
    channel = message.channel



    if message.content.startswith("+도움말"):
        await message.channel.send(message.author.mention+"```css\n성은봇 사용법\n#1. '성은아'를 붙어 봇을 사용한다\n#2. '성은아 안녕'등 명령어들이 있다(점점 추가 함)\n#3. '+문의'로 문의\n'+관리자 [정보/소환]으로 관리자의 정보를 확인할 수 있다'\n...```")
        
    elif message.content.startswith("+문의"):
        atr = message.guild.get_member(653172394499768322)
        atr1 = message.guild.get_member(336425833403252746)
        msg = message.content[4:]
        if msg == "":
            await message.channel.send(message.author.mention + "```css\n문의 내용을 적어주세요.(+문의 [내용])\n```")
        else:
            await atr1.send(message.author.mention + " : " + msg)
            await atr.send(message.author.mention + " : " + msg)
            await message.channel.send(message.author.mention + "```css\n정상적으로 문의를 보냈습니다.\n```")

    elif message.content.startswith("+관리자"):
        atr = message.guild.get_member(336425833403252746)
        msg = message.content[5:]
        if msg == "소환":
            await atr.send(message.author.mention + "님이 영옥이방에서 당신을 부릅니다")
            # await atr.send(message.author.mention + "님이 영옥이방에서 당신을 부릅니다" + message.author.mention(id="336425833403252746"))
            await message.channel.send(message.author.mention + "```css\n정상적으로 메세지를 보냈습니다.\n(다소 시간이 걸릴 수 있음.)\n```")
        elif msg == "정보":
            await message.channel.send(message.author.mention + "```css\n이름 : 김성진\n나이 : 16\n학교 : 동백중학교\n관리자가 이전될때마다 변경됩니다.\n[추가중...]\n```")
        else:
            await message.channel.send(message.author.mention + "```css\n내용을 적어주세요.(+관리자 [정보/소환])\n```")



    elif message.content.startswith("성은아 안녕"):
        await message.channel.send("ㅎㅇ")
    elif message.content.startswith("성은아 뭐해"):
        await message.channel.send("영옥이방에서 노동중 ㅎ")
    elif message.content.startswith("성은아 엄마"):
        await message.channel.send("? 선넘네")
    elif message.content.startswith("성은아 바보"):
        await message.channel.send("지는 ㅋ")
    elif message.content.startswith("성은아 병신"):
        await message.channel.send("지는 ㅋ")
    elif message.content.startswith("성은아 ㅂㅅ"):
        await message.channel.send("지는 ㅋ")
    elif message.content.startswith("성은아 시발"):
        await message.channel.send("ㅇ")
    elif message.content.startswith("성은아 ㅅㅂ"):
        await message.channel.send("ㅇ")
    elif message.content.startswith("성은아 씨발"):
        await message.channel.send("ㅇ")
    elif message.content.startswith("성은아 넌 누구야"):
        await message.channel.send("영옥이방의 노예")
    elif message.content.startswith("성은아 잘가"):
        await message.channel.send("ㅂㅇ")
    elif message.content.startswith("성은아"):
        await message.channel.send("?")
    elif message.content.startswith("김성은"):
        await message.channel.send("왜 불러")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
