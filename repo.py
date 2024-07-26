import csv
import requests
import math
from math import cos, asin, sqrt


def read_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def get_zipcode_coordinates(zipcode):
    #hard coded api key for now 
    url=f'https://api.zipcodestack.com/v1/search?codes={zipcode}&country=us&apikey=01J3NDBCR8J9QF614DHHN8B048'

    response=requests.get(url)
    data=response.json()
    results=data['results']
    if len(results)==0:
        return None,None
    result=data['results'][zipcode]
    if not result:
        return None,None
    #get lat and lon
    if not result[0]:
        return None,None
    return result[0]['latitude'],result[0]['longitude']


class FoodData:

    # reading food data from csv
    def __init__(self, data):
        self.data = read_csv('csv/Mobile_Food_Facility_Permit.csv')
        self.data = [dict(zip(self.data[0], row)) for row in self.data]
        self.data = self.data[1:]





class FoodRepository:

    def __init__(self):
        self.data = FoodData(self)

    def get_distance(self,lat1,lon1,lat2,lon2):
        p = 0.017453292519943295
        a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
        return 12742 * asin(sqrt(a))
    
    def get_items_length(self):
        return len(self.data.data)
    
    def get_by_location(self,location):
        temp_data=self.data.data
        temp_data=[item for item in temp_data if item['address'].lower().find(location.lower())!=-1]
        return temp_data

    def get_all_food(self,start=0,limit=24,q='',zipcode='', max_distance=4):
        temp_data=self.data.data

        if zipcode:
            lat,lon=get_zipcode_coordinates(zipcode)
            #get food items within 40 miles of zipcode
            if not lat or not lon:
                temp_data=[]
            else:
                temp_data = sorted(
                        [item for item in temp_data if self.get_distance(lat, lon, float(item['lat']), float(item['lon'])) <= max_distance],
                        key=lambda x: self.get_distance(lat, lon, float(x['lat']), float(x['lon']))
                    )

        if q:
            temp_data=[item for item in temp_data if item['applicant'].lower().find(q.lower())!=-1]
        return temp_data[start:start+limit]

    #find where id is equals to cnn

    def get_food_by_id(self, cnn):
        matches = [item for item in self.data.data if item['cnn'] == cnn]
        return matches[0] if matches else None
    

     
        