import folium
import json

# Define GeoJSON data for early Church Fathers and writings
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "Didache",
                "date": "80-90 AD",
                "description": "An early Christian treatise from Syria.",
            },
            "geometry": {"type": "Point", "coordinates": [38.9968, 34.8021]},
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Clement of Rome",
                "date": "96 AD",
                "description": "Bishop of Rome and author of 1 Clement.",
            },
            "geometry": {"type": "Point", "coordinates": [12.4964, 41.9028]},
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Ignatius of Antioch",
                "date": "110 AD",
                "description": "Bishop of Antioch and martyr.",
            },
            "geometry": {"type": "Point", "coordinates": [36.1619, 36.2043]},
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Papias of Hierapolis",
                "date": "100-125 AD",
                "description": "Bishop of Hierapolis, Asia Minor.",
            },
            "geometry": {"type": "Point", "coordinates": [29.1232, 37.9249]},
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Polycarp of Smyrna",
                "date": "110-140 AD",
                "description": "Bishop of Smyrna and martyr.",
            },
            "geometry": {"type": "Point", "coordinates": [27.1428, 38.4237]},
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Justin Martyr",
                "date": "155 AD",
                "description": "Christian apologist in Rome.",
            },
            "geometry": {"type": "Point", "coordinates": [12.4964, 41.9528]},
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Muratorian Canon Fragment",
                "date": "170 AD",
                "description": "Earliest list of New Testament books.",
            },
            "geometry": {"type": "Point", "coordinates": [12.4964, 41.9928]},
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Irenaeus of Lyons",
                "date": "180 AD",
                "description": "Bishop of Lyons and opponent of Gnosticism.",
            },
            "geometry": {"type": "Point", "coordinates": [4.8357, 45.7640]},
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Clement of Alexandria",
                "date": "180 AD",
                "description": "Christian theologian in Alexandria.",
            },
            "geometry": {"type": "Point", "coordinates": [29.9187, 31.2001]},
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Tertullian of Carthage",
                "date": "208 AD",
                "description": "Christian apologist and theologian.",
            },
            "geometry": {"type": "Point", "coordinates": [10.2307, 36.8625]},
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Sarapion of Antioch",
                "date": "199-211 AD",
                "description": "Bishop of Antioch.",
            },
            "geometry": {"type": "Point", "coordinates": [36.1619, 35.5]},
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Origen of Alexandria",
                "date": "248-250 AD",
                "description": "Prolific Christian scholar and theologian.",
            },
            "geometry": {"type": "Point", "coordinates": [29.9187, 30.2001]},
        },
        {
            "type": "Feature",
            "properties": {
                "name": "Celsus the Heretic",
                "date": "248 AD",
                "description": "Critic of Christianity, associated with Gaul.",
            },
            "geometry": {"type": "Point", "coordinates": [4.8357, 45.9640]},
        },
    ],
}

# Create a Folium map centered on the Mediterranean
m = folium.Map(location=[35, 15], zoom_start=4)

# Add points from the GeoJSON data to the map
for feature in geojson_data["features"]:
    coords = feature["geometry"]["coordinates"]
    props = feature["properties"]
    folium.Marker(
        location=[coords[1], coords[0]],  # Note: Folium uses [latitude, longitude]
        popup=f"<b>{props['name']}</b><br>{props['date']}<br>{props['description']}",
    ).add_to(m)

# Save the map to an HTML file
m.save("early_church_map.html")

print("Map saved as 'early_church_map.html'. Open it in your browser to view.")
