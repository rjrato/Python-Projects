# Stock Trading News Alert

## Overview

This project is a stock trading news alert system that notifies users via SMS when a stock's price changes by 5% or more compared to the last Friday's closing price. It fetches stock data from [Alpha Vantage API](https://www.alphavantage.co/query) and news articles from [News API](https://newsapi.org/v2/everything). The Twilio library is used to send SMS alerts to users with relevant news.

## Features

- Monitors stock price changes.
- Fetches relevant news articles.
- Sends SMS alerts when stock price changes by 5% or more.

## Getting Started

### Prerequisites

- Python 3.x
- Virtual Environment (optional but recommended)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/stock-trading-news-alert.git
    cd stock-trading-news-alert
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. **Alpha Vantage API**:
    - Sign up at [Alpha Vantage](https://www.alphavantage.co/support/#api-key) to get your API key.
    - Set up your API key in the configuration file or environment variables.

2. **News API**:
    - Sign up at [News API](https://newsapi.org/register) to get your API key.
    - Set up your API key in the configuration file or environment variables.

3. **Twilio API**:
    - Sign up at [Twilio](https://www.twilio.com/try-twilio) to get your account SID, auth token, and a phone number.
    - Set up your Twilio credentials in the configuration file or environment variables.

### Usage

1. Update the `config.py` file with your API keys and other configurations.
2. Run the script:
    ```sh
    python main.py
    ```

## Project Structure


Sure thing! Here's a README.md file for your stock trading news alert project:

markdown
Copy code
# Stock Trading News Alert

## Overview

This project is a stock trading news alert system that notifies users via SMS when a stock's price changes by 5% or more compared to the last Friday's closing price. It fetches stock data from [Alpha Vantage API](https://www.alphavantage.co/query) and news articles from [News API](https://newsapi.org/v2/everything). The Twilio library is used to send SMS alerts to users with relevant news.

## Features

- Monitors stock price changes.
- Fetches relevant news articles.
- Sends SMS alerts when stock price changes by 5% or more.

## Getting Started

### Prerequisites

- Python 3.x
- Virtual Environment (optional but recommended)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/stock-trading-news-alert.git
    cd stock-trading-news-alert
    ```

2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. **Alpha Vantage API**:
    - Sign up at [Alpha Vantage](https://www.alphavantage.co/support/#api-key) to get your API key.
    - Set up your API key in the configuration file or environment variables.

2. **News API**:
    - Sign up at [News API](https://newsapi.org/register) to get your API key.
    - Set up your API key in the configuration file or environment variables.

3. **Twilio API**:
    - Sign up at [Twilio](https://www.twilio.com/try-twilio) to get your account SID, auth token, and a phone number.
    - Set up your Twilio credentials in the configuration file or environment variables.

### Usage

1. Update the `config.py` file with your API keys and other configurations.
2. Run the script:
    ```sh
    python main.py
    ```

## Dependencies

- [Alpha Vantage](https://www.alphavantage.co/)
- [News API](https://newsapi.org/)
- [Twilio](https://www.twilio.com/docs/libraries/python)

Install all dependencies using:
```sh
pip install -r requirements.txt
```

## Contributing
Feel free to fork this project, open issues, or submit pull requests. Contributions are welcome!

## Licence
This project is licensed under the MIT Licence

