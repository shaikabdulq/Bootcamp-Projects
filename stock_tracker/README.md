
# Stock News Alert System

## Overview
This project is a Python-based system that monitors stock price changes and sends news alerts via SMS. It focuses on tracking significant price movements in specific stocks and then gathers relevant news articles to keep the user informed.

## Components
The project consists of four main files:

### 1. `main.py`
- **Purpose**: Central script that orchestrates the stock monitoring and alerting process.
- **Functionality**:
  - Defines stock symbol and company name for monitoring.
  - Calls `price_change` to check for significant stock price changes.
  - Fetches news using `get_news` if a significant change is detected.
  - Formats and sends an SMS with stock change and news headlines using `send_sms`.

### 2. `price_change.py`
- **Purpose**: Monitors stock price changes.
- **Functionality**:
  - Connects to Alpha Vantage API for daily stock data.
  - Checks for 5% or more price changes between the past two days.
  - Returns the change percentage and type (increase/decrease).

### 3. `get_news.py`
- **Purpose**: Fetches news articles for a specified company.
- **Functionality**:
  - Connects to NewsAPI.
  - Retrieves top three news pieces related to the company.
  - Filters news by language and author presence.
  - Returns news headlines and briefs.

### 4. `send_sms.py`
- **Purpose**: Sends SMS alerts.
- **Functionality**:
  - Utilizes Twilio API for sending SMS.
  - Sends a message including stock price change and news headlines.
  - Returns the message SID as a confirmation.


## Functionality
- **Stock Price Monitoring**: Detects a 5% or more change in the stock price between yesterday and the day before yesterday.
- **News Fetching**: Retrieves the latest news articles related to the specified company.
- **SMS Alerts**: Sends an SMS to the user with the stock price change and relevant news headlines.

## Setup and Execution
1. Ensure all dependencies are installed.
2. Set the desired stock symbol in `main.py`.
3. Schedule `main.py` to run daily at a specific time (e.g., 6 PM) using a task scheduler.

## Dependencies
- `requests`
- `datetime`
- `dateutil`
- `langdetect`
- `twilio`

## External APIs
- Alpha Vantage for stock price data - [link](https://www.alphavantage.co/)
- NewsAPI.org for fetching news articles - [link](https://newsapi.org/)
- Twilio API for sending SMS alerts - [link](https://www.twilio.com/en-us/messaging/channels/sms)

## Usage

1. **Manual:** Run `main.py` manually whenever you want to check for stock price changes and send an alert if necessary.

2. **Automated Scheduling:** Schedule `main.py` to run at your desired time, preferably after the stock market's closing time using the **Windows Task Scheduler**. For detailed instrcutions, click [here](https://info.eaglebusinesssoftware.com/support/help_modules/84/EBMS%20Main%20Documentation/Automate_using_Windows_Scheduler.htm)

## Note
Ensure API keys and Twilio account details are set correctly in the respective files.
