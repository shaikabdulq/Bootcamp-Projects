from modules.price_change import price_change
from modules.get_news import get_news
from modules.send_sms import send_sms

# Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# Enter which stock you wish to monitor
stock = "AAPL"
company_name = "Apple Inc"

#Checks for price change and if change more than 5%, then creates body for sms
body = ""
try:
    change_percent = int((price_change(stock))['change_percent'])
    change = (price_change(stock))['change']
except:
    print("Sorry! Unable to get Stock Price data")
    quit()
if change == "increase":
    symbol = "🔺"
else:
    symbol = "🔻"
if change_percent > 5 :
    body = stock + ": " + symbol + str(change_percent) + "%" + "\n"
    news = get_news(company_name)
    for i in news:
        body = body + i + '\n'

    #sends body as sms to number provided in twilio account
    send_sms(body)





