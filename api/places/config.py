import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

LIMIT = 20
RECOMMENDATION_LIMIT = 3

url = "https://api.foursquare.com/v3/places/search"

headers = {
    "accept": "application/json",
    "Accept-Language": "ru",
    "Authorization": API_KEY,
}
