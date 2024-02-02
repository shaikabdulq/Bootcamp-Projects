## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then returns "Get News"

## Stock exchange opens at 7PM and closes at 1:30AM. So, program should run at 6PM daily
## To run the program, we'll use 'Task Scheduler' in windows which runs the 'main' program once daily at 6PM


import requests

def price_change(stock):

    # Get JSON data from Time Series Daily API
    link = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="
    url = link + stock + '&apikey=ENTER_API_KEY'
    r = requests.get(url)
    data = r.json()
    # Get yesterday's and day-before-yesterday's close price
    time_series_daily = data["Time Series (Daily)"]
    count = 0
    for day in time_series_daily:
        count = count+1
        if count == 1:
            yest_close_price = float(time_series_daily[day]["4. close"])
        elif count == 2:
            day_before_close_price = float(time_series_daily[day]["4. close"])
        else:
            break

    # Prints "Get News" if difference between close of two days is more than 5%
    difference = yest_close_price - day_before_close_price
    if difference > 0:
        change = "increase"
    else:
        change = "decrease"
    change_percent = abs(difference) / day_before_close_price * 100 ## abs always gives positive value
    return {"change": change, "change_percent": change_percent, "data": data}

