import json
import os

def filtering(species):
    if 'Human' in species:
        return False
    else:
        return True

def reactions(reaction):

    numOfReactions = len(reaction)

    final = []

    if numOfReactions > 1:
        for i in range(numOfReactions):
            final.append([reaction[i]['veddra_version'],reaction[i]['veddra_term_code'],reaction[i]['veddra_term_name']])

    else:
        final.append([reaction[0]['veddra_version'],reaction[0]['veddra_term_code'],reaction[0]['veddra_term_name']])

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

    if numOfDrugs > 1: #Filling in data and data imputation
        for dr in drug:
            if 'active_ingredients' in dr.keys():  
                active_ingr_names.append(dr['active_ingredients'][0]['name'])
                fraction = dr['active_ingredients'][0]['dose']['numerator'] + dr['active_ingredients'][0]['dose']['denominator']
                dose_fractions.append(fraction)
                dose_units.append(dr['active_ingredients'][0]['dose']['numerator_unit'])

                if 'route' in dr.keys():
                    routes.append(dr['route'])
                else:
                    routes.append('unknown')
                if 'used_according_to_label' in dr.keys(): 
                    used_according_to_labels.append(dr['used_according_to_label'])
                else:
                    used_according_to_labels.append('unknown')
                if 'off_label_use' in dr.keys():
                    off_label_uses.append(dr['off_label_use'])
                else:
                    off_label_uses.append('unknown')
                if 'dosage_form' in dr.keys():
                    dosage_forms.append(dr['dosage_form'])
                else:
                    dosage_forms.append('unknown')

            else:
                continue
            

    else:

        if 'active_ingredients' in drug.keys():  
            active_ingr_names.append(drug['active_ingredients'][0]['name'])
            fraction = drug['active_ingredients'][0]['dose']['numerator'] + drug['active_ingredients'][0]['dose']['denominator']
            dose_fractions.append(fraction)
            dose_units.append(drug['active_ingredients'][0]['dose']['numerator_unit'])
        
            #If is nested to avoid logging records with no active ingredients

            if 'route' in drug.keys():
                routes.append(drug['route'])
            else:
                routes.append('unknown')
            
            if 'used_according_to_label' in drug.keys(): 
                used_according_to_labels.append(drug['used_according_to_label'])
            else:
                used_according_to_labels.append('unknown')
            
            if 'off_label_use' in drug.keys():
                off_label_uses.append(drug['off_label_use'])
            else:
                off_label_uses.append('unknown')
            
            if 'dosage_form' in drug.keys():
                dosage_forms.append(drug['dosage_form'])
            else:
                dosage_forms.append('unknown')
        
        
    return [routes, used_according_to_labels, off_label_uses, dosage_forms, active_ingr_names, dose_fractions, dose_units]


def animals(animal):

    numOfAnimals = len(animal) 


