import unittest
from unittest.mock import patch, MagicMock
from app import db, HistoricWeather
from scripts.fetch_and_populate_historical_weather import fetch_and_populate_historical_weather

class TestFetchAndPopulateHistoricalWeather(unittest.TestCase):

    @patch('scripts.fetch_and_populate_historical_weather.requests.get')
    def test_fetch_and_populate_historical_weather_success(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                'city_id': 1,
                'weather_condition_id': 1,
                'temperature': 20.0,
                'humidity': 65.0,
                'wind_speed': 4.0,
                'precipitation': 0.0,
                'timestamp': '2024-02-27 12:00:00'
            },
        
        ]
        mock_requests_get.return_value = mock_response

        fetch_and_populate_historical_weather()

        # Verify that the data is inserted into the HistoricWeather table
        historical_weather = HistoricWeather.query.all()
        self.assertEqual(len(historical_weather), 1)  # Adjust 
        self.assertEqual(historical_weather[0].city_id, 1)  # Adjust 

    @patch('scripts.fetch_and_populate_historical_weather.requests.get')
    def test_fetch_and_populate_historical_weather_failure(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 404  # Simulate a failure status code
        mock_requests_get.return_value = mock_response

        # Call the function and check if an error message is printed
        with patch('builtins.print') as mock_print:
            fetch_and_populate_historical_weather()
            mock_print.assert_called_with(f"Failed to fetch data from API. Status code: 404")

if __name__ == '__main__':
    unittest.main()
