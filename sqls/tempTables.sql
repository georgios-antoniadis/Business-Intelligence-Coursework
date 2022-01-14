--CREATE Schema IF NOT EXISTS temp;
DROP TABLE if exists temp.reaction;
DROP TABLE if exists temp.animal;
DROP TABLE if exists temp.incident;
DROP TABLE if exists temp.outcome;
DROP TABLE if exists temp.drug;
DROP TABLE if exists temp.active_ingredient;

CREATE TABLE temp.active_ingredient(
    p_record_id            VARCHAR(128),
    ingredient_id          VARCHAR(128),
    active_ingredient_name VARCHAR(128),
    dose_fraction          NUMERIC,
    dose_unit              VARCHAR(128)
)

CREATE TABLE temp.reaction(
    p_record_id                 VARCHAR(128),
    reaction_id                 VARCHAR(128),
    veddra_version              VARCHAR(128),
    veddra_term_code            VARCHAR(128),
    veddra_term_name            VARCHAR(128),
    number_of_animals_affected  NUMERIC
);

CREATE TABLE temp.animal(
    p_record_id                         VARCHAR(128),
    animal_id                           VARCHAR(128),
    species 	                        VARCHAR(128),
    gender 	                            VARCHAR(128),
    female_animal_physiological_status 	VARCHAR(128),
    age                                 DECIMAL(21,6),
    age_unit 	                        VARCHAR(128),
    "weight_kg"    	                    DECIMAL(21,6),
    is_crossbred 	                    VARCHAR(128),
    breed_component 	                VARCHAR(128),
    reproductive_status 	            VARCHAR(128)
);

CREATE TABLE temp.drug(
    p_record_id                         VARCHAR(128),
    drug_id                             VARCHAR(128),
    "route"                             VARCHAR(64),
    dosage_form                         VARCHAR(128),
    used_according_to_label             BOOLEAN,
    off_label_use                       VARCHAR(128),
    first_exposure_date                 VARCHAR(128),
    last_exposure_date                  VARCHAR(128),
    administered_by                     VARCHAR(128),
    previous_exposure_to_drug           BOOLEAN,
    previous_ae_to_drug                 BOOLEAN,
    frequency_of_administration_value   VARCHAR(128),
    frequency_of_administration_unit    VARCHAR(128),
    dose_fraction                       NUMERIC,
    dose_unit                           VARCHAR(128),
    ae_abated_after_stopping_drug       VARCHAR(128),
    ae_reappeared_after_resuming_drug   VARCHAR(128),
    active_ingredient_name              VARCHAR(128)
);

CREATE TABLE temp.incident(
    p_record_id                                     VARCHAR(128),
    incident_id                                     VARCHAR(128),
    receive_date                                    DATE,
    animals_affected                                NUMERIC,
    animals_treated                                 NUMERIC,
    health_assessment_prior_to_exposure_condition   VARCHAR(128),
    onset_date                                      VARCHAR(128),
    treated_for_ae                                  BOOLEAN
);

CREATE TABLE temp.outcome(
    p_record_id                         VARCHAR(128),
    outcome_id                          VARCHAR(128),
    outcome_medical_status              VARCHAR(128),
    outcome_number_of_animals_affected  VARCHAR(128)
);

