import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/-/en/Artist-Graphics-Display-Function-Learning/dp/B07VPHR6GD/ref=sr_1_6?dchild=1&keywords=xp-pen+artist12+pro+graphics+drawing+tablet+11%2C6+zoll+full+hd-display+f%C3%BCr+windows%2C+mac&qid=1605296035&quartzVehicle=184-492&replacementKeywords=xp-pen+artist12+graphics+drawing+tablet+11%2C6+zoll+full+hd-display+f%C3%BCr+windows%2C+mac&sr=8-6'


headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[1:5])


    if(converted_price < 300):
        send_mail()


    print(converted_price)
    print(title.strip())

    if(converted_price < 300):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("mymail@gmail.com", "mypassword")

    subject = "hej the price is 300"

    body = " check the amazon link : https://www.amazon.de/-/en/Artist-Graphics-Display-Function-Learning/dp/B07VPHR6GD/ref=sr_1_6?dchild=1&keywords=xp-pen+artist12+pro+graphics+drawing+tablet+11%2C6+zoll+full+hd-display+f%C3%BCr+windows%2C+mac&qid=1605296035&quartzVehicle=184-492&replacementKeywords=xp-pen+artist12+graphics+drawing+tablet+11%2C6+zoll+full+hd-display+f%C3%BCr+windows%2C+mac&sr=8-6"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(

        "mymail@gmail.com",
        "mymail@gmail.com",
        msg

    )
    print("EMAIL HAS BEEN SENT")

    server.quit()


check_price()