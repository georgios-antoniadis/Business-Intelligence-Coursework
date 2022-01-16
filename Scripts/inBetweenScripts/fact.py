def fact_Incident(cursor):
    fact_incident_sql = """
    INSERT INTO dw.Fact_Incident
    (
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

    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute("SELECT * FROM temp.incident")

    temp_incident_results = cursor.fetchall()

    for result in temp_incident_results:
        insert_in_fact_incident = [\
            result[0], #aer
            None, #reaction_id
            None, #outcome_id
            None, #drug_id
            result[2], #primary_reporter
            result[4], #total_affected
            result[5], #total_treated
            result[7], #onset date
            result[3], #receive_date
            result[8], #treated_for_ae
            None, # time_between_exposure_and_onset, 
            result[6], # health_assessment_prior_to_exposure_condition
            None, # serious_ae
            None, # outcome_animals_affected
            None  # reaction_animals_affected
            ]

        cursor.execute(fact_incident_sql,insert_in_fact_incident)

    ##########################################################################
    update_drug = """
    UPDATE dw.Fact_Incident
    SET
    drug_id = AI.active_ingredient_name,
    time_between_exposure_and_onset = AI.time_between_exposure_and_onset
    FROM
    temp.active_ingredient AI
    WHERE
    dw.Fact_Incident.aer = AI.p_record_id;
    """ 

    cursor.execute(update_drug)

    ##########################################################################
    update_outcome = """
    UPDATE dw.Fact_Incident
    SET
    outcome_id = OU.outcome_medical_status,
    outcome_animals_affected = OU.outcome_number_of_animals_affected
    FROM
    temp.outcome OU
    WHERE
    dw.Fact_Incident.aer = OU.p_record_id;
    """ 

    cursor.execute(update_outcome)

    ##########################################################################
    update_reaction = """
    UPDATE dw.Fact_Incident
    SET
    reaction_id = RE.veddra_term_name,
    reaction_animals_affected = RE.number_of_animals_affected
    FROM
    temp.reaction RE
    WHERE
    dw.Fact_Incident.aer = RE.p_record_id;
    """ 

    cursor.execute(update_reaction)