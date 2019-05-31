import discord

import os
import datetime
import urllib.request
import random
import bs4


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(activity=discord.Game(name="말하는 쿠키봇"))



@client.event
async def on_message(message):
    if message.content.startswith('!롤각'):
        randomNum = random.randrange(1, 3)
        if randomNum == 1:
            await message.channel.send(
                embed=discord.Embed(description="롤각 가즈아~ (* >ω<) (＞Д＜)ゝ", colour=discord.Colour.green()))
            return
        else:
            await message.channel.send(
                embed=discord.Embed(description="응 오늘은아니야~ ಥ_ಥ (╥_╥)", colour=discord.Colour.green()))
            return

    if message.content.startswith('!실검') :
        url = "https://www.naver.com/"
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
        realTimeSerach3 = realTimeSerach2.find_all('li')

        embed = discord.Embed(
            title='네이버 실시간 검색순위',
            description='1위~10위',
            colour=discord.Colour.green()
        )
        for i in range(0, 10):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query=' + realTimeSerach
            print(realTimeSerach)
            embed.add_field(name=str(i + 1) + '위', value='\n' + '[%s](<%s>)' % (realTimeSerach, realURL),
                            inline=False)  # [텍스트](<링크>) 형식으로 적으면 텍스트 하이퍼링크 만들어집니다

        await message.channel.send( embed=embed)

    if message.content.startswith("!명령어"):
        embed = discord.Embed(
            title='(✪㉨✪) (⌬̀⌄⌬́) （๑✧∀✧๑）٩(●ᴗ●)۶',
            description='-쿠키봇의 명령어\n\n ',
            colour=discord.Colour.blue()
        )
        dtime = datetime.datetime.now()
        embed.add_field(name='!롤 아이디', value='롤op.gg 전적검색 결과를 보여줍니다 참고- 언랭은 정보따위 제공안합니다.', inline=True)
        embed.add_field(name='!핑', value='지연시간확인. ', inline=False)
        embed.add_field(name='!투표 제목/내용/내용...', value='투표함을 만듭니다. 이모지를 클릭하여 투표를 진행합니다.', inline=False)
        embed.add_field(name='!실검', value='네이버 실시간 검색순위를 1위부터 20위까지 보여줍니다.', inline=False)
        embed.set_footer(text=str(dtime.year) + "년 " + str(dtime.month) + "월 " + str(dtime.day) + "일 " + str(
            dtime.hour) + "시 " + str(dtime.minute) + "분")
        await message.channel.send(embed=embed)

    if message.content.startswith("!투표"):

        vote = message.content[4:].split("/")

        await message.channel.send("✉투표 - "+vote[0])
        for i in range(1,len(vote)):
            choose= await  message.channel.send("```"+vote[i]+"```")
            await choose.add_reaction('👍')

    if message.content.startswith("!핑"):
        ping = '%.2f' % (1000 * (client.latency ))
        await  message.channel.send(ping )

    if message.content.startswith("!롤"):
        learn = message.content[3:].split(" ")
        print(learn[0])
        location = learn[0]
        if len(learn) > 1:
            loc = ""
            for l in range(0, len(learn), 1):
                loc += learn[l]
            location=loc
        enc_location = urllib.parse.quote(location)
        print(enc_location)
        url = "http://www.op.gg/summoner/userName=" + enc_location
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        id1 = bsObj.find("div", {"class": "Profile"})

        if id1 is None:
            await message.channel.send(embed=discord.Embed(description="입력하신 아이디의 정보가없습니다",colour=discord.Colour.green()))
            return
        id2 = id1.find("div", {"class": "Information"})
        id3 = id2.find("span", {"class": "Name"})
        id4 = id3.text

        imaget1 = bsObj.find("div", {"class": "SummonerRatingMedium"})
        imaget2 = imaget1.find("img",{"class": "Image"})
        imaget3 = imaget2.get('src')
        imagetCut=imaget3.split("/")
        imageThumbnail=imagetCut[len(imagetCut) - 1]

        print(imageThumbnail)
        imagec1 = bsObj.find("div", {"class": "ProfileIcon"})
        imagec2 = imagec1.find("img")
        imagec3 = imagec2.get('src')
        imagecCut = imagec3.split("/")
        imageIcon = imagecCut[len(imagecCut) - 1]

        rank1 = bsObj.find("div", {"class": "TierRankInfo"})
        rank2 = rank1.find("div", {"class": "TierRank"})
        rank4 = rank2.text  # 티어표시 (브론즈1,2,3,4,5 등등)
        if rank4=='':
            rank4 = rank1.find("div", {"class": "TierRank unranked"}).text
        print(rank4)
        if rank4.strip() != 'Unranked':
            jumsu1 = rank1.find("div", {"class": "TierInfo"})
            jumsu2 = jumsu1.find("span", {"class": "LeaguePoints"})
            jumsu3 = jumsu2.text
            jumsu4 = jumsu3.strip()  # 점수표시 (11LP등등)
            print(jumsu4)

            winlose1 = jumsu1.find("span", {"class": "WinLose"})
            winlose2 = winlose1.find("span", {"class": "wins"})
            winlose2_1 = winlose1.find("span", {"class": "losses"})
            winlose2_2 = winlose1.find("span", {"class": "winratio"})

            winlose2txt = winlose2.text
            winlose2_1txt = winlose2_1.text
            winlose2_2txt = winlose2_2.text  # 승,패,승률 나타냄  200W 150L Win Ratio 55% 등등

            print(winlose2txt + " " + winlose2_1txt + " " + winlose2_2txt)

        channel = message.channel
        embed = discord.Embed(
            title=id4+'님의 롤 정보',
            description='롤 정보입니다.',

            colour=discord.Colour.red()
        )

        embed.set_thumbnail(url="http://opgg-static.akamaized.net/images/medals/"+imageThumbnail)
        embed.set_image(url="http://opgg-static.akamaized.net/images/profile_icons/"+imageIcon )
        if rank4.strip() == 'Unranked':
            embed.add_field(name='당신의 티어', value=rank4, inline=False)
            embed.add_field(name='-당신은 언랭-', value="언랭은 정보제공 따위 안합니다.", inline=False)
            await message.channel.send(embed=embed)
        else:
            embed.add_field(name='당신의 티어', value=rank4, inline=False)
            embed.add_field(name='당신의 LP(점수)', value=jumsu4, inline=False)
            embed.add_field(name='당신의 승,패 정보', value=winlose2txt + " " + winlose2_1txt, inline=False)
            embed.add_field(name='당신의 승률', value=winlose2_2txt, inline=False)
            await message.channel.send(embed=embed)




access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
