from fastapi import FastAPI, Query
import requests

app = FastAPI()

# Search tempat pakai Nominatim (OpenStreetMap)
@app.get("/search_places")
def search_places(query: str, city: str = "Jakarta"):
    url = f"https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"{query}, {city}",
        "format": "json",
        "addressdetails": 1,
        "limit": 5
    }
    response = requests.get(url, params=params, headers={"User-Agent": "maps-llm-demo"}).json()
    return response

# Directions pakai OSRM (Open Source Routing Machine)
@app.get("/directions")
def get_directions(origin: str, destination: str, mode: str = "driving"):
    # origin & destination = "lat,lon"
    url = f"http://router.project-osrm.org/route/v1/{mode}/{origin};{destination}?overview=full&geometries=geojson"
    response = requests.get(url).json()
    return response
