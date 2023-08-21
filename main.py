import requests
from bs4 import BeautifulSoup
from pprint import pprint
import lxml
import smtplib


User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
Accept_Language = "en-US,en;q=0.9,hi;q=0.8"
URL = "https://www.amazon.in/boAt-Rockerz-255-Pro-Earphones/dp/B08TTXNZ4Y/ref=sr_1_1_sspa?crid=3I1MNTCE72W4N&keywords=boat+neckband+rockerz+255+pro&qid=1678282263&sprefix=boat+neckband+rockerz+255+pro%2Caps%2C497&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

headers = {
"User-Agent": User_Agent,
"Accept-Language": Accept_Language,
}

response = requests.get(URL, headers=headers)
Amazon_web = response.text

soup = BeautifulSoup(Amazon_web, "lxml")
Boat_price = soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
# float_Boat_price = float(Boat_price)
print(Boat_price)

BUY_PRICE = 1100

if Boat_price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
