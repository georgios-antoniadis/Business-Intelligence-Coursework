import psycopg2

# try:
connection = psycopg2.connect(host='localhost',
                                        database='vets_dw',
                                        user='postgres',
                                        password='password')

####################################################################
# Inserting data
####################################################################

print("============================================================")
print("Starting to insert reaction....")
print("============================================================")

#Reaction
reaction_select_Query = "select * from staging.FdaApiReaction"
cursor = connection.cursor()
cursor.execute(reaction_select_Query)
# get all records
records = cursor.fetchall()
counter = 1 #For the id
for row in records:
    p_record_id = row[0]
    
    if row[2] == []:
        ved_version = 'unknown'
    else:
        ved_version = row[2]

    if row[3] == []:
        ved_term_code = 'unknown'
    else:
        ved_term_code = row[3]

    if row[4] == []:
        ved_term_name = 'unknown'
    else:
        ved_term_name = row[4]

    animals_affected = row[5]
    counter += 1

    insert_reaction = """
    INSERT INTO dw.reaction(
        reaction_id,         
        veddra_version,      
        veddra_term_code,    
        veddra_term_name,    
        number_of_animals_affected
        )
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(insert_reaction,[p_record_id, ved_version, ved_term_code, ved_term_name, animals_affected])


##################################################################

print("============================================================")
print("Starting to insert outcomes....")
print("============================================================")

#Outcome
outcome_select_Query = "select * from staging.FdaApiOutcome"
cursor = connection.cursor()
cursor.execute(outcome_select_Query)
# get all records
records = cursor.fetchall()
counter = 1 #For the id
for row in records:
    p_record_id = row[0]
    
    if row[2] == []:
        medical_status = 'unknown'
    else:
        medical_status = row[2]

    number_of_animals_affected = row[3]

    counter += 1

    insert_outcome = """
    INSERT INTO dw.outcome(
        outcome_id,              
        outcome_medical_status,              
        outcome_number_of_animals_affected  
        )
    VALUES (%s, %s, %s)
    """

    cursor.execute(insert_outcome,[p_record_id, medical_status, number_of_animals_affected])


##################################################################

print("============================================================")
print("Starting to insert active ingredients....")
print("============================================================")

#ActiveIngredient
active_select_Query = "select * from staging.FdaApiActiveIngredient"
cursor = connection.cursor()
cursor.execute(active_select_Query)
# get all records
records = cursor.fetchall()

for row in records:

    ingredient_id = row[0]

    drug_id = row[1]

    if row[3] == []:
        name = 'unknown'
    else:
        name = row[3] 

    dose_numerator = row[4]
    dose_numerator_unit = row[5]
    dose_denominator = row[6]
    dose_denominator_unit = row[7]

    if float(row[4]) or float(row[6]) == 0:
        dose_fraction = None
    else:
        dose_fraction = float(dose_numerator) / float(dose_denominator)
    
    if row[5] == []:
        dose_unit = 'unknown'
    else:
        dose_unit = dose_numerator_unit

    insert_drug1 = """
    INSERT INTO dw.active_ingredient(  
        ingredient_id,       
        drug_id,           
        active_ingredient_name,
        dose_fraction,
        dose_unit  
        )                  
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(insert_drug1,[ingredient_id, drug_id, dose_fraction,dose_unit, name])

##################################################################

print("============================================================")
print("Starting to insert drugs....")
print("============================================================")

#FdaApiDrug
drug_select_Query = "select * from staging.FdaApiDrug"
cursor = connection.cursor()
cursor.execute(drug_select_Query)
# get all records
records = cursor.fetchall()
for row in records:
    p_record_id = row[0]

    if row[3] == []:
        route = 'unknown'
    else:
        route = row[3]

    if row[10] == []:
        off_label_use = 'unknown'
    else:
        off_label_use = row[10]

    if row[14] == []:
        administered_by = 'unknown'
    else:
        administered_by = row[14]

    if row[18] == []:
        frequency_of_administration_value = 'unknown'
    else:
        frequency_of_administration_value = row[18]  

    if row[19] == []:
        frequency_of_administration_unit = 'unknown'
    else:
        frequency_of_administration_unit = row[19]

    if row[24] == []:
        ae_abated_after_stopping_drug = 'unknown'
    else:
        ae_abated_after_stopping_drug = row[24]

    if row[25] == []:
        ae_reappeared_after_resuming_drug = 'unknown'
    else:
        ae_reappeared_after_resuming_drug = row[25]  
    
    dosage_form = row[5]

    if row[9] == 'NaN':
        used_according_to_label = None
    else:   
        used_according_to_label = row[9]  

    first_exposure_date = row[12]
    last_exposure_date = row[13] 

    if row[15] == 'NaN':
        previous_exposure_to_drug = None
    else:   
        previous_exposure_to_drug = row[15]  

    if row[16] == 'NaN':
        previous_ae_to_drug = None
    else:   
        previous_ae_to_drug = row[16]  


    insert_drug2 = """
    INSERT INTO dw.drug(  
        drug_id,                              
        route,                              
        dosage_form,                          
        used_according_to_label,             
        off_label_use,                        
        first_exposure_date,                  
        last_exposure_date,                   
        administered_by,                      
        previous_exposure_to_drug,           
        previous_ae_to_drug,                
        frequency_of_administration_value,    
        frequency_of_administration_unit,                          
        ae_abated_after_stopping_drug,        
        ae_reappeared_after_resuming_drug
        )                            
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    drugvalues = [\
        p_record_id,
        route, 
        dosage_form,
        used_according_to_label,
        off_label_use,
        first_exposure_date,
        last_exposure_date,
        administered_by, 
        previous_exposure_to_drug,           
        previous_ae_to_drug,                
        frequency_of_administration_value,    
        frequency_of_administration_unit,                           
        ae_abated_after_stopping_drug,        
        ae_reappeared_after_resuming_drug
        ]

    cursor.execute(insert_drug2, drugvalues)

##################################################################

print("============================================================")
print("Starting to insert incidents....")
print("============================================================")

#FdaApiIncident
incident_select_Query = "select * from staging.FdaApiIncident"
cursor = connection.cursor()
cursor.execute(incident_select_Query)
# get all records
records = cursor.fetchall()
counter = 1
for row in records:

    aer = row[0]
    if len(row[2]) > 9:
        original_receive_date = row[2][1:10]
    else:
        original_receive_date = row[2]
    
    if row[3] == 'NaN':
        number_of_animals_affected = None
    else:
        number_of_animals_affected = row[3]

    if row[4] == []:
        primary_reporter = 'unknown'
    else:
        primary_reporter = row[4]
    
    number_of_animals_treated = row[5]
    onset_date = row[6]
    
    if row[15] == []:
        health_assessment_prior_to_exposure_assessed_by = 'unknown'
    else:
        health_assessment_prior_to_exposure_assessed_by = row[15]
    
    if row[16] == []:
        species = 'unknown'
    else:
        species = row[16]
    
    if row[17] == []:
        gender = 'unknown'
    else:
        gender = row[17]
    
    if row[18] == []:
        female_animals_physiological_status = 'unknown'
    else:
        female_animals_physiological_status = row[18]
    
    if row[20] == []:
        age_unit = 'unknown'
    else:
        age_unit = row[20]

    age = row[19]
    weight = row[22]
    is_crossbred = row[25]

    if row[26] == []:
        breed_component = 'unknown'
    else:
        breed_component = row[26]

    if row[29] == []:
        reproductive_status = 'unknown'
    else:
        reproductive_status = row[29]

    if row[30] == 'NaN':
        treated_for_ae = None
    else:
        treated_for_ae = row[30]

    if row[31] == []:
        time_between_exposure_and_onset = 'unknown'
    else:
        time_between_exposure_and_onset = row[31]
    
    if row[32] == []:
        health_assessment_prior_to_exposure_condition = 'unknown'
    else:
        health_assessment_prior_to_exposure_condition = row[32]


    p_record_id = row[0]
    counter += 1

    insert_animals = """
    INSERT INTO dw.animal(  
        animal_id,                            
        species, 	                         
        gender, 	                             
        female_animal_physiological_status, 	 
        age,                                 
        age_unit, 	                         
        "weight_kg",    	                    
        is_crossbred, 	                 
        breed_component, 	             
        reproductive_status 
        )	                                
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(insert_animals,[\
        p_record_id,                            
        species, 	                         
        gender, 	                             
        female_animals_physiological_status, 	 
        age,                                 
        age_unit, 	                         
        weight,    	                    
        is_crossbred, 	                 
        breed_component, 	             
        reproductive_status, 
    ])


    insert_incident = """INSERT INTO dw.incident(  
        aer,                                  
        receive_date,                        
        animals_affected,                     
        animals_treated,                      
        health_assessment_prior_to_exposure_condition,  
        onset_date,                                    
        time_between_exposure_and_onset,      
        treated_for_ae
        )                     	                                
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """ 

    cursor.execute(insert_incident,[\
        aer,                                  
        original_receive_date,                        
        animals_affected,                     
        number_of_animals_treated,                      
        health_assessment_prior_to_exposure_condition,  
        onset_date,                                    
        time_between_exposure_and_onset,      
        treated_for_ae      
    ])


##################################################################
    
# except psycopg2.connect.Error as e:
#     print("Error reading data from PostgreSQL table", e)

# finally:
#     if connection.is_connected():
#         connection.close()
#         cursor.close()
#         print("PostgreSQL connection is closed")