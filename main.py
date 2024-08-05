# Property Hunting Project
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

website_url = "https://appbrewery.github.io/Zillow-Clone/"
form_url = ("https://docs.google.com/forms/d/e/1FAIpQLSeZxgPxGy_83AP-CW92Fq-vmODJmBSPtcFBdlKXKs-x6_o1QQ/viewform?usp=sf_link")

data = requests.get(website_url)
soup = BeautifulSoup(data.content, 'html.parser')

location = soup.find_all(name="address")
link = soup.select(".StyledPropertyCardDataWrapper a")
price = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")

location_list = [address.getText().strip().replace("|", "") for address in location]
print(location_list)

price_list = [prices.getText().strip().replace("/mo", "") for prices in price]
print(price_list)

link_list = [links["href"] for links in link]
print(link_list)

web_chrome = webdriver.ChromeOptions()
web_chrome.add_experimental_option("detach", True)

for i in range(len(price_list)):
    web_driver = webdriver.Chrome(options=web_chrome)
    web_driver.get(url=form_url)
    time.sleep(2)

    price_form = web_driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_form = web_driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    location_form = web_driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    submit_button = web_driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    location_form.send_keys(location_list[i])
    price_form.send_keys(price_list[i])
    link_form.send_keys(link_list[i])

    submit_button.click()


