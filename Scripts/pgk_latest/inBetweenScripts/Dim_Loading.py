def Load_Dim_Animal(cursor):

    print("Insert data to Dim_Animal")
    print("")

    dim_animal_sql = """
    INSERT INTO dw.Dim_Animal
    ("animal_id", "species")

    SELECT row_number() over (ORDER BY species) 
    AS "animal_id","species" FROM temp.animal
    GROUP BY species;""" 

    cursor.execute(dim_animal_sql)
    
def Load_Dim_Drug(cursor):

    print("Creating dimesnion table drug")
    print("")

    dim_drug_sql = """
    INSERT INTO dw.Dim_Drug
    ("drug_id", "active_ingredient_name")

    SELECT row_number() over (ORDER BY active_ingredient_name) 
    AS "drug_id", "active_ingredient_name" FROM temp.active_ingredient
    GROUP BY active_ingredient_name;""" 

    cursor.execute(dim_drug_sql)

def Load_Dim_Outcome(cursor):

    print("Creating dimesnion table outcome")
    print("")

    dim_outcome_sql = """
    INSERT INTO dw.Dim_Outcome
    ("outcome_id", "outcome_medical_status")

    SELECT row_number() over (ORDER BY outcome_medical_status) 
    AS "outcome_id","outcome_medical_status" FROM temp.outcome
    GROUP BY outcome_medical_status;""" 

    cursor.execute(dim_outcome_sql)

def Load_Dim_Reaction(cursor):

    print("Creating dimesnion table reaction")
    print("")

    dim_reaction_sql = """
    INSERT INTO dw.Dim_Reaction
    ("reaction_id", "veddra_version", "veddra_term_code", "veddra_term_name")

    SELECT row_number() over (ORDER BY veddra_term_name) 
    AS "reaction_id", "veddra_version", "veddra_term_code", "veddra_term_name" FROM temp.reaction
    GROUP BY veddra_version, veddra_term_code, veddra_term_name;""" 

    cursor.execute(dim_reaction_sql)
    
    
def Load_Dim_Date(cursor):
        
    dim_date_sql = '''
    INSERT INTO dw.dim_date
    SELECT TO_CHAR(datum,'yyyymmdd')::INT AS date_dim_id,
           datum AS date_actual,
           EXTRACT(epoch FROM datum) AS epoch,
           TO_CHAR(datum,'fmDDth') AS day_suffix,
           TO_CHAR(datum,'Day') AS day_name,
           EXTRACT(dow FROM datum) + 1 AS day_of_week,
           EXTRACT(isodow FROM datum) AS day_of_week_iso,
           EXTRACT(DAY FROM datum) AS day_of_month,
           datum - DATE_TRUNC('quarter',datum)::DATE +1 AS day_of_quarter,
           EXTRACT(doy FROM datum) AS day_of_year,
           TO_CHAR(datum,'W')::INT AS week_of_month,
           EXTRACT(week FROM datum) AS week_of_year,
           TO_CHAR(datum,'YYYY"-W"IW-') || EXTRACT(isodow FROM datum) AS week_of_year_iso,
           EXTRACT(MONTH FROM datum) AS month_actual,
           TO_CHAR(datum,'Month') AS month_name,
           TO_CHAR(datum,'Mon') AS month_name_abbreviated,
           EXTRACT(quarter FROM datum) AS quarter_actual,
           CASE
             WHEN EXTRACT(quarter FROM datum) = 1 THEN 'First'
             WHEN EXTRACT(quarter FROM datum) = 2 THEN 'Second'
             WHEN EXTRACT(quarter FROM datum) = 3 THEN 'Third'
             WHEN EXTRACT(quarter FROM datum) = 4 THEN 'Fourth'
           END AS quarter_name,
           EXTRACT(year FROM datum) AS year_actual,
           EXTRACT(isoyear FROM datum) AS year_actual_iso,
           datum +(1 -EXTRACT(isodow FROM datum))::INT AS first_day_of_week,
           datum +(7 -EXTRACT(isodow FROM datum))::INT AS last_day_of_week,
           datum +(1 -EXTRACT(DAY FROM datum))::INT AS first_day_of_month,
           (DATE_TRUNC('MONTH',datum) +INTERVAL '1 MONTH - 1 day')::DATE AS last_day_of_month,
           DATE_TRUNC('quarter',datum)::DATE AS first_day_of_quarter,
           (DATE_TRUNC('quarter',datum) +INTERVAL '3 MONTH - 1 day')::DATE AS last_day_of_quarter,
           TO_DATE(EXTRACT(isoyear FROM datum) || '-01-01','YYYY-MM-DD') AS first_day_of_year,
           TO_DATE(EXTRACT(isoyear FROM datum) || '-12-31','YYYY-MM-DD') AS last_day_of_year,
           TO_CHAR(datum,'mmyyyy') AS mmyyyy,
           TO_CHAR(datum,'mmddyyyy') AS mmddyyyy,
           CASE
             WHEN EXTRACT(isodow FROM datum) IN (6,7) THEN TRUE
             ELSE FALSE
           END AS weekend_indr
    FROM (SELECT '1985-01-01'::DATE+ SEQUENCE.DAY AS datum
          FROM GENERATE_SERIES (0,42002) AS SEQUENCE (DAY)
          GROUP BY SEQUENCE.DAY) DQ
    ORDER BY 1
    '''
    
    cursor.execute(dim_date_sql)