from bs4 import BeautifulSoup
import requests 
import re


url = ["https://www.youtube.com/watch?v=95MAxatKgG4","https://www.youtube.com/watch?v=WvQ3xCmsphU","https://www.youtube.com/watch?v=HNziOoXDBeg","https://www.youtube.com/watch?v=cWrMvQEYVCA"]

title_list = []
category_list = []
channel_name_list  = []
subscriber_count_list = []
views_list = []
likes_list = []
dislikes_list = []


def scrapper(url):

	site = requests.get(url)
	#print(site.status_code)
	soup = BeautifulSoup(site.content,"html.parser")

	# to see and find HTML correct locators
	#open("video.html","w",encoding ="utf8").write(site.text)

	#  title

	title = soup.find(class_="watch-title").get_text().strip()
	title_list.append(title)
	# category 

	category_finder = soup.select("#watch-description-extras > ul > li > ul > li > a")

	category = category_finder[0].get_text()
	category_list.append(category)

	# channel name

	name = soup.find_all(class_="yt-uix-sessionlink spf-link")

	# if trending video 

	trending_test = re.match ("#.*",name[0].get_text())

	if trending_test:
		channel_name = name[1].get_text()
	else:
		channel_name = name[0].get_text()

	channel_name_list.append(channel_name)
	# subscriber count 

	subscriber_count = soup.find(class_="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count").get_text()
	subscriber_count_list.append(subscriber_count)
	# views 

	views = soup.find(class_="watch-view-count").get_text()
	views_list.append(views)
	# amount of likes and dislikes 

	thumbs = soup.find_all(class_="yt-uix-button-content")

	dislikes = thumbs[-10].get_text()
	dislikes_list.append(dislikes)
	likes = thumbs[-13].get_text()
	likes_list.append(likes)

# for occasional NoneTpe error 
try:
	for i in url:
		scrapper(i)
except AttributeError:
	for i in url:
		scrapper(i)

print(title_list)
print(category_list)
print(channel_name_list)
print(subscriber_count_list)
print(views_list)
print(likes_list)
print(dislikes_list)



