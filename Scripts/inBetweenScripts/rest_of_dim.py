def dim_Outcome(cursor):
    dim_outcome_sql = """
    INSERT INTO dw.Dim_Outcome
    ("outcome_id", "outcome_medical_status")

    SELECT row_number() over (ORDER BY outcome_medical_status) 
    AS "outcome_id","outcome_medical_status" FROM temp.outcome
    GROUP BY outcome_medical_status;""" 

    cursor.execute(dim_outcome_sql)

def dim_Reaction(cursor):
    dim_reaction_sql = """
    INSERT INTO dw.Dim_Reaction
    ("reaction_id", "veddra_version", "veddra_term_code", "veddra_term_name")

    SELECT row_number() over (ORDER BY veddra_term_name) 
    AS "reaction_id", "veddra_version", "veddra_term_code", "veddra_term_name" FROM temp.reaction
    GROUP BY veddra_version, veddra_term_code, veddra_term_name;""" 

    cursor.execute(dim_reaction_sql)