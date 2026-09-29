import os
import smtplib
import requests

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
APPID = os.environ.get("APPID")
PARAMETERS = {
    "lat": 24.617838,
    "lon": 46.748404,  # تم إصلاح المسافة الخفية هنا
    "appid": APPID,
    "cnt": 4,
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params=PARAMETERS
)
response.raise_for_status()
data = response.json()

will_rain = False
for hour_data in data["list"]:
    weather_id = int(hour_data["weather"][0]["id"])
    if weather_id < 700:  # الرموز أقل من 700 تعني أمطار وخيول ورعد
        will_rain = True
        break

# تحديد نص الرسالة بناءً على الحالة
subject = "Attention: Weather Update"
message_body = (
    "It will rain today, bring an umbrella!"
    if will_rain
    else "No rain expected today."
)
email_message = f"Subject: {subject}\n\n{message_body}"

# إرسال الإيميل مرة واحدة باستخدام with للإغلاق التلقائي
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="mmaherali250@gmail.com",
        msg=email_message.encode("utf-8"),
    )

print("Email sent successfully!")
