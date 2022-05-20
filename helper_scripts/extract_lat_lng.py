import os
import pandas as pd
from opencage.geocoder import OpenCageGeocode

api_key = 'ab6833b017cd4ee4a27dff46ceee2363'
geocoder = OpenCageGeocode(api_key)

all_files = os.listdir('original_data_files')
all_files = [f for f in all_files if f[-3:] == 'csv' and f != 'geo_position.csv']

all_cities = []
for file in all_files:
    city = file.split(',', 1)[0]
    city = city.replace('+', ' ')
    all_cities.append(city)

file_name = 'data/geo_position.csv'
if os.path.exists(file_name):
    file_mode = 'a'
    df = pd.read_csv(file_name)
    existing_cities = list(df['CITY'])
    all_cities = [x for x in all_cities if x not in existing_cities]
    print('Remaining cities to be completed:')
    print(all_cities)
else:
    file_mode = 'w'

max_len = len(all_cities)
with open(file_name, file_mode) as f:
    f.write('CITY,LAT,LNG')
    for i, city in enumerate(all_cities):
        query = f'{city}, Croatia'
        results = geocoder.geocode(query)
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        print(f'{i + 1}/{max_len}:  {city}')
        f.write("\n")
        f.write(f'{city},{lat},{lng}')
