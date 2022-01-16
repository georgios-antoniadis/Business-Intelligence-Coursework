def dim_Animal(cursor):

    print("Creating dimesnion table animal")
    print("")

    dim_animal_sql = """
    INSERT INTO dw.Dim_Animal
    ("animal_id", "species")

    SELECT row_number() over (ORDER BY species) 
    AS "animal_id","species" FROM temp.animal
    GROUP BY species;""" 

    cursor.execute(dim_animal_sql)

def fact_Animal(cursor):
    fact_animal_sql = """
    INSERT INTO dw.Fact_Animal
    ("aer", 
    "animal_id",
    "age",
    "age_unit",
    "gender",
    "weight_kg",
    "is_crossbred",
    "breed_component",
    "reproductive_status")

    SELECT p_record_id,
        species,
        age,
        age_unit,
        gender,
        weight_kg,
        is_crossbred,
        breed_component,
        reproductive_status 
    FROM temp.animal""" 

    cursor.execute(fact_animal_sql)