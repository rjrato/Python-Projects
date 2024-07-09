import requests
import os
import datetime
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

CRYPTO = "BTC"
NAME = "Bitcoin"
CRYPTO_DATA_END_POINT = "https://www.alphavantage.co/query"
NEWS_DATA_ENDPOINT = "https://newsapi.org/v2/everything"

# GET CRYPTO DATA
crypto_api_params = {
    "function": "DIGITAL_CURRENCY_WEEKLY",
    "symbol": CRYPTO,
    "market": "USD",
    "apikey": os.environ.get("DIGITAL_CURRENCY_API_KEY")
}

crypto_api_response = requests.get(CRYPTO_DATA_END_POINT, params=crypto_api_params)
crypto_api_response.raise_for_status()
crypto_data = crypto_api_response.json()["Time Series (Digital Currency Weekly)"]

# Convert data to list to access previous week closing price
data_list = [date for date in crypto_data.items()]

year = datetime.date.today().year
month = datetime.date.today().month
today = datetime.date.today().isoformat()
last_week_end = crypto_data[data_list[2][0]]

today_open_price = float(crypto_data[today]["1a. open (USD)"])
last_week_closing_price = float(crypto_data[data_list[2][0]]["4a. close (USD)"])

price_difference = round((today_open_price - last_week_closing_price), 2)
percentage = 100 - round(last_week_closing_price * 100 / today_open_price, 2)
up_down = None

if percentage > 5:
    up_down = "🔺"
else:
    up_down = "🔻"

if percentage > 5:
    # GET 3 RELEVANT NEWS FROM NEWSAPI
    news_api_params = {
        "q": NAME,
        "from": last_week_end,
        "to": today,
        "language": "en",
        "pageSize": 3,
        "apiKey": os.environ.get("NEWS_API_KEY")
    }

    news_api_response = requests.get(NEWS_DATA_ENDPOINT, params=news_api_params)
    news_api_response.raise_for_status()
    news_data = news_api_response.json()["articles"]

    news = news_data[:3]

    # SEND SMS WITH HEADLINES AND URL'S
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="+19727745859",
        body=f"Bitcoin {up_down} {round(percentage, 1)}%. Check here some relevant news:\n"
             f"1 - {news[0]["title"]}, {news[0]["url"]}\n"
             f"2 - {news[1]["title"]}, {news[1]["url"]}\n"
             f"3 - {news[2]["title"]}, {news[2]["url"]}",
        to="+351964657580"
    )

    print(message.sid)
