import pickle
import json
import numpy as np
from os import path

availability_values = None
area_values = None
location_values = None
model = None


def load_saved_attributes():

    global availability_values
    global location_values
    global area_values
    global model

    with open("columns.json", "r") as f:
        resp = json.load(f)
        availability_values = resp["availability_columns"]
        area_values = resp["area_columns"]
        location_values = resp["location_columns"]

    model = pickle.load(open("banglore_home_prices_model.pickle", "rb"))

def get_location_names():
    #if location_values == None:
    #  load_saved_attributes()
    return location_values

def get_availability_values():
    #if availability_values == None:
    #  load_saved_attributes()
    return availability_values

def get_area_values():
    #if area_values == None:
    #   load_saved_attributes()
    return area_values

def predict_house_price(location, area, availability, sqft, bhk, bathrooms):
    #load_saved_attributes()
    try:
        loc_index = location_values.index(location)
        availability_index = availability_values.index(availability)
        area_index = area_values.index(area)

    except:
        loc_index = -1
        area_index = -1
        availability_index = -1

    loc_array = np.zeros(len(location_values))
    if loc_index >= 0:
        loc_array[loc_index] = 1

    area_array = np.zeros(len(area_values))
    if area_index >= 0:
        area_array[area_index] = 1

    availability_array = np.zeros(len(availability_values))
    if availability_index >= 0:
        availability_array[availability_index] = 1

    availability_array = availability_array[:-1]
    area_array = area_array[:-1]
    loc_array = loc_array[:-1]
    sample = np.concatenate((np.array([sqft, bhk, bathrooms]), availability_array, area_array, loc_array))

    return model.predict(sample.reshape(1,-1))[0]


if __name__ == '__main__':
    load_saved_attributes()
else:
    load_saved_attributes()
