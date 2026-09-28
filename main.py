
import requests
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

PARAMETERS = {
"lat" : 24.617838,
"lon" :  46.748404,
"appid" : "71ab17ddeffca062d4f83895801c0fd2",
"cnt" : 4
}



response = requests.get("https://api.openweathermap.org/data/2.5/forecast" , params=PARAMETERS)
response.raise_for_status()
data = response.json()
print(data)
will_rain = False
for code in range(4):
    if int(data["list"][code]["weather"][0]["id"]) <=700:
        will_rain =True

if will_rain:
    connection = SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=EMAIL , password= PASSWORD)
    connection.sendmail(from_addr=EMAIL , to_addrs="mmaherali250@gmail.com" , msg="Subject:attention🔔 \n\n it will rain bring an umbrella☂️☂️")
else:
    connect = SMTP("smtp.gmail.com")
    connect.starttls()
    connect.login(user=EMAIL , password= PASSWORD)
    connect.sendmail(from_addr=EMAIL , to_addrs="mmaherali250@gmail.com" , msg="Subject:attention🔔 \n\n no rain expected")
