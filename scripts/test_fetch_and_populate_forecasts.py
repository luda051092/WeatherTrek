import unittest
from unittest.mock import patch, MagicMock
from app import db, Forecast
from scripts.fetch_and_populate_forecasts import fetch_and_populate_forecasts

class TestFetchAndPopulateForecasts(unittest.TestCase):

    @patch('scripts.fetch_and_populate_forecasts.requests.get')
    def test_fetch_and_populate_forecasts_success(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                'city_id': 1,
                'weather_condition_id': 1,
                'temperature': 25.5,
                'feels_like': 26.0,
                'humidity': 60.0,
                'wind_speed': 5.0,
                'precipitation': 0.0,
                'timestamp': '2024-02-28 12:00:00'
            },
            
        ]
        mock_requests_get.return_value = mock_response

        fetch_and_populate_forecasts()

        # Verify that the data is inserted into the Forecast table
        forecasts = Forecast.query.all()
        self.assertEqual(len(forecasts), 1)  # Adjust based on the number of forecasts in the mock data
        self.assertEqual(forecasts[0].city_id, 1)  # Adjust based on the mock data

    @patch('scripts.fetch_and_populate_forecasts.requests.get')
    def test_fetch_and_populate_forecasts_failure(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 404  # Simulate a failure status code
        mock_requests_get.return_value = mock_response

        # Call the function and check if an error message is printed
        with patch('builtins.print') as mock_print:
            fetch_and_populate_forecasts()
            mock_print.assert_called_with(f"Failed to fetch data from API. Status code: 404")

if __name__ == '__main__':
    unittest.main()
