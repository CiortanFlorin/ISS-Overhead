Link to project: https://github.com/ciortan123/ISS-Overhead

ISS coordinates API address: http://api.open-notify.org/iss-now.json

Sunrise-Sunset API address: https://api.sunrise-sunset.org/json

How the project works:

-Using the ISS coordinates API, we check every minute for the coordinates of the ISS

-Using the Sunrise-Sunset API we check if it is nighttime at our location

-If both conditions are met, then we send an email to ourselves with the message that the ISS is visible from our location. The e-mail is being sent using SMTPLIB
