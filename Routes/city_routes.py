import requests

def get_city_data(api_key, city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        city_data = response.json()
        return city_data
    else:
        print(f"Failed to fetch data for {city_name}. Status code: {response.status_code}")
        return None

# Usage
api_key = "KEY"
city_name = input("Enter the city name: ")
city_data = get_city_data(api_key, city_name)

if city_data:
    print(f"City Name: {city_data['name']}")
    print(f"Country: {city_data['sys']['country']}")
    print(f"Population: {city_data['population']}")
    print(f"Latitude: {city_data['coord']['lat']}")
    print(f"Longitude: {city_data['coord']['lon']}")
    
