import numpy as np
import pandas as pd
import json
from pandas_profiling import ProfileReport
import os

datadir = ('../allData')

fileList = os.listdir(datadir)

print(len(fileList))

data = json.load(open(datadir+"/2007q2.json"))

print(data['results'][0]['reaction'])

print(data['results'][0]['reaction'][0])

# How am I gonna store mutliple reactions?
'''
table 1 reactions:
    reaction_key
    veddra version
    veddra term code
    veddra term name

Veddra version can be removed

table 2 incidents:
    aer
    reaction_key
    drug_key
    active_ingredient_key
    animal_key
    receive_date
    animals_affected
    animals_treated
    primary reporter
    type_of_info
    outcome_med_status
    outcome_animals_affected

table 3 drugs:
    drug_key
    route
    label use
    off label
    dosage form

table 4 active_ingredients:
    active_ingredient_key
    name COULD HAVE MULTIPLE NAMES, which would give multiples of the others
    dose_fraction
    dose_unit

table 5 animals:
    animal_key
    species
    gender
    age
    age unit
    weight ALWAYS IN KG
    breed_component
    is_crossbred

'''