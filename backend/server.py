from fastapi import FastAPI, Request
from fastapi_utils.tasks import repeat_every
from fastapi.middleware.cors import CORSMiddleware
import requests
import uvicorn
import json
from datetime import datetime
from constants import CORS_URLS
from bitcoin_timestamp import BitcoinTimestamp
from custom_util import get_live_bitcoin_price, convert_date_to_text
from database_connection import DatabaseConnection

# TODO (3.1): define FastAPI app
app = FastAPI()

# TODO (5.4.1): define database connection
db = DatabaseConnection()

# TODO (3.2): add CORS middleware
app.add_middleware(CORSMiddleware, allow_origins=CORS_URLS,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# TODO (3.1)
"""
a index function to test if server is running
"""
@app.get("/")
async def root():
    content = {"message": "Hello World! This is a bitcoin monitoring service!"}
    return json.dumps(content)

# TODO (5.4.2)
"""
repeated task to update bitcoin prices periodically
"""
@repeat_every(seconds=300)
def update_bitcoin_price() -> None:
    print("Getting new price....")
    # get live bitcoin price
    try:
        price = get_live_bitcoin_price()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching live bitcoin price: {e}")
        return
    
    # insert timestamp with current time and price into database
    timestamp = convert_date_to_text(datetime.now())
    db.insert_timestamp(BitcoinTimestamp(timestamp, price))

# TODO (5.4.3)
"""
API endpoint to get bitcoin prices

:return:
    a list of bitcoinstamps
:rtype:
    json
"""
@app.get("/bitcoin_prices")
def get_bitcoin_prices() -> str:
    # get all bitcoin timestamps from the database and return
    return json.dumps(db.get_all_timestampes())

# main function to run the server
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
