def update_fact_animal(cursor):
    update_fact_animal_sql = """
    UPDATE dw.Fact_Animal
    SET
    animal_id = DA.animal_id
    FROM
    dw.Dim_Animal DA
    WHERE
    dw.Fact_Animal.animal_id = DA.species;
    """

    cursor.execute(update_fact_animal_sql)

def update_fact_drug(cursor):
    update_fact_drug_sql = """
    UPDATE dw.Fact_Drug
    SET
    drug_id = DD.drug_id
    FROM
    dw.Dim_Drug DD
    WHERE
    dw.Fact_Drug.drug_id = DD.active_ingredient_name;
    """
    cursor.execute(update_fact_drug_sql)


def update_fact_incident(cursor):
    update_fact_incident_drug = """
    UPDATE dw.Fact_Incident
    SET
    drug_id = DD.drug_id
    FROM
    dw.Dim_Drug DD
    WHERE
    dw.Fact_Incident.drug_id = DD.active_ingredient_name;
    """
    cursor.execute(update_fact_incident_drug)

    ###################################################################

    update_fact_incident_outcome = """
    UPDATE dw.Fact_Incident
    SET
    outcome_id = DT.outcome_id
    FROM
    dw.Dim_Outcome DT
    WHERE
    dw.Fact_Incident.outcome_id = DT.outcome_medical_status;
    """
    cursor.execute(update_fact_incident_outcome)

    ###################################################################

    update_fact_incident_reaction= """
    UPDATE dw.Fact_Incident
    SET
    reaction_id = DR.reaction_id
    FROM
    dw.Dim_Reaction DR
    WHERE
    dw.Fact_Incident.reaction_id = DR.veddra_term_name;

    """

    cursor.execute(update_fact_incident_reaction)