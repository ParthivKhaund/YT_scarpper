# find title 
# find category
# find channel name
# find subscriber count 
# find watch time
# total amount of comments

from bs4 import BeautifulSoup
import requests 
import re

url = "https://www.youtube.com/watch?v=OeHjN4oWVfk"

site = requests.get(url)
#print(site.status_code)
soup = BeautifulSoup(site.content,"html.parser")

#open("video.html","w",encoding ="utf8").write(site.text)

#  title

title_finder = soup.find(class_="watch-title")
title= title_finder.get_text()

# category 

category_finder = soup.select("#watch-description-extras > ul > li > ul > li > a")

category = category_finder[-1].get_text()

# channel name

name = soup.find_all(class_="yt-uix-sessionlink spf-link")

# if trending video 

trending_test = re.match ("#.*",name[0].get_text())

if trending_test:
	channel_name = name[1].get_text()
else:
	channel_name = name[0].get_text()


