
import requests
from app import db, User

API_URL = 'https://api.userdataprovder.com/v1/userdata'
API_KEY = 'API_KEY'  # Replace with API key

def fetch_and_populate_user_data():
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        user_data = response.json()

        # Loop through the data and insert into the User table
        for data in user_data:
            user = User(
                user_id=data['user_id'],
                username=data['username'],
                # Add more user-related fields as needed
            )
            db.session.add(user)

        db.session.commit()
        print("User data successfully fetched and inserted into the database.")
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")

if __name__ == '__main__':
    fetch_and_populate_user_data()
