import re

def dateCheck(date_to_check):
    #Convesions are:
    if len(date_to_check) == 8:
        date_to_return = date_to_check
    elif len(date_to_check) == 6: #If type is YYYYMM we assume the first of that month
        date_to_return = date_to_check + '01'
    elif len(date_to_check) == 4: #If type is YYYY we assume the first of January
        date_to_return = date_to_check + '0101'
    elif len(date_to_check) == 19: #If type is {YYYYMMDD, YYYYMMDD} we assume the first date YYYYMMDD
        pattern = r'\{(.*?)\,' 
        datePat = re.findall(pattern,date_to_check)
        date_to_return = datePat[0]

    return date_to_return

def booleanCheck(boolean_to_check):
    #BOOLEAN
    if boolean_to_check == 'NaN' or boolean_to_check == '' or boolean_to_check == 'Unknown': 
        boolean_to_return = None
    elif 'true' in boolean_to_check and 'false' not in boolean_to_check:
        boolean_to_return = True
    elif 'false' in boolean_to_check and 'true' not in boolean_to_check:
        boolean_to_return = False
    else: #This also includes values when there is Yes and No inside the field
        boolean_to_return = None
    
    return boolean_to_return

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

        # drug_id = 'DRUG'+str(counter)
        # counter +=1 

        drug_id = row[1] #Drug id from staging

        if row[3] == [] or row[3] == '' or row[3] == 'Unknown' or row[3] == 'unknown':
            route = 'NaN'
        else:
            route = row[3]

        if row[10] == [] or row[10] == '' or row[10] == 'Unknown':
            off_label_use = 'NaN'
        else:
            off_label_use = row[10]

        if row[14] == [] or row[14] == '' or row[14] == 'Unknown':
            administered_by = 'NaN'
        else:
            administered_by = row[14]

        if row[18] == [] or row[18] == '' or row[18] == 'Unknown':
            frequency_of_administration_value = None
        else:
            frequency_of_administration_value = float(row[18])  

        if row[19] == [] or row[19] == '' or row[19] == 'Unknown':
            frequency_of_administration_unit = 'NaN'
        else:
            frequency_of_administration_unit = row[19]

        #BOOLEAN
        ae_abated_after_stopping_drug = booleanCheck(row[24])

        #BOOLEAN
        ae_reappeared_after_resuming_drug = booleanCheck(row[25])
        
        if row[5] == '' or row[5] == 'unknown' or row[5] == 'Unknown':
            dosage_form = 'NaN'
        else:
            dosage_form = row[5]

        #BOOLEAN
        used_according_to_label = booleanCheck(row[9])

        if row[12] == 'NaN':
            first_exposure_date = None
        else:
            first_exposure_date = dateCheck(row[12])

        if row[13] == 'NaN':
            last_exposure_date = None
        else:
            last_exposure_date = dateCheck(row[13])

        #Boolean check
        previous_ae_to_drug = booleanCheck(row[16])

        #Boolean check
        previous_exposure_to_drug = booleanCheck(row[15])

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
