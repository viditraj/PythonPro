import requests
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

API_KEY = '<Get your own key from open weather>'
OWC_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall?'
TWILIO_ACC_SID = '<Get your own key from twilio>'
TWILIO_AUTH_KEY = '<Get your own key from twilio>'

OWH_ENDPOINT = 'https://pro.openweathermap.org/data/2.5/forecast/hourly?'

weather_params = {
    "lat": 26.872860,
    "lon": 80.941230,
    "units": "metric",
    "exclude": "minutely,daily",
    "appid": API_KEY
}

response = requests.get(url=OWC_ENDPOINT, params=weather_params)
result = response.json()
weather_data = result["hourly"][:12]
it_will_rain = False  # This variable will be true if it will rain in next 12 hours
for hour in weather_data:
    hourly_weather = hour["weather"]
    condition_code = hourly_weather[0]["id"]
    if int(condition_code) < 700:
        it_will_rain = True
        break
if it_will_rain:
    try:
        client = Client(TWILIO_ACC_SID, TWILIO_AUTH_KEY)

        message = client.messages.create(
            messaging_service_sid='MG4dc6e707f19f8d3ce109f2da23522d47',
            body="Today it will rain ⛈, Bring your umbrella ☔.",
            to='+918604633326'
        )
    except TwilioRestException:
        print("Error Sending SMS")
    else:
        print("SMS sent successfully.")







