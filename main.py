# Property Hunting Project
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

website_url = "https://appbrewery.github.io/Zillow-Clone/"
form_url = ("https://docs.google.com/forms/d/e/"
            "1FAIpQLSfqWaWRaoE35-BcIlRj_jq3WMisHWkkh1oslpS8uFWf3WrbFw/viewform?usp=sf_link")

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

web_driver = webdriver.Chrome(options=web_chrome)
web_driver.get(url=form_url)




for i in range(0, len(price_list)):
    price_form = web_driver.find_element(By.CLASS_NAME, "Hvn9fb zHQkBf")
    link_form = web_driver.find_element(By.CLASS_NAME, "Hvn9fb zHQkBf")
    location_form = web_driver.find_element(By.CLASS_NAME, "Hvn9fb zHQkBf")
    submit_button = web_driver.find_element(By.CLASS_NAME, "l4V7wb Fxmcue")
    price_form.send_keys(price_list[i], Keys.ENTER)
    link_form.send_keys(link_list[i], Keys.ENTER)
    location_form.send_keys(location_list[i], Keys.ENTER)
    submit_button.click()


