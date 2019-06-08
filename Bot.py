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
    #await client.change_presence(activity=discord.Game(name="!명령어 "))
    game = discord.Game("!명령어")
    await client.change_presence(status=discord.Status.idle, activity=game)




@client.event
async def on_message(message):
    
    
    if message.content.startswith('!롤각'):

        randomNum = random.randrange(1, 3)
        if randomNum == 1:
            lolm=['강해지고싶나??? 그럼 롤을 키시게!! (￣ω￣)','롤각 가즈아~ (* >ω<) (＞Д＜)ゝ','★오늘의메타 : 탑소라카 GOGO -얼른키라구!'
                  ,'오늘은 승급하는날 입니다（＾∀＾）','이번판은 팀원들이 캐리 하겠네요! ＾ω＾ y','이번판은 당신의 손에 승패가 갈립니다.열시미 하세요! (￣`Д´￣)9']
            await message.channel.send(
                embed=discord.Embed(description=random.choice(lolm), colour=discord.Colour.green()),delete_after=300)
            return
        else:
            lolm = ['응 오늘은아니야~ (ಥ﹏ಥ)', '오늘하면 9대1을 하게 될 것입니다 물론 당신이 1 (;Д;)(Ｔ▽Ｔ)', '우리팀 정글이 던지는날입니다...마음의 준비를하세요! ☜╮(´ิ∀´ิ☜╮)'
                , '오늘은 10연패각 입니다ㄷㄷ (;´Д｀)','당장 메이플을 키세요 ԅ( ˘ω˘ԅ)','지금하면 15분 서렌각;; ((( ；ﾟДﾟ)))']
            await message.channel.send(
                embed=discord.Embed(description=random.choice(lolm), colour=discord.Colour.red()),delete_after=300)
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

        await message.channel.send( embed=embed,delete_after=300)

    if message.content.startswith("!명령어"):
        embed = discord.Embed(
            title='(✪㉨✪) (⌬̀⌄⌬́) （๑✧∀✧๑）٩(●ᴗ●)۶',
            description='-쿠키봇의 명령어\n\n ',
            colour=discord.Colour.blue()
        )
        dtime = datetime.datetime.now()
        embed.add_field(name='!롤 아이디', value='롤op.gg 전적검색 결과를 보여줍니다 참고- 언랭은 정보따위 제공안합니다.', inline=True)
        embed.add_field(name='!롤각', value='오늘 롤의 운세를 정해줍니다 찡긋^.', inline=False)
        embed.add_field(name='#play 유튜브 링크', value='뮤직앱에 노래를 추가합니다.', inline=False)
        embed.add_field(name='#np', value='현재 플레이중인 노래의 제목,정보를 봅니다. ', inline=False)
        embed.add_field(name='#queue', value='뮤직앱에 예약중인 플레이 리스트를 봅니다.', inline=False)
        embed.add_field(name='#skip', value='현재곡 스킵 투표를 합니다.', inline=False)
        embed.add_field(name='!핑', value='지연시간확인. ', inline=False)
        embed.add_field(name='!투표 제목/내용/내용...', value='투표함을 만듭니다. 이모지를 클릭하여 투표를 진행합니다.', inline=False)
        embed.add_field(name='!실검', value='네이버 실시간 검색순위를 1위부터 10위까지 보여줍니다.', inline=False)
        embed.add_field(name='!운세 생일(월/일)', value='★ 별자리 운세를 알아봅니다 예)!운세 01/12.', inline=False)
        embed.set_footer(text=str(dtime.year) + "년 " + str(dtime.month) + "월 " + str(dtime.day) + "일 " + str(
            dtime.hour) + "시 " + str(dtime.minute) + "분")
        await message.channel.send(embed=embed,delete_after=60)

    if message.content.startswith("!투표"):

        vote = message.content[4:].split("/")

        await message.channel.send("✉투표 - "+vote[0])
        for i in range(1,len(vote)):
            choose= await  message.channel.send("```"+vote[i]+"```")
            await choose.add_reaction('👍')

    if message.content.startswith("!핑"):
        ping = '%.2f' % (1000 * (client.latency ))
        await  message.channel.send(ping+"ms" ,delete_after=15)

    if message.content.startswith("!운세"):
        vote = message.content[4:].split("/")
        #print(vote)
        if vote == ['']:
            return
        num = ""
        for i in range(0,len(vote),1):
            num+=vote[i]

        if not num.isdigit():
            return
        num=int(num)
        pos=""
        if num>=120 and num<=218:
            pos="물병자리"
        elif num>=219 and num<=320:
             pos="물고기자리"
        elif num>= 321 and num <= 419:
            pos="양자리"
        elif num>= 420 and num <= 520:
            pos="황소자리"
        elif num>= 521 and num <= 621:
            pos="쌍둥이자리"
        elif num>= 622 and num <= 722:
            pos="게자리"
        elif num>= 723 and num <= 822:
            pos="사자자리"
        elif num>= 823 and num <= 923:
            pos="처녀자리"
        elif num>= 924 and num <= 1022:
            pos="천칭자리"
        elif num>= 1023 and num <= 1122:
            pos="전갈자리"
        elif num>= 1123 and num <= 1224:
            pos="사수자리"
        elif num >= 1225 and num <= 1231 or num>=101 and num <= 119:
            pos = "염소자리"
        else:
            pos="없음"
        if(pos=="없음"):
            return

        print(pos)
        enc_location = urllib.parse.quote(pos)
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query="+enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        luck1 = bsObj.find("div", {"role": "main"})
        luck2 = luck1 .find("div", {"class": "main_pack"})
        luck3 = luck2.find("div", {"class": "content_search section"})
        luck4 = luck3.find("div", {"class": "detail detail2"})
        luck5 = luck4.find_all("p", {"class": "text _cs_fortune_text"})
        imagel1 = luck3.find("div", {"class": "thumb"})
        imagel2 = imagel1.find("img")
        imagel3 = imagel2.get('src')

        print(imagel3)

        embed = discord.Embed(
            title='별자리 운세',
            description=pos,

            colour=discord.Colour.purple()
        )

        embed.set_thumbnail(url=imagel3)
        embed.add_field(name='오늘의 운세', value=luck5[0].text, inline=False)
        embed.add_field(name='내일의 운세', value=luck5[1].text, inline=False)
        embed.add_field(name='이주의 운세', value=luck5[2].text, inline=False)
        embed.add_field(name='이달의 운세', value=luck5[3].text, inline=False)
        await message.channel.send(embed=embed, delete_after=300)

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
            await message.channel.send(embed=discord.Embed(description="입력하신 아이디의 정보가없습니다",colour=discord.Colour.green()),delete_after=15)
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
        embed.set_image(url="http://opgg-static.akamaized.net/images/profile_icons/"+imageIcon)
        if rank4.strip() == 'Unranked':
            embed.add_field(name='당신의 티어', value=rank4, inline=False)
            embed.add_field(name='-당신은 언랭-', value="언랭은 정보제공 따위 안합니다.", inline=False)
            await message.channel.send(embed=embed,delete_after=300)
        else:
            embed.add_field(name='당신의 티어', value=rank4, inline=False)
            embed.add_field(name='당신의 LP(점수)', value=jumsu4, inline=False)
            embed.add_field(name='당신의 승,패 정보', value=winlose2txt + " " + winlose2_1txt, inline=False)
            embed.add_field(name='당신의 승률', value=winlose2_2txt, inline=False)
            await message.channel.send(embed=embed,delete_after=300)



access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
