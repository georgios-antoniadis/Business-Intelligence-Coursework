def drugs(cursor):
    print("============================================================")
    print("Starting to insert drugs....")
    print("============================================================")

    #FdaApiDrug
    drug_select_Query = "select * from staging.FdaApiDrug"
    cursor.execute(drug_select_Query)
    # get all records
    records = cursor.fetchall()
    counter = 1
    for row in records:

        p_record_id = row[0]

        drug_id = 'DRUG'+str(counter)
        counter +=1 

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
        INSERT INTO temp.drug(
            p_record_id,  
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
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        drugvalues = [\
            p_record_id,
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
            ]

        cursor.execute(insert_drug2, drugvalues)
