import psycopg2

# try:
connection = psycopg2.connect(host='localhost',
                                        database='vets_dw',
                                        user='postgres',
                                        password='password')
connection.autocommit = True

cursor = connection.cursor()

truncTables = ['dw.reaction',
                   'dw.animal',
                   'dw.date',
                   'dw.fact',
                   'dw.incident',
                   'dw.outcome',
                   'dw.drug',
                   'dw.active_ingredient']

for table in truncTables:
         cursor.execute('TRUNCATE TABLE ' + table)

####################################################################
# Inserting data
####################################################################

print("============================================================")
print("Starting to insert reactions....")
print("============================================================")

#Reaction
reaction_select_Query = "select * from staging.FdaApiReaction"
cursor.execute(reaction_select_Query)
# get all records
records = cursor.fetchall()
counter = 1 #For the id
for row in records:
    p_record_id = row[0]
    
    if row[2] == []:
        ved_version = 'NaN'
    else:
        ved_version = row[2]

    if row[3] == []:
        ved_term_code = 'NaN'
    else:
        ved_term_code = row[3]

    if row[4] == []:
        ved_term_name = 'NaN'
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


# ##################################################################

print("============================================================")
print("Starting to insert outcomes....")
print("============================================================")

# #Outcome
outcome_select_Query = "select * from staging.FdaApiOutcome"
cursor = connection.cursor()
cursor.execute(outcome_select_Query)
# get all records
records = cursor.fetchall()
counter = 1 #For the id
for row in records:
    p_record_id = row[0]
    
    if row[2] == []:
        medical_status = 'NaN'
    else:
        medical_status = row[2]

    if row[3] == 'NaN' or row[3] == '':
        outcome_number_of_animals_affected = 0
    else:
        outcome_number_of_animals_affected = row[3]

    counter += 1

    insert_outcome = """
    INSERT INTO dw.outcome(
        outcome_id,              
        outcome_medical_status,              
        outcome_number_of_animals_affected  
        )
    VALUES (%s, %s, %s)
    """

    cursor.execute(insert_outcome,[p_record_id, medical_status, outcome_number_of_animals_affected])


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
        active_ingredient_name = 'NaN'
    else:
        active_ingredient_name = row[3] 

    dose_numerator = row[4]
    dose_numerator_unit = row[5]
    dose_denominator = row[6]
    dose_denominator_unit = row[7]

    if float(row[4]) or float(row[6]) == 0:
        dose_fraction = None
    else:
        dose_fraction = float(dose_numerator) / float(dose_denominator)
    
    if row[5] == [] or row[5] == 'Unknown' or row[5] == 'unknown':
        dose_unit = 'NaN'
    else:
        dose_unit = dose_numerator_unit

    insert_active_ingredient = """
    INSERT INTO dw.active_ingredient(  
        ingredient_id,       
        drug_id,           
        active_ingredient_name,
        dose_fraction,
        dose_unit  
        )                  
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(insert_active_ingredient,[ingredient_id, drug_id, active_ingredient_name, dose_fraction, dose_unit])

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

    if row[3] == [] or row[3] == 'Unknown' or row[3] == 'unknown':
        route = 'NaN'
    else:
        route = row[3]

    if row[10] == []:
        off_label_use = 'NaN'
    else:
        off_label_use = row[10]

    if row[14] == []:
        administered_by = 'NaN'
    else:
        administered_by = row[14]

    if row[18] == []:
        frequency_of_administration_value = 'NaN'
    else:
        frequency_of_administration_value = row[18]  

    if row[19] == []:
        frequency_of_administration_unit = 'NaN'
    else:
        frequency_of_administration_unit = row[19]

    if row[24] == []:
        ae_abated_after_stopping_drug = 'NaN'
    else:
        ae_abated_after_stopping_drug = row[24]

    if row[25] == []:
        ae_reappeared_after_resuming_drug = 'NaN'
    else:
        ae_reappeared_after_resuming_drug = row[25]  
    
    if row[5] == '' or row[5] == 'unknown' or row[5] == 'Unknown':
        dosage_form = 'NaN'
    else:
        dosage_form = row[5]

    if row[9] == 'NaN':
        used_according_to_label = None
    else:   
        used_according_to_label = row[9]  

    if row[12] == 'NaN':
        first_exposure_date = None
    else:
        first_exposure_date = row[12]

    if row[13] == 'NaN':
        last_exposure_date = None
    else:
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
    print("Starting to insert incidents and animals....")
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
    
    if row[3] == 'NaN' or row[3] == '':
        number_of_animals_affected = 0
    else:
        number_of_animals_affected = row[3]

    if row[4] == []:
        primary_reporter = 'NaN'
    else:
        primary_reporter = row[4]
    
    if row[5] == 'NaN' or row[5] == '':
        number_of_animals_treated = 0
    else:
        number_of_animals_treated = row[5]

    if row[6] == 'NaN':
        onset_date = None
    else:
        onset_date = row[6]
    
    if row[15] == []:
        health_assessment_prior_to_exposure_assessed_by = 'NaN'
    else:
        health_assessment_prior_to_exposure_assessed_by = row[15]
    
    if row[16] == []:
        species = 'NaN'
    else:
        species = row[16]
    
    if row[17] == []:
        gender = 'NaN'
    else:
        gender = row[17]
    
    if row[18] == [] or row[18] == 'Not applicable' or row[18] == 'NOT APPLICABLE':
        female_animals_physiological_status = 'NaN'
    else:
        female_animals_physiological_status = row[18]
    
    if row[20] == []:
        age_unit = 'NaN'
    else:
        age_unit = row[20]

    if row[19] == 'NaN':
        age = None
    else:
        age = row[19]

    if row[22] == 'NaN':
        weight = None
    else:
        weight = row[22]
    
    if row[25] == 'NaN':
        is_crossbred = None
    else:
        is_crossbred = row[25]

    if row[26] == []:
        breed_component = 'NaN'
    else:
        breed_component = row[26]

    if row[29] == []:
        reproductive_status = 'NaN'
    else:
        reproductive_status = row[29]

    if row[30] == 'NaN':
        treated_for_ae = None
    else:
        treated_for_ae = row[30]
    
    if row[32] == []:
        health_assessment_prior_to_exposure_condition = 'NaN'
    else:
        health_assessment_prior_to_exposure_condition = row[32]


    p_record_id = row[0]
    counter += 1

    insert_incident = """INSERT INTO dw.incident(  
        aer,                                  
        receive_date,                        
        animals_affected,                     
        animals_treated,                      
        health_assessment_prior_to_exposure_condition,  μ,
        onset_date,                                      
        treated_for_ae
        )                     	                                
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """ 

    cursor.execute(insert_incident,[\
        aer,                                  
        original_receive_date,                        
        number_of_animals_affected,                     
        number_of_animals_treated,                      
        health_assessment_prior_to_exposure_condition,  
        onset_date,                                       
        treated_for_ae      
    ])

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

##################################################################
    
# except psycopg2.connect.Error as e:
#     print("Error reading data from PostgreSQL table", e)

# finally:
#     if connection.is_connected():
#         connection.close()
#         cursor.close()
#         print("PostgreSQL connection is closed")

connection.close()
cursor.close()
