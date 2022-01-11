import json
import os

def filtering(species):
    if 'Human' in species:
        return False
    else:
        return True

def reactions(reaction):

    numOfReactions = len(reaction)

    veddra_ver = []
    veddra_code = []
    veddra_term_name = []

    if numOfReactions > 1:
        for i in range(numOfReactions):
            veddra_ver.append(reaction[i]['veddra_version'])
            veddra_code.append(reaction[i]['veddra_term_code'])
            veddra_term_name.append(reaction[i]['veddra_term_name'])
    
    else:
        veddra_ver.append(reaction[0]['veddra_version'])
        veddra_code.append(reaction[0]['veddra_term_code'])
        veddra_term_name.append(reaction[0]['veddra_term_name'])

    final = [veddra_ver,veddra_code,veddra_term_name]

    return final

def drugs(drug):

    numOfDrugs = len(drug)

    routes = []
    used_according_to_labels = []
    off_label_uses = []
    dosage_forms = []
    active_ingr_names = []
    dose_fractions = []
    dose_units = []

    print(drug)
    print(numOfDrugs)

    if numOfDrugs > 1:
        for dr in drug:
            routes.append(dr['route'])
            used_according_to_labels.append(dr['used_according_to_label'])
            off_label_uses.append(dr['off_label_use'])
            dosage_forms.append(dr['dosage_form'])
            active_ingr_names.append(dr['active_ingredients'][0]['name'])
            fraction = dr['active_ingredients'][0]['dose']['numerator'] + dr['active_ingredients'][0]['dose']['denominator']
            dose_fractions.append(fraction)
            dose_units.append(dr['active_ingredients'][0]['dose']['numerator_unit'])

    else:
        routes.append(drug['route'])
        used_according_to_labels.append(drug['used_according_to_label'])
        off_label_uses.append(drug['off_label_use'])
        dosage_forms.append(drug['dosage_form'])
        active_ingr_names.append(drug['active_ingredients'][0]['name'])
        fraction = drug['active_ingredients'][0]['dose']['numerator'] + '/' +drug['active_ingredients'][0]['dose']['denominator']
        dose_fractions.append(fraction)
        dose_units.append(drug['active_ingredients'][0]['dose']['numerator_unit'])
    
    return [routes, used_according_to_labels, off_label_uses, dosage_forms, active_ingr_names, dose_fractions, dose_units]


def animals(animal):

    numOfAnimals = len(animal) 


