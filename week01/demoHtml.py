import requests
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")
soup.prettify()