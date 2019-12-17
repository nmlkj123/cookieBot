import discord
from urllib.request import urlopen, Request
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
    await client.change_presence(activity=discord.Game(name="!명령어 "))


def f(x): return {'!원딜': 'ADC', '!정글': 'JUNGLE', '!미드': 'MID', '!탑': 'TOP', '!서포터': 'SUPPORT'}.get(x, '3')


def b(x): return {'종합': '0', '소설': '1', '에세이': '55889', '자격증': '1383', '경제경영': '170',
                  '인문': '656', '사회과학': '798', '경제경영': '170', '과학': '987', '외국어': '1322',
                  '건강/취미': '55890', '라노벨': '50927', '종교': '1237', '가정/요리': '1230', '역사': '74', '자기계발': '336',
                  '여행': '1196', '컴퓨터': '351', '만화': '2551'}.get(x, '3')


@client.event
async def on_message(message):
    if message.content.startswith("!메이플"):
        location = message.content[5:]

        enc_location = urllib.parse.quote(location)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://maple.gg/u/' + enc_location

        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        imaget = bsObj.find('div', {'class': 'col-6 col-md-8 col-lg-6'})
        image=imaget.find('img').get('src')
        title = bsObj.find('div', {'class': 'col-lg-8'})
        worldt = title.find('img')
        worldm=worldt.get('src')
        worldn = title.find('img').get('alt')
        name = title.find('b').text
        infoa=title.find('ul', {'class': 'user-summary-list'}).text.replace('\n','|')
        infoa=infoa.replace('도|','도:')
        infob=title.find('div',{'class':'row row-normal user-additional'}).text.replace(' ','')
        infob=infob.replace('\n','')
        infob = infob.replace('\n', ' ')
        infob = infob.replace('종합랭킹', '\n🔹종합랭킹: ')
        infob = infob.replace('월드랭킹', '🔹월드랭킹: ')
        infob = infob.replace('직업랭킹(월드)', '🔹직업랭킹(월드): ')
        infob = infob.replace('직업랭킹(전체)', '🔹직업랭킹(전체): ')
        infob = infob.replace('위', '위\n')
        infob = infob.replace('길드', '🔸길드: ')

        embed = discord.Embed(
            title=name+'님의 정보',
            description="월드: "+worldn,
            colour=discord.Colour.green()
        )

        embed.set_image(url=image)
        embed.add_field(name='정보', value=infoa+'\n'+infob, inline=False)  # 현재날씨

        embed.set_thumbnail(url=worldm)
        await message.channel.send(embed=embed)

        return
    if message.content.startswith("!급식"):

        location = message.content[4:]

        enc_location = urllib.parse.quote(location + ' 급식')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location

        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")

        title= bsObj.find('div',{'class':'sc cs_school _cs_school'})
        main_title=title.find('strong').text
        area = bsObj.find('div', {'data-time-target': 'true'})

        embed = discord.Embed(
            title=' 급식정보',
            description=main_title,
            colour=discord.Colour.green()
        )

        for y in range(0, 2):
            if(y==1):
                area = area.find_next_sibling()

            menu_info = area.find_all('li',{'class': 'menu_info'})
            todays = menu_info[0].find('strong').text
            tomorrows = menu_info[1].find('strong').text
            todayr = menu_info[0].find_all('li')
            tomorrowr = menu_info[1].find_all('li')
            todayl = ''
            tomorrowl = ''
            for i in range(0, len(todayr)):
                if (i == 0):
                    todayl += todayr[i].text
                else:
                    todayl += '\n'+todayr[i].text

            for i in range(0, len(tomorrowr)):
                if (i == 0):
                    tomorrowl += tomorrowr[i].text
                else:
                    tomorrowl += '\n'+tomorrowr[i].text



            embed.add_field(name=todays, value=todayl, inline=False)  # 현재날씨
            embed.add_field(name=tomorrows, value=tomorrowl, inline=False)  # 현재날씨

        await message.channel.send(embed=embed)

        return

    if message.content.startswith('!서정'):
        lolm = [
            '분명 챌린저 였으나, 상대하는것은 마치 다이아와 같았으니 우리팀 피지컬에 혀를 내두르며 채팅을 치더라. \n\n저 우롱하는 손짓을 보라! 마치 캐리 한다는 듯이 욕을 던져대니 어이하여 죽지않으리오. 어허, 라인전에서 풀콤맞고 피가 너덜이 나니 그녀가 아이쿠 하며 길을 서두르더라.\n\n아아 억울하다. 내가 본것은 소녀이거늘, 어이하여 상대하는 것은 듬직한 남자같은가. 오늘도 그녀의 캐리로 눈을 적시니 아아 달이 밝구나. 언제서야 그녀가 음성채팅을 할까.\n\n오랜 친구 관리자 겨울은 그녀와 함께 게임을 끌며 풍월을 읊었건만 어인 일로 도플갱어가  있는가 하여 그녀에 물으니, 아아 그녀는 저 악마같은 웃음으로 디스코드에서 사라졌나이다. 채팅창을 보시옵소서 저 소녀의 탈을 쓴 마녀가 우리를 핍박하나이다.\n\n그녀 잡아 벌하고 싶으나 힘이 모자르구나. 하늘이 이를 어여삐 여겨 고소를 내리오니 서정아 서정아 어두운 뒷골목 에서 우리를 해하지 말아라 해하지 말아라. 두려울 것은 그것이 아니거늘 다른 곳에서 화면넘어 웃고있는 그녀를 조심 하여라.\n\n그녀는이미 이세계 사람이더라.\n[RIP] 2019.07.18 ']
        await message.channel.send(
            embed=discord.Embed(description=random.choice(lolm), colour=discord.Colour.red()))
        return

    if message.content.startswith("!책"):
        learn = message.content.split(" ")
        if (len(learn) < 2):
            location = '3'
        else:
            location = learn[1]
        a = b(location)
        if (a == '3'):
            await message.channel.send(
                embed=discord.Embed(description="!책 (종합, 소설, 에세이, 자격증, 경제경영, 인문, 사회과학, 경제경영, 과학,\n "
                                                "외국어, 건강/취미, 라노벨, 종교, 가정/요리, 역사, 자기계발, 여행, 컴퓨터, 만화",
                                    colour=discord.Colour.green()), delete_after=60)
            return

        enc_location = urllib.parse.quote(a)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&CID=' + enc_location

        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        listi = bsObj.find_all('div', {'class': 'ss_book_box'})
        # print(listi)
        embed = discord.Embed(
            title='베스트셀러',
            description=location,

            colour=discord.Colour.green()
        )
        for i in range(0, 15):

            cover = listi[i].find('img')
            image = cover.get('src')
            # 이름,링크,등등
            linki = listi[i].find('div', {'class': 'ss_book_list'})
            linki2 = linki.find('a', {'class': 'bo3'})
            link = linki2.get('href')
            name = linki2.find('b').text

            aui = linki.find_all('li')
            au = aui[2].text
            au2 = au.split("|")
            if len(au2) < 3:
                au = aui[1].text
                au2 = au.split("|")
            # print(au2)
            if i == 0:
                embed.set_thumbnail(url=image)
            embed.add_field(name=i + 1,
                            value='[%s](<%s>) ' % (name, link) + '\n' + au2[0] + '|' + au2[1] + '|' + au2[2],
                            inline=False)

        await message.channel.send(embed=embed, delete_after=1800)

    if message.content.startswith("!챔피언"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        hdr = {'User-Agent': 'Mozilla/5.0', "Accept-Language": "ko-KR"}
        url = 'https://www.op.gg/champion/' + enc_location + '/statistics'

        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        # 카운터챔피언
        counteri = bsObj.find('table', {
            'class': 'champion-stats-header-matchup__table champion-stats-header-matchup__table--strong tabItem'})
        counterc = counteri.find_all('tr')
        counter = []
        counterw = []
        for i in range(0, len(counterc)):
            s = counterc[i].find('td', {'class': 'champion-stats-header-matchup__table__champion'}).text
            w = counterc[i].find('td', {'class': 'champion-stats-header-matchup__table__winrate'})
            wt = w.find('b').text

            s = s.lstrip().rstrip()
            counterw.insert(i, wt)
            counter.insert(i, s)
        # 쉬운챔피언
        easyi = bsObj.find('table', {
            'class': 'champion-stats-header-matchup__table champion-stats-header-matchup__table--weak tabItem'})
        easyc = easyi.find_all('tr')
        easy = []
        easyw = []
        for i in range(0, len(easyc)):
            e = easyc[i].find('td', {'class': 'champion-stats-header-matchup__table__champion'}).text
            w = easyc[i].find('td', {'class': 'champion-stats-header-matchup__table__winrate'})
            wt = w.find('b').text
            e = e.lstrip().rstrip()
            easyw.insert(i, wt)
            easy.insert(i, e)

        # print(easy)
        # print(easyw)
        imagei = bsObj.find('div', {'class': 'champion-stats-header-info__image'})
        image = 'https:' + imagei.find('img').get('src')
        name = bsObj.find('h1', {'class': 'champion-stats-header-info__name'}).text
        tieri = bsObj.find('div', {'class': 'champion-stats-header-info__tier'})
        tier = tieri.find('b').text
        skilli = bsObj.find('table', {'class': 'champion-overview__table champion-overview__table--summonerspell'})
        skillc = skilli.find_all('tbody')
        skillc2 = skillc[1].find_all('li', {'class': 'champion-stats__list__item tip'})
        skill = []
        for i in range(0, len(skillc2)):
            skill += skillc2[i].find('span').text

        embed = discord.Embed(
            title=name,
            description=tier,

            colour=discord.Colour.green()
        )

        embed.add_field(name='자세한정보', value='[%s](<%s>)' % ('이곳을 눌러 정보보기', url), inline=False)
        embed.add_field(name='\n🔸\n추천 스킬 빌드', value=skill[0] + '>' + skill[1] + '>' + skill[2] + '\n\n 🔹',
                        inline=False)
        embed.add_field(name='카운터 챔피언', value=counter[0] + ' 승률 : ' + counterw[0] +
                                              '\n' + counter[1] + ' 승률 : ' + counterw[1] +
                                              '\n' + counter[2] + ' 승률 : ' + counterw[2], inline=True)
        embed.add_field(name='상대하기 쉬운 챔피언', value=easy[0] + ' 승률 : ' + easyw[0] +
                                                  '\n' + easy[1] + ' 승률 : ' + easyw[1] +
                                                  '\n' + easy[2] + ' 승률 : ' + easyw[2], inline=True)

        embed.set_thumbnail(url=image)
        await message.channel.send(embed=embed, delete_after=300)

    if message.content.startswith("!미드") or message.content.startswith("!원딜") or message.content.startswith("!탑") \
            or message.content.startswith("!정글") or message.content.startswith("!서포터"):
        learn = message.content.split(" ")
        location = 1
        line = f(learn[0].replace(" ", ""))

        if len(learn) == 1:
            location = location * 5
        else:
            location = int(learn[1]) * 5
        url = 'https://kr.op.gg/champion/statistics'
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")

        top = bsObj.find('tbody', {'class': 'tabItem champion-trend-tier-' + line})
        tr = top.find_all('tr')
        if (len(tr) < location):
            location = len(tr)
        for i in range(location - 5, location):
            rank = tr[i].find('td', {'class': 'champion-index-table__cell champion-index-table__cell--rank'})

            name = tr[i].find('div', {'class': 'champion-index-table__name'})
            link = tr[i].find('td', {'class': 'champion-index-table__cell champion-index-table__cell--champion'})
            link2 = link.find('a')
            link3 = 'https://www.op.gg' + link2.get('href')
            wli = tr[i].find_all('td', {'class': 'champion-index-table__cell champion-index-table__cell--value'})
            win = wli[0]
            pix = wli[1]
            icon = wli[2].find('img')
            icon2 = icon.get('src')

            embed = discord.Embed(
                title=name.text,
                description='승률 :' + win.text + ', 픽률 :' + pix.text,

                colour=discord.Colour.green()
            )
            embed.add_field(name='정보보기', value='[%s](<%s>)' % ('이곳을 눌러 정보보기', link3), inline=False)
            embed.set_thumbnail(url='http://opgg-static.akamaized.net/images/lol/champion/' + name.text.replace(" ",
                                                                                                                "") + '.png?image=w_140&v=1')
            embed.set_image(url='http:' + icon2)
            await message.channel.send(embed=embed, delete_after=300)

    if message.content.startswith("!날씨"):

        location = message.content[4:]

        enc_location = urllib.parse.quote(location + '날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location

        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")

        url2 = "https://weather.naver.com/life/wetrClsrmIcon.nhn"
        html2 = urllib.request.urlopen(url2)

        bsObj2 = bs4.BeautifulSoup(html2, "html.parser")

        img = bsObj2.find('table', {'class': 'tbl_type1'})
        imgs = img.find_all('img')

        area1 = bsObj.find('div', {'class': 'weather_box'})

        area = area1('div', {'class': 'select_box'})

        toarea = area1.find('em')
        areas = toarea.text

        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # 온도
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지
        icon = todayValue.split(',')
        src = ''
        for i in range(0, len(imgs)):
            s = imgs[i].get('alt')
            if (s.replace(" ", "") == icon[0]):
                src = imgs[i].get('src')

        embed = discord.Embed(
            title=' 날씨 정보',
            description=areas + '[%s](<%s>)' % ('\n\n(자세히보기 클릭)', url),
            colour=discord.Colour.gold()
        )
        embed.set_thumbnail(url=src)

        embed.add_field(name='-현재날씨', value='```asciidoc\n= ' + todayTemp + '˚' + ' =\n```' +
                                            '```yaml\n' + todayValue + '\n```' +
                                            '```fix\n' + tomorrowTemp + ' , ' + todayFeelingTemp + ' , 미세먼지: ' + todayMiseaMongi + '\n```\n',
                        inline=False)  # 현재날씨
        embed.add_field(name='-내일오전', value='```asciidoc\n= ' + tomorrowMoring + '˚' + ' =\n```' +
                                            '```yaml\n' + tomorrowValue + '\n```', inline=True)  # 내일오전
        embed.add_field(name='-내일오후', value='```asciidoc\n= ' + tomorrowAfterTemp + '˚' + ' =\n```' +
                                            '```yaml\n' + tomorrowAfterValue + '\n```', inline=True)  # 내일오후

        await message.channel.send(embed=embed)

    if message.content.startswith('!냥냥'):
        embed = discord.Embed(
            title='야옹~! ฅ•ω•ฅ  ि०॰०ॢी !!!',
            description='랜덤고먐이',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase + str(randomNum)
        embed.set_image(url=urlF)
        await message.channel.send(embed=embed)

    if message.content.startswith('!멍멍'):
        embed = discord.Embed(
            title='왈왈~! (⁎˃ᆺ˂)  ʢᵕᴗᵕʡ !!!',
            description='랜덤 강아지',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240/dog?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase + str(randomNum)
        embed.set_image(url=urlF)
        await message.channel.send(embed=embed)

    if message.content.startswith('!롤각'):

        randomNum = random.randrange(1, 3)
        if randomNum == 1:
            lolm = ['강해지고싶나??? 그럼 롤을 키시게!! (￣ω￣)', '롤각 가즈아~ (* >ω<) (＞Д＜)ゝ', '★오늘의메타 : 탑소라카 GOGO -얼른키라구!'
                , '오늘은 승급하는날 입니다（＾∀＾）', '이번판은 팀원들이 캐리 하겠네요! ＾ω＾ y', '이번판은 당신의 손에 승패가 갈립니다.열시미 하세요! (￣`Д´￣)9']
            await message.channel.send(
                embed=discord.Embed(description=random.choice(lolm), colour=discord.Colour.green()), delete_after=300)
            return
        else:
            lolm = ['응 오늘은아니야~ (ಥ﹏ಥ)', '오늘하면 9대1을 하게 될 것입니다 물론 당신이 1 (;Д;)(Ｔ▽Ｔ)',
                    '우리팀 정글이 던지는날입니다...마음의 준비를하세요! ☜╮(´ิ∀´ิ☜╮)'
                , '오늘은 10연패각 입니다ㄷㄷ (;´Д｀)', '당장 메이플을 키세요 ԅ( ˘ω˘ԅ)', '지금하면 15분 서렌각;; ((( ；ﾟДﾟ)))']
            await message.channel.send(
                embed=discord.Embed(description=random.choice(lolm), colour=discord.Colour.red()), delete_after=300)
            return

    if message.content.startswith('!실검'):

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

        await message.channel.send(embed=embed, delete_after=300)

    if message.content.startswith("!명령어"):
        embed = discord.Embed(
            title='(✪㉨✪) (⌬̀⌄⌬́) （๑✧∀✧๑）٩(●ᴗ●)۶',
            description='-쿠키봇의 명령어\n\n ',
            colour=discord.Colour.blue()
        )
        dtime = datetime.datetime.now()
        embed.add_field(name='!롤 아이디', value='롤op.gg 전적검색 결과를 보여줍니다 참고- 언랭은 정보따위 제공안합니다.', inline=False)
        embed.add_field(name='!챔피언 챔피언이름', value='챔피언의 간단한 정보를 불러 옵니다 예)!챔피언 모데카이저 .', inline=True)
        embed.add_field(name='!탑 숫자', value='탑 챔피언의 티어와 승률을 순서대로 보여줍니다 예)!탑 1.', inline=True)
        embed.add_field(name='!미드 숫자', value='미드 챔피언의 티어와 승률을 5개씩 순서대로 보여줍니다 예)!미드 1.', inline=True)
        embed.add_field(name='!정글 숫자', value='정글 챔피언의 티어와 승률을 5개씩 순서대로 보여줍니다 예)!정글 1.', inline=True)
        embed.add_field(name='!원딜 숫자', value='원딜 챔피언의 티어와 승률을 5개씩 순서대로 보여줍니다 예)!원딜 1.', inline=True)
        embed.add_field(name='!서포터 숫자', value='서포터 챔피언의 티어와 승률을 5개씩 순서대로 보여줍니다 예)!서포터 1.', inline=True)
        embed.add_field(name='!롤각', value='오늘 롤의 운세를 정해줍니다 찡긋^.', inline=False)
        embed.add_field(name='!냥냥', value='고양이 사진을 무작위로 보여줍니다.ฅ•ω•ฅ', inline=False)
        embed.add_field(name='!멍멍', value='강아지 사진을 무작위로 보여줍니다.(⁎˃ᆺ˂)', inline=False)
        embed.add_field(name='!play 유튜브 링크', value='뮤직앱에 노래를 추가합니다.', inline=False)
        embed.add_field(name='!np', value='현재 플레이중인 노래의 제목,정보를 봅니다. ', inline=False)
        embed.add_field(name='!queue', value='뮤직앱에 예약중인 플레이 리스트를 봅니다.', inline=False)
        embed.add_field(name='!skip', value='현재곡 스킵 투표를 합니다.', inline=False)
        embed.add_field(name='!핑', value='지연시간확인. ', inline=False)
        embed.add_field(name='!투표 제목/내용/내용...', value='투표함을 만듭니다. 이모지를 클릭하여 투표를 진행합니다.', inline=False)
        embed.add_field(name='!실검', value='네이버 실시간 검색순위를 1위부터 10위까지 보여줍니다.', inline=False)
        embed.add_field(name='!운세 생일(월/일)', value='★ 별자리 운세를 알아봅니다 예)!운세 01/12.', inline=False)
        embed.add_field(name='!날씨 지역', value='현재 날씨와 내일의 날씨를 불러옵니다. 예)!날씨 서울.', inline=False)
        embed.add_field(name='!책 장르', value='주간 베트스셀러 TOP15 위를 불러 옵니다. \n장르(종합, 소설, 에세이, 자격증, 경제경영, 인문, 사회과학, 경제경영, 과학,'
                                            '\n 외국어, 건강/취미, 라노벨, 종교, 가정/요리, 역사, 자기계발, 여행, 컴퓨터, 만화)', inline=False)
        embed.add_field(name='!급식 학교명', value='급식을 확인.', inline=False)
        embed.add_field(name='!메이플 캐릭터명', value='메이플스토리 캐릭터 정보를 확인.', inline=False)
        embed.set_footer(text=str(dtime.year) + "년 " + str(dtime.month) + "월 " + str(dtime.day) + "일 " + str(
            dtime.hour) + "시 " + str(dtime.minute) + "분")
        await message.channel.send(embed=embed, delete_after=300)
        return
    if message.content.startswith("!투표"):

        vote = message.content[4:].split("/")

        await message.channel.send("✉투표 - " + vote[0])
        for i in range(1, len(vote)):
            
            choose = await client.send_message(message.channel,vote[i])
            await client.add_reaction(choose,'👍')
        return
    if message.content.startswith("!핑"):
        ping = '%.2f' % (1000 * (client.latency))
        await  message.channel.send(ping + "ms", delete_after=15)
        return
    if message.content.startswith("!운세"):
        vote = message.content[4:].split("/")
        # print(vote)
        if vote == ['']:
            return
        num = ""
        for i in range(0, len(vote), 1):
            num += vote[i]

        if not num.isdigit():
            return
        num = int(num)
        pos = ""
        if num >= 120 and num <= 218:
            pos = "물병자리"
        elif num >= 219 and num <= 320:
            pos = "물고기자리"
        elif num >= 321 and num <= 419:
            pos = "양자리"
        elif num >= 420 and num <= 520:
            pos = "황소자리"
        elif num >= 521 and num <= 621:
            pos = "쌍둥이자리"
        elif num >= 622 and num <= 722:
            pos = "게자리"
        elif num >= 723 and num <= 822:
            pos = "사자자리"
        elif num >= 823 and num <= 923:
            pos = "처녀자리"
        elif num >= 924 and num <= 1022:
            pos = "천칭자리"
        elif num >= 1023 and num <= 1122:
            pos = "전갈자리"
        elif num >= 1123 and num <= 1224:
            pos = "사수자리"
        elif num >= 1225 and num <= 1231 or num >= 101 and num <= 119:
            pos = "염소자리"
        else:
            pos = "없음"
        if (pos == "없음"):
            return

        print(pos)
        enc_location = urllib.parse.quote(pos)
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=" + enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        luck1 = bsObj.find("div", {"role": "main"})
        luck2 = luck1.find("div", {"class": "main_pack"})
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
        await message.channel.send(embed=embed, delete_after=1800)
        return
    if message.content.startswith("!롤"):
        learn = message.content[3:].split(" ")
        print(learn[0])
        location = learn[0]
        if len(learn) > 1:
            loc = ""
            for l in range(0, len(learn), 1):
                loc += learn[l]
            location = loc
        enc_location = urllib.parse.quote(location)
        print(enc_location)
        url = "http://www.op.gg/summoner/userName=" + enc_location
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        id1 = bsObj.find("div", {"class": "Profile"})

        if id1 is None:
            await message.channel.send(
                embed=discord.Embed(description="입력하신 아이디의 정보가없습니다", colour=discord.Colour.green()), delete_after=15)
            return
        id2 = id1.find("div", {"class": "Information"})
        id3 = id2.find("span", {"class": "Name"})
        id4 = id3.text

        imaget1 = bsObj.find("div", {"class": "SummonerRatingMedium"})
        imaget2 = imaget1.find("img", {"class": "Image"})
        imaget3 = imaget2.get('src')
        imagetCut = imaget3.split("/")
        imageThumbnail = imagetCut[len(imagetCut) - 1]

        print(imageThumbnail)
        imagec1 = bsObj.find("div", {"class": "ProfileIcon"})
        imagec2 = imagec1.find("img")
        imagec3 = imagec2.get('src')
        imagecCut = imagec3.split("/")
        imageIcon = imagecCut[len(imagecCut) - 1]

        rank1 = bsObj.find("div", {"class": "TierRankInfo"})
        rank2 = rank1.find("div", {"class": "TierRank"})
        rank4 = rank2.text  # 티어표시 (브론즈1,2,3,4,5 등등)
        if rank4 == '':
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
            title=id4 + '님의 롤 정보',
            description='롤 정보입니다.',

            colour=discord.Colour.red()
        )

        embed.set_thumbnail(url="http://opgg-static.akamaized.net/images/medals/" + imageThumbnail)
        embed.set_image(url="http://opgg-static.akamaized.net/images/profile_icons/" + imageIcon)
        if rank4.strip() == 'Unranked':
            embed.add_field(name='당신의 티어', value=rank4, inline=False)
            embed.add_field(name='-당신은 언랭-', value="언랭은 정보제공 따위 안합니다.", inline=False)
            await message.channel.send(embed=embed, delete_after=300)
        else:
            embed.add_field(name='당신의 티어', value=rank4, inline=False)
            embed.add_field(name='당신의 LP(점수)', value=jumsu4, inline=False)
            embed.add_field(name='당신의 승,패 정보', value=winlose2txt + " " + winlose2_1txt, inline=False)
            embed.add_field(name='당신의 승률', value=winlose2_2txt, inline=False)
            await message.channel.send(embed=embed)




access_token = os.environ["BOT_TOKEN"]

client.run(access_token)
