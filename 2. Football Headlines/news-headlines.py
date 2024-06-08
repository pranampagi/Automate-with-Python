from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "/home/pranam/Programs/Python/Automate with Python/chromedriver-linux64/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
	try:
		title = container.find_element(by="xpath", value="./a/span").text
		subtitle = container.find_element(by="xpath", value="./a/h3").text
		link = container.find_element(by="xpath", value="./a").get_attribute("href")
	except:
		continue

	titles.append(title)
	subtitles.append(subtitle)
	links.append(link)

my_dict = {
	"title": titles,
	"subtitle": subtitles,
	"link": links
}

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv("headline.csv")

driver.quit()