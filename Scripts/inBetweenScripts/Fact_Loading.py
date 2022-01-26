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
    
    
def Load_Fact_Outcome(cursor):
    
    print("Insert data to Fact_Outcome")
    print("")
    
    fact_outcome_sql = """
    INSERT INTO dw.fact_outcome
    (aer, 
     ourcome_id, 
     animals_affected)
     
    SELECT tmpouc.p_record_id, 
    dwouc.outcome_id, 
    tmpouc.outcome_number_of_animals_affected
    FROM temp.outcome tmpouc
    INNER JOIN dw.dim_outcome dwouc
    ON tmpouc.outcome_medical_status = dwouc.outcome_medical_status
    """
    
    cursor.execute(fact_outcome_sql)  
    
    
    
def Load_Fact_Reaction(cursor):
    
    print("Insert data to Fact_Reaction")
    print("")
    
    fact_reaction_sql = """
    INSERT INTO dw.fact_reaction
    (aer, reaction_id, animals_affected)

     SELECT tmprea.p_record_id, dwrea.reaction_id,
        tmprea.number_of_animals_affected
        FROM temp.reaction tmprea
        INNER JOIN dw.dim_reaction dwrea
        ON tmprea.veddra_term_name = dwrea.veddra_term_name
        AND dwrea.veddra_version != 'NaN'   --NaNs in veddra version are doubles
    
    """
    cursor.execute(fact_reaction_sql)  
    
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
     INSERT INTO dw.fact_incident
    (fact_incident_id,
     aer,
     primary_reporter,
     total_animals_affected,
     total_animals_treated,
     onset_date,
     onset_date_key,
     receive_date,
     receive_date_key,
     treated_for_ae,
     time_between_exposure_and_onset,
     health_assessment_prior_to_exposure_condition,
    serious_ae
    )
    
     SELECT
            row_number() over(),
            INC.p_record_id,
            --REA.reaction_id, --dim_reaction_id
            --OUC.outcome_id, -- dim_outcome_id
            INC.primary_reporter,
            INC.animals_affected,
            INC.animals_treated,
            INC.onset_date,
    		to_char(INC.onset_date, 'YYYYMMDD')::integer onset_date_key,
            INC.receive_date,
    		to_char(INC.receive_date, 'YYYYMMDD')::integer receive_date_key,
            INC.treated_for_ae,
            INC.time_between_exposure_and_onset,
            INC.health_assessment_prior_to_exposure_condition,
            CAST(CASE WHEN INC.serious_ae = 'NaN' THEN NULL END AS BOOLEAN)--, --BOOLEAN
            --OUC.outcome_number_of_animals_affected,
            --REA.number_of_animals_affected
          FROM temp.incident INC;
        /*  	INNER JOIN temp.reaction REA
    	  ON INC.p_record_id = REA.p_record_id
    	  LEFT JOIN temp.outcome OUC
    	  ON INC.p_record_id = OUC.p_record_id; */
       
    
    """
    
    cursor.execute(fact_incident_sql)