# find title 
# find category
# find channel name
# find subscriber count 
# find views 
# find likes and dislikes 
# language
# location

# total amount of comments (for this we would need to use selenium as it only loads comments as we scroll down)


from bs4 import BeautifulSoup
import requests 
import re

url = "https://www.youtube.com/watch?v=95MAxatKgG4"

site = requests.get(url)
#print(site.status_code)
soup = BeautifulSoup(site.content,"html.parser")

#open("video.html","w",encoding ="utf8").write(site.text)

#  title

title = soup.find(class_="watch-title").get_text().strip()

# category 

category_finder = soup.select("#watch-description-extras > ul > li > ul > li > a")

category = category_finder[0].get_text()


# channel name

name = soup.find_all(class_="yt-uix-sessionlink spf-link")

# if trending video 

trending_test = re.match ("#.*",name[0].get_text())

if trending_test:
	channel_name = name[1].get_text()
else:
	channel_name = name[0].get_text()

# subscriber count 

subscriber_count = soup.find(class_="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count").get_text()

# views 

views = soup.find(class_="watch-view-count").get_text()

# amount of likes and dislikes 

likes = soup.find_all(class_="yt-uix-button-content")

dislikes = likes[-10].get_text()

likes = likes[-13].get_text()

# location 

# language

#test output 
print(title)
print(category)
print(channel_name)
print(subscriber_count)
print(views)
print(likes)
print(dislikes)

