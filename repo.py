import csv


def read_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


class FoodData:

    # reading food data from csv
    def __init__(self, data):
        self.data = read_csv('csv/Mobile_Food_Facility_Permit.csv')
        self.data = [dict(zip(self.data[0], row)) for row in self.data]
        self.data = self.data[1:]





class FoodRepository:

    def __init__(self):
        self.data = FoodData(self)
    
    def get_items_length(self):
        return len(self.data.data)

    def get_all_food(self,start=0,limit=24,q=''):
        temp_data=self.data.data

        if q:
            temp_data=[item for item in temp_data if item['applicant'].lower().find(q.lower())!=-1]
        return temp_data[start:start+limit]

    #find where id is equals to cnn

    def get_food_by_id(self, cnn):
        matches = [item for item in self.data.data if item['cnn'] == cnn]
        return matches[0] if matches else None

     
        