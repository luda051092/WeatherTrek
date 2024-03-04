
import requests
from app import db, HistoricWeather

API_URL = 'https://api.historicalweatherprovider.com/v1/historical'
API_KEY = 'API_KEY'  # Replace with API key

def fetch_and_populate_historical_weather():
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        historical_weather_data = response.json()

        # Loop through the data and insert into the HistoricWeather table
        for weather_data in historical_weather_data:
            historic_weather = HistoricWeather(
                city_id=weather_data['city_id'],
                weather_condition_id=weather_data['weather_condition_id'],
                temperature=weather_data['temperature'],
                humidity=weather_data.get('humidity'),
                wind_speed=weather_data.get('wind_speed'),
                precipitation=weather_data.get('precipitation'),
                timestamp=weather_data['timestamp']
            )
            db.session.add(historic_weather)

        db.session.commit()
        print("Historical weather data successfully fetched and inserted into the database.")
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")

if __name__ == '__main__':
    fetch_and_populate_historical_weather()
