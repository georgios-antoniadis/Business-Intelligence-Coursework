
def fact_Drug(cursor):
    fact_drug_sql = """
    INSERT INTO dw.Fact_Drug
    (
    aer,
    "drug_id", 
    "route", 
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
    
    SELECT 
    p_record_id,
    active_ingredient_name, 
    "route", 
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
    FROM temp.drug
    """

    cursor.execute(fact_drug_sql)

    update_name_sql = """
    UPDATE dw.Fact_Drug
    SET
    drug_id = AI.active_ingredient_name
    FROM
    temp.active_ingredient AI
    WHERE
    dw.Fact_Drug.aer = AI.p_record_id;
    """

    cursor.execute(update_name_sql)

def dim_Drug(cursor):
    dim_reaction_sql = """
    INSERT INTO dw.Dim_Drug
    ("drug_id", "active_ingredient_name")

    SELECT row_number() over (ORDER BY active_ingredient_name) 
    AS "drug_id", "active_ingredient_name" FROM temp.active_ingredient
    GROUP BY active_ingredient_name;""" 

    cursor.execute(dim_reaction_sql)