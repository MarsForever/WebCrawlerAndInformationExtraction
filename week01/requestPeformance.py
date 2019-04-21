import requests
from datetime import datetime
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''
 
def main():
    url = "https://www.baidu.com"
    t0 = datetime.now()
    for i in range(1,101):
        getHTMLText(url)
        print('\r{} % have been finished.'.format(i), end='')
    t1 = datetime.now()
    t = (t1 - t0).total_seconds()
    print('\n爬取100次共花费%.1f秒!' % t)
