
import requests
from app import db, Forecast

API_URL = 'https://api.weatherforecastprovider.com/v1/forecasts'
API_KEY = 'API_KEY'  # Replace with API key

def fetch_and_populate_forecasts():
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        forecasts_data = response.json()

        # Loop through the data and insert into the Forecast table
        for forecast_data in forecasts_data:
            forecast = Forecast(
                city_id=forecast_data['city_id'],
                weather_condition_id=forecast_data['weather_condition_id'],
                temperature=forecast_data['temperature'],
                feels_like=forecast_data.get('feels_like'),
                humidity=forecast_data.get('humidity'),
                wind_speed=forecast_data.get('wind_speed'),
                precipitation=forecast_data.get('precipitation'),
                timestamp=forecast_data['timestamp']
            )
            db.session.add(forecast)

        db.session.commit()
        print("Forecast data successfully fetched and inserted into the database.")
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")

if __name__ == '__main__':
    fetch_and_populate_forecasts()
