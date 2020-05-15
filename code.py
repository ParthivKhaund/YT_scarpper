# selenium 
# go to different videos 
# scroll down 
# call scrapper 

from bs4 import BeautifulSoup
import requests 
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()

title_list = []
category_list = []
channel_name_list  = []
subscriber_count_list = []
views_list = []
likes_list = []
dislikes_list = []

# # to clear cache 
# browser.get('chrome://settings/clearBrowserData')
# browser.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)

limit = 10
# scrapper function
def scrapper_1(url):

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

# starter Url
#url = input("Please give start Url : ")
url = "https://www.youtube.com/watch?v=qFkNATtc3mc"

browser.get(url)

# wait for all to load
browser.implicitly_wait(10)

# call scrapper 
scrapper_1(url)


for i in range(limit):
	browser.implicitly_wait(10)
	next_url = browser.find_element_by_css_selector("#video-title")
	next_url.click()
	url = (browser.current_url)
	scrapper_1(url)



# list output to be submitted to csv

print(title_list)
print(category_list)
print(channel_name_list)
print(subscriber_count_list)
print(views_list)
print(likes_list)
print(dislikes_list)