-- CREATE Schema IF NOT EXISTS dw;
DROP TABLE if exists dw.date;
DROP TABLE if exists dw.reaction;
DROP TABLE if exists dw.animal;
DROP TABLE if exists dw.incident;
DROP TABLE if exists dw.outcome;
DROP TABLE if exists dw.drug;
DROP TABLE if exists dw.fact;

CREATE TABLE dw.reaction(
    reaction_id                 VARCHAR(128),
    veddra_version              VARCHAR(128),
    veddra_term_code            VARCHAR(128),
    number_of_animals_affected  VARCHAR(128),
    veddra_term_name            VARCHAR(128)
);

CREATE TABLE dw.animal(
    animal_id                           VARCHAR(128),
    species 	                        VARCHAR(128),
    gender 	                            VARCHAR(128),
    female_animal_physiological_status 	VARCHAR(128),
    age                                 DECIMAL(21,6),
    age_unit 	                        VARCHAR(128),
    "weight_kg"    	                    DECIMAL(21,6),
    is_crossbred 	                    BOOLEAN,
    breed_component 	                VARCHAR(128),
    reproductive_status 	            VARCHAR(128)
);

CREATE TABLE dw.drug(
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

CREATE TABLE dw.incident(
    aer                                             VARCHAR(128),
    receive_date                                    DATE,
    animals_affected                                NUMERIC,
    animals_treated                                 NUMERIC,
    health_assessment_prior_to_exposure_condition   VARCHAR(128),
    onset_date                                      VARCHAR(128),
    treated_for_ae                                  BOOLEAN
);

CREATE TABLE dw.outcome(
    outcome_id                          VARCHAR(128),
    outcome_medical_status              VARCHAR(128),
    outcome_number_of_animals_affected  VARCHAR(128)
);


CREATE TABLE dw.date(
    date_dim_id              INT NOT NULL,
    date_actual              DATE NOT NULL,
    epoch                    BIGINT NOT NULL,
    day_suffix               VARCHAR(4) NOT NULL,
    day_name                 VARCHAR(9) NOT NULL,
    day_of_week              INT NOT NULL,
    day_of_week_iso          INT NOT NULL,
    day_of_month             INT NOT NULL,
    day_of_quarter           INT NOT NULL,
    day_of_year              INT NOT NULL,
    week_of_month            INT NOT NULL,
    week_of_year             INT NOT NULL,
    week_of_year_iso         CHAR(10) NOT NULL,
    month_actual             INT NOT NULL,
    month_name               VARCHAR(9) NOT NULL,
    month_name_abbreviated   CHAR(3) NOT NULL,
    quarter_actual           INT NOT NULL,
    quarter_name             VARCHAR(9) NOT NULL,
    year_actual              INT NOT NULL,
    year_actual_iso          INT NOT NULL,
    first_day_of_week        DATE NOT NULL,
    last_day_of_week         DATE NOT NULL,
    first_day_of_month       DATE NOT NULL,
    last_day_of_month        DATE NOT NULL,
    first_day_of_quarter     DATE NOT NULL,
    last_day_of_quarter      DATE NOT NULL,
    first_day_of_year        DATE NOT NULL,
    last_day_of_year         DATE NOT NULL,
    mmyyyy                   CHAR(6) NOT NULL,
    mmddyyyy                 CHAR(10) NOT NULL,
    weekend_indr             BOOLEAN NOT NULL
);


CREATE TABLE dw.fact(
    reaction_id     VARCHAR(128),
    animal_id       VARCHAR(128),
    aer             VARCHAR(128),
    drug_id         VARCHAR(128),
    outcome_id      VARCHAR(128)
);
