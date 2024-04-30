import requests
from datetime import date, timedelta
from twilio.rest import Client

yesterday = date.today() - timedelta(days=2)
the_day_before_yesterday = date.today() - timedelta(days=3)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = 'ursid'
auth_token = 'urtoken'
client = Client(account_sid, auth_token)


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

STOCK_INFO = {
    "symbol": "TSLA",
    "apikey": "urapikey",
    "function": "TIME_SERIES_DAILY",
    "outputsize": "compact"
}

NEWS_INFO = {
    "q": "tesla",
    "from": yesterday,
    "to": yesterday,
    "apiKey": "urapikey",
    "pageSize": 3
}

news = []
def calculate_percent_change(x, y):
    return ((x/y)*100)-100

response_stock = requests.get(STOCK_ENDPOINT, params=STOCK_INFO)
data_stock = response_stock.json()

#3 new news about tesla
response_news = requests.get(NEWS_ENDPOINT, params=NEWS_INFO)
response_news.raise_for_status()
data_news = response_news.json()["articles"]
for item in data_news:
    news.append(f"Headline: {item["title"]} \nBrief: {item["description"]}")
yesterday_endpoint = float(data_stock["Time Series (Daily)"][str(yesterday)]["4. close"])
day_before_endpoint = float(data_stock["Time Series (Daily)"][str(the_day_before_yesterday)]["4. close"])

if calculate_percent_change(yesterday_endpoint,day_before_endpoint) > 0.05:
        message=client.messages.create(
            body=f"Between yesterday and the day before yesterday: {calculate_percent_change(yesterday_endpoint,day_before_endpoint)}\n{news}",
            from_='+12184137232',
            to='+48579316607'
        )







