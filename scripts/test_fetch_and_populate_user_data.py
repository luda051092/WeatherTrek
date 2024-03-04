import unittest
from unittest.mock import patch, MagicMock
from app import db, User
from scripts.fetch_and_populate_user_data import fetch_and_populate_user_data

class TestFetchAndPopulateUserData(unittest.TestCase):

    @patch('scripts.fetch_and_populate_user_data.requests.get')
    def test_fetch_and_populate_user_data_success(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                'user_id': 1,
                'username': 'test_user',
                
            },
        
        ]
        mock_requests_get.return_value = mock_response

        fetch_and_populate_user_data()

        # Verify that the data is inserted into the User table
        users = User.query.all()
        self.assertEqual(len(users), 1)  # Adjust based on the number of user entries in the mock data
        self.assertEqual(users[0].user_id, 1)  # Adjust based on the mock data

    @patch('scripts.fetch_and_populate_user_data.requests.get')
    def test_fetch_and_populate_user_data_failure(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 404  # Simulate a failure status code
        mock_requests_get.return_value = mock_response

        # Call the function and check if an error message is printed
        with patch('builtins.print') as mock_print:
            fetch_and_populate_user_data()
            mock_print.assert_called_with(f"Failed to fetch data from API. Status code: 404")

if __name__ == '__main__':
    unittest.main()
