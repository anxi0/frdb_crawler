import requests
from bs4 import BeautifulSoup

r = requests.get('http://frdb2.ivyro.net/2.htm')
f = open('result.csv', 'w', encoding='UTF-8-sig')

soup = BeautifulSoup(r.text, 'html.parser')
tables = soup.select('table')
# table 분리
for table in tables:
    trs = table.select('tr')
    # title 분리
    for tr_index in range(0, len(trs)):
        td = trs[tr_index].select('td')
        if (len(td) != 0):
            # 개통 년도
            if ("년 개통" in td[0].text):
                # print(td[0].text.strip(), end="")
                f.write(td[0].text.strip()[2:6])
            else:
                # 테이블 내용
                if len(td) != 1:
                    # 인덱스 제목
                    if ((len(td[0]) != 0) and (td[0].text.strip() not in ["미래철도 DB", "개통시기별, 개통내역"])):
                        # print(","+td[0]
                        #   .select('p')[0].select(
                        # 'a')[0]
                        #   .text+",", end="")
                        f.write(",\""+td[0].text+"\",")
                    # 진행 상황
                    if (len(td[0].select('img')) != 0):
                        progress = td[0].select('img')[0].get('src')[8:9]
                        if progress == '1':
                            # print("구상중,", end="")
                            f.write("구상중(예타 전),")

                        elif progress == '2':
                            # print("계획중,", end="")
                            f.write("계획중,")
                        elif progress == '3':
                            # print("설계중,", end="")
                            f.write("설계중,")
                        elif progress == '4':
                            # print("시공중,", end="")
                            f.write("시공중,")

                    # 인덱스 내용
                    if ("[" not in td[1].text.strip()):
                        # print(td[1].text.strip())
                        f.write("\""+td[1].text.strip()+"\""+"\n")
f.close()
