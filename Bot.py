import discord

import urllib.request

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
    if message.content.startswith("!핑"):
        ping = '%.2f' % (1000 * (client.latency))
        await  message.channel.send(ping+"ms")

    if message.content.startswith("!롤"):
        learn = message.content.split(" ")
        location = learn[1]
        if len(learn) > 3:
            loc = ""
            for l in range(1, len(learn), 1):
                loc += learn[l]
            location = loc

        print(learn[1])
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




client.run('NTgyNzc3MzU0NjIzOTA5ODk4.XOywRA.-rbxJkijR2Lvhe30Kh2JQKH4n48')
