import json

# opens geojson file
with open(r"uk_districts.geojson", "r", encoding="utf-8") as f:  # modify file path for data input
    uk_geojson = json.load(f)
