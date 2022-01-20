from xmlrpc.client import boolean


def incident_and_animals(cursor):

    print("============================================================")
    print("Starting to insert incidents and animals....")
    print("============================================================")

    #FdaApiIncident
    incident_select_Query = "select * from staging.FdaApiIncident"
    cursor.execute(incident_select_Query)
    # get all records
    records = cursor.fetchall()

    counter_incident = 1
    counter_animal = 1
    for row in records:

        p_record_id_incident = row[0]

        incident_id = 'INCIDENT'+str(counter_incident)
        counter_incident += 1

        if row[2] == 'NaN' or row[2] == 'unknown' or row[2] == 'Unknown':
            original_receive_date = None
        elif len(row[2]) > 9:
            original_receive_date = row[2][1:10]
        else:
            original_receive_date = row[2]
        
        if row[3] == 'NaN' or row[3] == '':
            number_of_animals_affected = 0
        else:
            number_of_animals_affected = float(row[3])
        
        if row[5] == 'NaN' or row[5] == '':
            number_of_animals_treated = 0
        else:
            number_of_animals_treated = float(row[5])

        #Resolving issues with inconsistency between the treated and affected
        if number_of_animals_affected == 0:
            number_of_animals_affected = number_of_animals_treated
        
        if number_of_animals_treated == 0:
            number_of_animals_treated = number_of_animals_affected

        #End of resolving issues with inconsistency between the treated and affected

        if row[4] == '' or row[4] == 'unknown':
            primary_reporter = 'NaN'
        else:
            primary_reporter = row[4]

        if row[6] == 'NaN':
            onset_date = None
        else:
            onset_date = row[6]

        if row[30] == 'NaN':
            treated_for_ae = None
        else:
            treated_for_ae = row[30]
        
        if row[32] == '':
            health_assessment_prior_to_exposure_condition = 'NaN'
        else:
            health_assessment_prior_to_exposure_condition = row[32]

        if row[31] == '' or row[31] == 'unknown' or row[31] == 'Unknown':
            time_between_exposure_and_onset = 'NaN'
        else:
            time_between_exposure_and_onset = row[31]
        
        if row[33] == '' or row[33] == 'unknown' or row [33] == 'Unknown':
            serious_ae = 'NaN'
        else:
            serious_ae = row[33]

        insert_incident = """INSERT INTO temp.incident(  
            p_record_id,
            incident_id,                         
            primary_reporter,         
            receive_date,                        
            animals_affected,                     
            animals_treated,                      
            health_assessment_prior_to_exposure_condition,
            onset_date,                                      
            treated_for_ae,
            time_between_exposure_and_onset,
            serious_ae
            )                     	                                
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """ 

        cursor.execute(insert_incident,[\
            p_record_id_incident,
            incident_id,                        
            primary_reporter,          
            original_receive_date,                        
            number_of_animals_affected,                     
            number_of_animals_treated,                      
            health_assessment_prior_to_exposure_condition,  
            onset_date,                                       
            treated_for_ae,
            time_between_exposure_and_onset,
            serious_ae
        ])

        ################################################################
        # Animal

        p_record_id_animal = row[0]

        animal_id = 'ANIMAL'+str(counter_animal)
        counter_animal += 1

        if row[16] == [] or row[16] == '' or row[16] == 'Unknown' or row[16] == 'unknown':
            species = 'NaN'
        else:
            species = row[16]
        
        if row[17] == [] or row[17] == '' or row[17] == 'Unknown' or row[17] == 'unknown':
            gender = 'NaN'
        else:
            gender = row[17]
        
        if row[20] == [] or row[20] == '' or row[20] == 'Unknown' or row[20] == 'unknown':
            age_unit = 'NaN'
        else:
            age_unit = row[20]

        if row[19] == 'NaN' or row[19] == '':
            age = None
        else:
            age = row[19]

        if row[22] == 'NaN' or row[22] == '':
            weight = None
        else:
            weight = row[22]
        
        # if row[25] == 'NaN' or row[25] == '' or row == 'Unknown': 
        if isinstance(row[25],boolean): #Checking if the value is boolean
            is_crossbred = None
        else:
            is_crossbred = row[25]

        if row[26] == [] or row[26] == '' or row == 'Unknown':
            breed_component = 'NaN'
        else:
            breed_component = row[26]

        if row[29] == []:
            reproductive_status = 'NaN'
        else:
            reproductive_status = row[29]

        insert_animals = """
        INSERT INTO temp.animal(
            p_record_id,  
            animal_id,                            
            species, 	                         
            gender, 	                             
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
            p_record_id_animal,
            animal_id,                            
            species, 	                         
            gender, 	                             
            age,                                 
            age_unit, 	                         
            weight,    	                    
            is_crossbred, 	                 
            breed_component, 	             
            reproductive_status 
        ])
        
###############################################################
# Testing with breed component
#         #Dealing with the very weird column of breed component
#         if int(number_of_animals_affected) > 1:
#             breed_text.append(breed_component)
#             breed_type.append(type(breed_component))
#             # print(type(breed_component))
#             # print(breed_component)
#             # number_of_components = len(breed_component)
#             # if number_of_components > 1:
#             #     for i in range(number_of_components):
#             #         print(breed_component[i])
#     with open('breed_type.txt', 'a') as f:
#             for breed_t in breed_type:
#                 component_type_line = str(counter_animal) + breed_t
#                 f.write(component_type_line)
    
#     with open('breed_text.txt', 'a') as f:
#             for breed in breed_text:
#                 component_line = str(counter_animal) + breed
#                 f.write(component_line)
