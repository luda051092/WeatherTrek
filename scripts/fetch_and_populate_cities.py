
import requests
from app import db, City

API_URL = 'https://api.api-ninjas.com/v1/city'
API_KEY = 'API_KEY'  # Replace with the actual API key

def fetch_and_populate_cities():
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        cities_data = response.json()

        # Loop through the data and insert into the City table
        for city_data in cities_data:
            city = City(
                name=city_data['name'],
                country=city_data['country'],
                population=city_data['population'],
                region=city_data['region'],
                latitude=city_data['latitude'],
                longitude=city_data['longitude'],
                elevation=city_data['elevation']
            )
            db.session.add(city)

        db.session.commit()
        print("Cities data successfully fetched and inserted into the database.")
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")

if __name__ == '__main__':
    fetch_and_populate_cities()
