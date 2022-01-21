def Load_Fact_Animal(cursor):

    print("Insert data to Fact_Animal")
    print("")

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
    
    SELECT 
       tmpanimal.p_record_id,
       dimanimal.animal_id,
       tmpanimal.age,
       tmpanimal.age_unit,
       tmpanimal.gender,
       tmpanimal.weight_kg,
       tmpanimal.is_crossbred,
       tmpanimal.breed_component,
       tmpanimal.reproductive_status

    FROM temp.animal tmpanimal
    INNER JOIN dw.dim_animal dimanimal
    ON tmpanimal.species = dimanimal.species

    """ 

    cursor.execute(fact_animal_sql)   
    
    
def fact_Drug(cursor):

    print("Creating fact table drug")
    print("")

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
    DRG.p_record_id,
    DW_DRG.drug_id,
--	ACT.active_ingredient_name,
    DRG."route",
    DRG.dosage_form,
    DRG.used_according_to_label,
    DRG.off_label_use,
    DRG.first_exposure_date,
    DRG.last_exposure_date,
    DRG.administered_by,
    DRG.previous_exposure_to_drug,
    DRG.previous_ae_to_drug,
    DRG.frequency_of_administration_value,
    DRG.frequency_of_administration_unit,
    DRG.ae_abated_after_stopping_drug,
    DRG.ae_reappeared_after_resuming_drug
    FROM temp.drug DRG

    --INNER JOIN temp.incident INC
    --ON DRG.p_record_id = INC.p_record_id
    INNER JOIN temp.active_ingredient ACT
    ON DRG.p_record_id = ACT.p_record_id
    AND DRG.drug_id = ACT.drug_id
    INNER JOIN dw.Dim_Drug DW_DRG
    ON DW_DRG.active_ingredient_name = ACT.active_ingredient_name
    """

    cursor.execute(fact_drug_sql)


def fact_Incident(cursor):

    print("Creating fact table incident")
    print("")

    fact_incident_sql = """
    INSERT INTO dw.Fact_Incident
    (
        fact_incident_id,
        aer,
        reaction_id,
        outcome_id,
        drug_id,
        primary_reporter,
        total_animals_affected,
        total_animals_treated,
        onset_date,
        receive_date,
        treated_for_ae,
        time_between_exposure_and_onset, 
        health_assessment_prior_to_exposure_condition,
        serious_ae,
        outcome_animals_affected,
        reaction_animals_affected
    )
    SELECT 
        row_number() over(),
        INC.aer,
        REA.reaction_id,
        OUC.outcome_id,
        DW_DRG.drug_id,
        INC.primary_reporter,
        INC.total_animals_affected,
        INC.total_animals_treated,
        INC.onset_date,
        INC.receive_date,
        INC.treated_for_ae,
        INC.time_between_exposure_and_onset, 
        INC.health_assessment_prior_to_exposure_condition,
        INC.serious_ae,
        OUC.outcome_animals_affected,
        REA.reaction_animals_affected
      FROM temp.incident INC
	  INNER JOIN temp.outcome OUC
	  ON INC.p_record_id = OUC.p_record_id
	  INNER JOIN temp.reaction REA
	  ON INC.p_record_id = REA.p_record_id
	  INNER JOIN dw.Dim_Drug DW_DRG
      ON DW_DRG.active_ingredient_name = ACT.active_ingredient_name
   
    
    """
    
    cursor.execute(fact_incident_sql)