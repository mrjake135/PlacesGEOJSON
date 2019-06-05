import googlemaps
from mapbox import Datasets
import json
from geojson import MultiPoint
#creates a geojson multipoint file using a google maps, but only parses maximum 20 searches
gmaps = googlemaps.Client(key='')#PUT YOUR GOOGLE API KEY HERE
places_result = gmaps.places_nearby(location = '33.775620, -84.396286', radius = 1000, type = 'restaurant')
# myplace_locations = {}
myplace_locations = []
counter = 0
for place in places_result['results']:
    myplace_id = place['id']
    myplace_name = place['name']
    myplace_lat = place['geometry']['location']['lat'] #Scrape the Lattitude
    myplace_lng = place['geometry']['location']['lng'] #Scrape the Longitude
    myplace_location = (myplace_lng,myplace_lat)
    # myplace_locations[myplace_name] = myplace_location
    myplace_locations.append(myplace_location)

print(myplace_locations)
geojsonFeature = {
    "type": "Feature",
    "properties": {
        "name": "Restaurants",
    },
    "geometry": {
        "type": "MultiPoint",
        "coordinates": myplace_locations
    }
}
print(geojsonFeature)
with open ('places.json', 'w') as f:
    json.dump(geojsonFeature, f)
    print('GEOJSON saved')