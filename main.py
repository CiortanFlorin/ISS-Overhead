import requests
import smtplib
from datetime import datetime
import time
MY_LAT = -27.507351 # Your latitude
MY_LONG = -46.127758 # Your longitude

email = "YOUR EMAIL"
password = "YOUR EMAIL Password"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_longitude)
print(iss_latitude)
#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
print(sunrise)
print(sunset)
print(time_now.hour)
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while int(iss_latitude) in range(int(MY_LAT-5), int(MY_LAT+6)) and int(iss_longitude) in range(int(MY_LONG-5), int(MY_LONG+6)) and time_now.hour > sunset or time_now.hour < sunrise:
    with smtplib.SMTP("smtp.gmail.com") as s:
        s.starttls()
        s.login(user=email, password=password)
        text = "LOOK UP"
        s.sendmail(from_addr=email, to_addrs="RECIPIENT EMAIL", msg=f"Subject: ISS AHEAD\n\n{text}")
    time.sleep(60)
