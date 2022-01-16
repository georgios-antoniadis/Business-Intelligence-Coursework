def outcomes(cursor):
    print("============================================================")
    print("Starting to insert outcomes....")
    print("============================================================")

    # #Outcome
    outcome_select_Query = "select * from staging.FdaApiOutcome"
    cursor.execute(outcome_select_Query)
    # get all records
    records = cursor.fetchall()
    counter = 1 #For the id
    for row in records:

        p_record_id = row[0]
        
        outcome_id = 'OUTCOME'+str(counter)
        counter += 1

        if row[2] == [] or row[2] == 'Unknown' or row[2] == 'unknown':
            medical_status = 'NaN'
        else:
            medical_status = row[2]

        if row[3] == 'NaN' or row[3] == '':
            outcome_number_of_animals_affected = 0
        else:
            outcome_number_of_animals_affected = float(row[3]) #Making sure that it is numeric type

        insert_outcome = """
        INSERT INTO temp.outcome(
            p_record_id,
            outcome_id,              
            outcome_medical_status,              
            outcome_number_of_animals_affected  
            )
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(insert_outcome,[p_record_id, outcome_id, medical_status, outcome_number_of_animals_affected])