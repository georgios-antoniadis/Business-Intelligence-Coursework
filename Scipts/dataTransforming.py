import json
import os

def readFile(dir):
    file = dir
    data = json.load(open(file))
    reactions = []
    incidents = []
    drugs = []
    activeIngredients = []
    animals = []
    results = data['results']

    for result in results:
        reactions.append(result['reaction'])
        drugs.append(result['drug'])
        animals.append(result['animal'])


def filtering(file):
    data = json.load(open(file))
    results = data['results']
    
    print(len(results))

    nonHumanresults = []

    for i in range(len(results)):
        try:
            if 'Human' in results[i]['animal']['species']:
                continue
            else:
                nonHumanresults.append(results[i])
        except KeyError: # What to do if no animal record exists
            nonHumanresults.append(results[i]) 
    
    print(len(nonHumanresults))


clearHumans('../allData/2007q2.json')