import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
# from twilio.http.http_client import TwilioHttpClient

load_dotenv()

end_point = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "AC5e8e50e8f1184c43c4ee0519045522ab"
auth_token = os.environ.get("AUTH_TOKEN")
contact_list = os.environ.get("CONTACT_LIST")
from_number = os.environ.get("FROM_NUMBER")


params = {
    "lat": 38.015305,
    "lon": -7.862731,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(end_point, params=params)
response.raise_for_status()
data = response.json()["list"]

will_rain = False

for call in data:
    weather_code = call["weather"][0]["id"]

    if weather_code < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    to_numbers = [contact_list]

    for number in to_numbers:
        client = Client(account_sid, auth_token)  # ADD 'http_client=proxy_client' here
        message = client.messages \
            .create(
                body="Will rain today! Don't forget to bring your umbrella! ☂️",
                from_=from_number,
                to=number
            )
        print(message.status)
