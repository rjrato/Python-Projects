# Weather Alert App

A Python application that checks weather forecasts using the OpenWeatherMap API and sends SMS alerts using Twilio if rain is expected.

## Overview

This Python program monitors weather forecasts for a specific location and sends SMS alerts to designated recipients if rain is predicted for the day. It utilizes the OpenWeatherMap API for weather data retrieval and Twilio for SMS messaging.

## Features

- **Weather Forecast**: 
  - Fetches weather data from the OpenWeatherMap API for a predefined location.
  - Checks if rain is forecasted based on weather condition codes.

- **SMS Alerts**: 
  - Sends SMS alerts using Twilio to notify recipients about expected rain.
  - Alerts include a friendly reminder to carry an umbrella.

- **Environment Variables**: 
  - Uses environment variables to securely store API keys, Twilio credentials, and contact list details.

## Installation

1. Ensure Python is installed on your system.
2. Clone the repository and install dependencies:

   ```bash
   pip install -r requirements.txt
    ```
3. Set up environment variables:
    - **"OWN_API_KEY"**: Your OpenWeatherMap API Key.
    - **"AUTH_TOKEN"**: Twillio account authentication token.
    - **"CONTACT_LIST"**: Comma-separated list of recipients phone numbers.
    - **"FROM_NUMBER"**: Twillio phone number used as the sender.
4. Run the application:
    ```bash
    python main.py
   ```

## Dependencies
Just run the following command to install all the required dependencies:
```bash
    pip install -r requirements.txt
   ```
