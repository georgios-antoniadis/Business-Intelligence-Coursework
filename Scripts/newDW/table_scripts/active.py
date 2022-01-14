def active_ingredients(cursor):
    print("============================================================")
    print("Starting to insert active ingredients....")
    print("============================================================")

    #ActiveIngredient
    active_select_Query = "select * from staging.FdaApiActiveIngredient"
    cursor.execute(active_select_Query)
    # get all records
    records = cursor.fetchall()
    counter = 1
    for row in records:

        p_record_id = row[0]

        ingredient_id = 'INGREDIENT'+str(counter)
        counter += 1

        if row[3] == []:
            active_ingredient_name = 'NaN'
        else:
            active_ingredient_name = row[3] 

        dose_numerator = row[4] #NaN seems to default to 1
        dose_denominator = row[6] #NaN seems to default to 1

        if float(row[4]) or float(row[6]) == 0:
            dose_fraction = None
        else:
            dose_fraction = float(dose_numerator) / float(dose_denominator)
        

        # Regulating dose unit
        if row[5] == '' or row[5] == 'Unknown' or row[5] == 'unknown':
            dose_numerator_unit = 'NaN'
        else:
            dose_numerator_unit = row[5]

        if row[7] == '' or row[7] == 'Unknown' or row[7] == 'unknown':
            dose_denominator_unit = 'NaN'
        else:
            dose_denominator_unit = row[7]

        if dose_numerator_unit == 'NaN':
            dose_unit = dose_denominator_unit
        else:
            dose_unit = 'NaN'
        if dose_denominator_unit == 'NaN' and dose_denominator_unit == 'NaN':
            dose_unit = 'NaN'
        else:
            dose_unit = 'NaN'

        insert_active_ingredient = """
        INSERT INTO temp.active_ingredient(  
            p_record_id,       
            ingredient_id,           
            active_ingredient_name,
            dose_fraction,
            dose_unit  
            )                  
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(insert_active_ingredient,[p_record_id, ingredient_id, active_ingredient_name, dose_fraction, dose_unit])
