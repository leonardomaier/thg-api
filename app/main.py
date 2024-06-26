import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import urlencode
from .utils import extract_population_by_year

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_URL = 'https://datausa.io/api/data'

@app.get("/")
async def home():
    return { 'message': "API is up and running" }

@app.get("/population")
async def get_population():
    try:
        params = {
            'drilldowns': 'State',
            'measures': 'Population',
            'geo': '04000US01,04000US12,04000US06'
        }

        query_string = urlencode(params)

        response = requests.get(f'{API_URL}?{query_string}')
        response.raise_for_status()

        json = response.json()

        result = extract_population_by_year(json["data"])

        return { 'data': result }
    except requests.RequestException as e:
        raise HTTPException(status_code=503, detail="Error fetching data from external API")

@app.get("/cars-per-household")
async def get_cars_per_household():
    try:
        params = {
            'measure': 'Commute Means by Gender,Commute Means by Gender Moe',
            'geo': '01000US,01000US',
            'drilldowns': 'Vehicles Available',
            'year': 2021
        }

        query_string = urlencode(params)

        response = requests.get(f'{API_URL}?{query_string}')
        response.raise_for_status()

        json = response.json()

        result = { 'labels': [], 'quantity': [] }

        for row in json['data']:
            vehicles_avaiable = row['Vehicles Available']
            vehicles_quantity = row['Commute Means by Gender']

            result['labels'].append(vehicles_avaiable)
            result['quantity'].append(vehicles_quantity)

        return { "data": result }
    except requests.RequestException as e:
            raise HTTPException(status_code=503, detail="Error fetching data from external API")
