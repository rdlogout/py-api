

from data.food_data import FoodData
import helpers.geo as geo


class FoodRepository:

    def __init__(self):
        self.data = FoodData(self)
    
    def get_items_length(self):
        return len(self.data.data)


    def get_all_food(self,start=0,limit=10,cli=False,q=''):
        temp_data=self.data.data

        if q:
            temp_data=[item for item in temp_data if item['applicant'].lower().find(q.lower())!=-1]

        return temp_data[start:start+limit]

    #find where id is equals to cnn

    def get_food_by_id(self, cnn):
        matches = [item for item in self.data.data if item['cnn'] == cnn]
        return matches[0] if matches else None

     
        