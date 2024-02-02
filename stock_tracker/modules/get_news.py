## STEP 2: Use https://newsapi.org
# Get the first 3 news pieces for the COMPANY_NAME.

import datetime
from dateutil.relativedelta import relativedelta
import requests
import langdetect

def get_news(company_name):
    #Get one-month ago date
    today = datetime.date.today()
    one_month_ago = str(today - relativedelta(months=1))

    #Do API call to newsapi.org to GET news data in json
    news_endpoint = "https://newsapi.org/v2/everything"
    news_params = {
        "apiKey" : "ENTER_API_KEY",
        "q" : company_name,
        "searchIn" : "title",
    }
    r = requests.get(news_endpoint, params=news_params)
    data = r.json()
    # Gets the latest 3 news articles (english only) and returns a list of these headlines
    articles = data["articles"]
    count = 0
    list = []
    for article in articles:
        author = article['author']
        if author == "null":
            continue
        text = article["title"]
        language = langdetect.detect(text)
        if language != "en":
            continue
        headline = ''
        brief = ''
        headline = "Headline: " + article["title"]
        brief = "Brief:" + article["description"]
        news = "\n" + headline + "\n" + brief
        count = count + 1
        if count == 4:
            break
        list.append(news)
    return list

