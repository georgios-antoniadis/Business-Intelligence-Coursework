import psycopg2

from inBetweenScripts.animal import dim_Animal, fact_Animal
from inBetweenScripts.rest_of_dim import dim_Outcome, dim_Reaction
from inBetweenScripts.fact import fact_Incident
from inBetweenScripts.update import update_fact_incident, update_fact_animal, update_fact_drug
from inBetweenScripts.drug import dim_Drug, fact_Drug

def connect():
    connection = psycopg2.connect(host='localhost',
                                            database='vets_dw',
                                            user='postgres',
                                            password='password')
    connection.autocommit = True

    cursor = connection.cursor()
    
    print("Connected to database!")
    print("")
    return cursor, connection


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

    print("Creating fact table animal")
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

def dim_Outcome(cursor):

    print("Creating dimesnion table outcome")
    print("")

    dim_outcome_sql = """
    INSERT INTO dw.Dim_Outcome
    ("outcome_id", "outcome_medical_status")

    SELECT row_number() over (ORDER BY outcome_medical_status) 
    AS "outcome_id","outcome_medical_status" FROM temp.outcome
    GROUP BY outcome_medical_status;""" 

    cursor.execute(dim_outcome_sql)

def dim_Reaction(cursor):

    print("Creating dimesnion table reaction")
    print("")

    dim_reaction_sql = """
    INSERT INTO dw.Dim_Reaction
    ("reaction_id", "veddra_version", "veddra_term_code", "veddra_term_name")

    SELECT row_number() over (ORDER BY veddra_term_name) 
    AS "reaction_id", "veddra_version", "veddra_term_code", "veddra_term_name" FROM temp.reaction
    GROUP BY veddra_version, veddra_term_code, veddra_term_name;""" 

    cursor.execute(dim_reaction_sql)


def fact_Incident(cursor):

    print("Creating fact table incident")
    print("")

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
            result[9], # time_between_exposure_and_onset, 
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
    drug_id = AI.active_ingredient_name
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
    p_record_id,
    drug_id, 
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

    print("Creating dimesnion table drug")
    print("")

    dim_reaction_sql = """
    INSERT INTO dw.Dim_Drug
    ("drug_id", "active_ingredient_name")

    SELECT row_number() over (ORDER BY active_ingredient_name) 
    AS "drug_id", "active_ingredient_name" FROM temp.active_ingredient
    GROUP BY active_ingredient_name;""" 

    cursor.execute(dim_reaction_sql)


#############################################################################
# For debugging
#############################################################################

# def reacionAffected(cursor):
#     reaction_sql = r"SELECT * FROM staging.fdaapireaction"
#     cursor.execute(reaction_sql)

#     reaction_result = cursor.fetchall()

#     for reaction in reaction_result:

#         if reaction[5] > 1:
#             print("Number: ", reaction[5])
#             print("Term code : ", reaction[3])



#############################################################################
# UPDATING
#############################################################################

def update_fact_animal(cursor):

    print("Updating fact table animal")
    print("")

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

    print("Updating fact table drug")
    print("")

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

    print("Updating fact table incident")
    print("")

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


if __name__ == '__main__':
    cursor, connection = connect()
    dim_Animal(cursor)
    dim_Outcome(cursor)
    dim_Drug(cursor)
    dim_Reaction(cursor)

    fact_Animal(cursor)
    fact_Incident(cursor)
    fact_Drug(cursor)

    update_fact_animal(cursor)
    update_fact_drug(cursor)

    update_fact_incident(cursor)
