import requests
from email.message import EmailMessage
import smtplib
import time
import datetime as dt


url = "http://api.open-notify.org/iss-now.json"

parameters = {
    "lat": 31.768318,
    "lng": 35.213711,
    "formatted": 0
}

my_lat = 31.7396570414
my_lng = 35.2033641865

response = requests.get(url)
data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

response = requests.get(
    " https://api.sunrise-sunset.org/json", params=parameters)
data2 = response.json()

sunrise = data2["results"]["sunrise"].split("T")[1].split(":")[0]
if int(sunrise) < 10:
    sunrise = data2["results"]["sunrise"].split("T")[1].split(":")[
        0].split("0")[1]
else:
    sunrise = data2["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data2["results"]["sunset"].split("T")[1].split(":")[0]
today = dt.datetime.now().hour

end = False

while end == False:
    time.sleep(60)
    if int(sunset) <= int(today) <= int(sunrise):
        print("its night time")

        if my_lat - 5 <= latitude <= my_lat + 5 and my_lng -5 <= longitude <= my_lng+5:
            email = EmailMessage()
            email["from"] = "mysterious Alien"
            email["to"] = "miladbannourah@outlook.com"
            email["subject"] = "look UP ☝☝"
            email.set_content(
                "the satelite is on top of Beit safafa look at the sky and try to find the fastest star moving")

            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login("hstevejobs@gmail.com", "milomilo2002")
                smtp.send_message(email)
                print("email sent")
