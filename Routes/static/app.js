document.addEventListener('DOMContentLoaded', function () {
    console.log('Hello from app.js!');
    // Fetch weather data from Flask API
    fetch('/current_weather?latitude=42.3478&longitude=-71.0828')
        .then(response => response.json())
        .then(data => {
            // Update HTML with weather information
            document.getElementById('temperature').textContent = `Temperature: ${data.temperature}`;
            document.getElementById('humidity').textContent = `Humidity: ${data.humidity}`;
            document.getElementById('weather-condition').textContent = `Weather Condition: ${data.weather_condition}`;    
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);

              // Display error message on the page
              const errorMessageElement = document.createElement('p');
              errorMessageElement.textContent = 'Error fetching weather data. Please try again later.';
              errorMessageElement.style.color = 'red'; // Optionally, style the error message
              document.getElementById('weather-info').appendChild(errorMessageElement);
        });
});