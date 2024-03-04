import unittest
from unittest.mock import patch, MagicMock
from app import db, WeatherCondition
from scripts.fetch_and_populate_conditions import fetch_and_populate_conditions

class TestFetchAndPopulateConditions(unittest.TestCase):

    @patch('scripts.fetch_and_populate_conditions.requests.get')
    def test_fetch_and_populate_conditions_success(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                'condition_name': 'Clear',
                'description': 'Clear sky',
                'icon_url': 'https://ex.com/clear.png'
            },
        
        ]
        mock_requests_get.return_value = mock_response

        fetch_and_populate_conditions()

        # Verify that the data is inserted into the WeatherCondition table
        conditions = WeatherCondition.query.all()
        self.assertEqual(len(conditions), 1)  # Adjust this
        self.assertEqual(conditions[0].condition_name, 'Clear')  # Adjust this

    @patch('scripts.fetch_and_populate_conditions.requests.get')
    def test_fetch_and_populate_conditions_failure(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 404  # Simulate a failure status code
        mock_requests_get.return_value = mock_response

        # Call the function and check if an error message is printed
        with patch('builtins.print') as mock_print:
            fetch_and_populate_conditions()
            mock_print.assert_called_with(f"Failed to fetch data from API. Status code: 404")

if __name__ == '__main__':
    unittest.main()
