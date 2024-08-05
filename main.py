# Property Hunting Project
from bs4 import BeautifulSoup
import requests

url = "https://appbrewery.github.io/Zillow-Clone/"

data = requests.get(url)
soup = BeautifulSoup(data.content, 'html.parser')

location = soup.find_all(name="address")
link = soup.select(".StyledPropertyCardDataWrapper a")
price = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")

location_list = [address.getText().strip() for address in location]
print(location_list)

price_list = [prices.getText().strip() for prices in price ]
print(price_list)

link_list = [links["href"] for links in link]
print(link_list)

