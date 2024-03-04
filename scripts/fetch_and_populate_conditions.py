
import requests
from app import db, WeatherCondition

API_URL = 'https://api.weatherprovider.com/v1/weather_conditions'
API_KEY = 'API_KEY'  # Replace with API key

def fetch_and_populate_conditions():
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        conditions_data = response.json()

        # Loop through the data and insert into the WeatherCondition table
        for condition_data in conditions_data:
            condition = WeatherCondition(
                condition_name=condition_data['condition_name'],
                description=condition_data['description'],
                icon_url=condition_data['icon_url']
            )
            db.session.add(condition)

        db.session.commit()
        print("Weather conditions data successfully fetched and inserted into the database.")
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")

if __name__ == '__main__':
    fetch_and_populate_conditions()
