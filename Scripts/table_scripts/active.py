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
        
        drug_id = row[1] # Drug id from staging

        if row[3] == [] or row[3] == 'unknown' or row[3] == 'Unknown':
            active_ingredient_name = 'NaN'
        else:
            active_ingredient_name = row[3] 

        insert_active_ingredient = """
        INSERT INTO temp.active_ingredient(  
            p_record_id,
            drug_id,
            ingredient_id,           
            active_ingredient_name
            )                  
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(insert_active_ingredient,[p_record_id, drug_id, ingredient_id, active_ingredient_name])
