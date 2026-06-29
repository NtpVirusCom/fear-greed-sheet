import json
import datetime
import cloudscraper
import gspread
from google.oauth2.service_account import Credentials

URL="https://production.dataviz.cnn.io/index/fearandgreed/graphdata"

scraper=cloudscraper.create_scraper()

r=scraper.get(URL)

data=r.json()

score=data["fear_and_greed"]["score"]
rating=data["fear_and_greed"]["rating"]

scope=[
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds=Credentials.from_service_account_file(
    "credentials.json",
    scopes=scope
)

gc=gspread.authorize(creds)

sheet=gc.open("FearGreed").worksheet("CNN")

sheet.update(
    "A2",
    [[
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        score,
        rating
    ]]
)
