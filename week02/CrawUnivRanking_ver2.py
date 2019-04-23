import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try :
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUniList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):  #判断是否为tag
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
            
def printUniList(ulist, num):
    tplt = "{0:^10}\t{1:^6}\t{2:^10}"
    print(tplt.format("排名", "学校", "总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUniList(uinfo, html)
    printUniList(uinfo, 20)
main()
