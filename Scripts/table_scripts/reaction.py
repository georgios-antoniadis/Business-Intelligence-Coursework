def reactions(cursor):
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

        reaction_id = 'REACTION'+str(counter)
        counter += 1

        if row[2] == [] or row[2] == '' or row[2] == 'Unknown':
            ved_version = 'NaN'
        else:
            ved_version = row[2]

        if row[3] == [] or row[3] == '' or row[3] == 'Unknown':
            ved_term_code = 'NaN'
        else:
            ved_term_code = row[3]

        if row[4] == [] or row[4] == '' or row[4] == 'Unknown':
            ved_term_name = 'NaN'
        else:
            ved_term_name = row[4]

        if row[5] == '' or row[5] == 'NaN' or row[5] == 'Unknown':
            animals_affected = 0
        else:
            animals_affected = row[5]

        insert_reaction = """
        INSERT INTO temp.reaction(
            p_record_id,
            reaction_id,         
            veddra_version,      
            veddra_term_code,    
            veddra_term_name,
            number_of_animals_affected    
            )
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(insert_reaction,[p_record_id, reaction_id, ved_version, ved_term_code, ved_term_name, animals_affected])
