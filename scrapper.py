# scrape YT
# findall channels subscribed and display them 

from bs4 import BeautifulSoup
import requests 


url = "https://www.youtube.com/watch?v=R1WsyFFajz0"

site = requests.get(url)
#print(site.status_code)
soup = BeautifulSoup(site.content,"lxml")

divs = soup.findAll("div")

name = soup.find(class_="watch-title")
print(name)