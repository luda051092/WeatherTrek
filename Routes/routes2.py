import requests
from flask import Flask, request, jsonify
from user_management import register_user, get_user_details, add_comment

app = Flask(__name__)

WEATHER_API_KEY = ''
WEATHER_API_URL = 'https://api.tomorrow.io/v4/weather/realtime'

@app.route('/current_weather')
def get_current_weather():
    latitude = request.args.get('latitude', '42.3478')
    longitude = request.args.get('longitude', '-71.0828')

    params = {
        'location': '42.3478,-71.0828',
        'apikey': WEATHER_API_KEY,
    }

    response = requests.get(WEATHER_API_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        print(f"Request URL: {response.url}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Weather Data: {weather_data}")

        # Example: Parsing the data to extract relevant information
        temperature = weather_data.get("temperature", "N/A")
        humidity = weather_data.get("humidity", "N/A")
        weather_condition = weather_data.get("weatherCode", "N/A")

      # Create a structured response
        formatted_response = {
            "temperature": temperature,
            "humidity": humidity,
            "weather_condition": weather_condition,
        }

        return jsonify(formatted_response)
    else:
        return jsonify({"error": f"Failed to fetch data. Status code: {response.status_code}"})
    
  # Route to fetch historical weather data
@app.route('/api/historic_weather')
def get_historic_weather():
    # Extract parameters from the request
    latitude = request.args.get('latitude', '52.52')
    longitude = request.args.get('longitude', '13.41')
    start_date = request.args.get('start_date', '2024-02-10')
    end_date = request.args.get('end_date', '2024-02-24')
    
    # Construct the URL for the API request
    api_url = f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m"

    # Make a GET request to the API
    response = requests.get(api_url)

    if response.status_code == 200:
        # Extract the historical weather data from the response
        weather_data = response.json()

        # Return the weather data as JSON
        return jsonify(weather_data)
    else:
        # Return an error message if the request fails
        return jsonify({"error": "Failed to fetch historical weather data"}), response.status_code
  
    
    
@app.route('/api/users', methods=['POST'])
def user_registration():
    # Logic to handle user registration
    data = request.json
    result, status_code = register_user(data)
    # Validate and store user data (e.g., in a database)
    return jsonify(result), status_code

# New route to get user details
@app.route('/api/users/<user_id>')
def user_details(user_id):
    # Logic to fetch user details based on user_id
    user_details = get_user_details(user_id)
    return jsonify(user_details)

# New route to handle user comments
@app.route('/api/comments', methods=['POST'])
def comment():
    # Logic to handle user comments
    data = request.json
    result = add_comment(data)
    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)
