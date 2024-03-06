import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ' 

WEATHER_API_KEY = ''
WEATHER_API_URL = 'https://api.tomorrow.io/v4/weather/realtime'

@app.route('/current_weather')
def get_current_weather():
    latitude = request.args.get('latitude', '42.3478')
    longitude = request.args.get('longitude', '-71.0828')

    params = {
        'location': f'{latitude},{longitude}',
        'apikey': WEATHER_API_KEY,
        'fields': 'temperature,humidity,weatherCode,windSpeed,windDirection,uvIndex',  # Adjust if/as necessary
    }

    response = requests.get(WEATHER_API_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json().get("data", {}).get("instant", {}).get("details", {})

        print(f"Request URL: {response.url}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Weather Data: {weather_data}")

        # Example: Parsing the data to extract relevant information
        temperature = weather_data.get("temperature", "N/A")
        humidity = weather_data.get("humidity", "N/A")
        weather_condition = weather_data.get("weatherCode", "N/A")
        wind_speed = weather_data.get("windSpeed", "N/A")
        wind_direction = weather_data.get("windDirection", "N/A")
        uv_index = weather_data.get("uvIndex", "N/A")

        # Create a structured response
        formatted_response = {
            "temperature": temperature,
            "humidity": humidity,
            "weather_condition": weather_condition,
            "wind_speed": wind_speed,
            "wind_direction": wind_direction,
            "uv_index": uv_index,
        }

        return jsonify(formatted_response)
    else:
        return jsonify({"error": f"Failed to fetch data. Status code: {response.status_code}"})
    
    # Comment model:
    class Comment(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, nullable=False)
        comment_text = db.Column(db.String(255), nullable=False)
        timestamp = db.Column(db.DateTime, nullable=False, default=datetime=utcnow)

if __name__ == '__main__':
    app.run(debug=True)
