import unittest
from unittest.mock import patch, MagicMock
from app import db, City
from scripts.fetch_and_populate_cities import fetch_and_populate_cities

class TestFetchAndPopulateCities(unittest.TestCase):

    @patch('scripts.fetch_and_populate_cities.requests.get')
    def test_fetch_and_populate_cities_success(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                'name': 'City1',
                'country': 'Country1',
                'population': 1000000,
                'region': 'Region1',
                'latitude': 40.7128,
                'longitude': -74.0060,
                'elevation': 10.5
            },
            
        ]
        mock_requests_get.return_value = mock_response

        fetch_and_populate_cities()

        # Verify that the data is inserted into the City table
        cities = City.query.all()
        self.assertEqual(len(cities), 1)  # Adjust based on the number of cities in the mock data
        self.assertEqual(cities[0].name, 'City1')  # Adjust based on the mock data

    @patch('scripts.fetch_and_populate_cities.requests.get')
    def test_fetch_and_populate_cities_failure(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 404  # Simulate a failure status code
        mock_requests_get.return_value = mock_response

        # Call the function and check if an error message is printed
        with patch('builtins.print') as mock_print:
            fetch_and_populate_cities()
            mock_print.assert_called_with(f"Failed to fetch data from API. Status code: 404")

if __name__ == '__main__':
    unittest.main()
