import requests
import lxml
from bs4 import BeautifulSoup

User_URL = input("Enter the URL to track price: ")
URL = User_URL
#URL = "https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5TNJHG/ref=sr_1_5?crid=1HJYKWSVL28FI&keywords=iphone+12&qid=1665256623&qu=eyJxc2MiOiI0Ljc1IiwicXNhIjoiNC4wMCIsInFzcCI6IjIuODAifQ%3D%3D&sprefix=iphone+12%2Caps%2C230&sr=8-5"
ACCEPT_LANGUAGE = "en-US,en;q=0.9,hi;q=0.8,en-IN;q=0.7"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
response = requests.get(url=URL, headers={"User-Agent": USER_AGENT, "Accept-Language": ACCEPT_LANGUAGE})
amazon = response.text
soup = BeautifulSoup(amazon, "lxml")
price_span = soup.find_all('span', attrs={"class": "a-offscreen"})
price_text = price_span[0]
price_string = price_text.getText()
price = price_string[1:]
original_price = price.replace(',', '')
print(float(original_price))

