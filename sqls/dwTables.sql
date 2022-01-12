-- CREATE Schema IF NOT EXISTS dw;
DROP TABLE if exists dw.date;
DROP TABLE if exists dw.reaction;
DROP TABLE if exists dw.animal;
DROP TABLE if exists dw.incident;
DROP TABLE if exists dw.active_ingredient;
DROP TABLE if exists dw.outcome;
DROP TABLE if exists dw.drug;
DROP TABLE if exists dw.fact;

CREATE TABLE dw.reaction(
    reaction_id                 VARCHAR(512),
    veddra_version              VARCHAR(512),
    veddra_term_code            VARCHAR(512),
    number_of_animals_affected  VARCHAR(512),
    veddra_term_name            VARCHAR(512)
);

CREATE TABLE dw.animal(
    animal_id                           VARCHAR(512),
    species 	                        VARCHAR(512),
    gender 	                            VARCHAR(512),
    female_animal_physiological_status 	VARCHAR(512),
    age                                 DECIMAL(21,6),
    age_unit 	                        VARCHAR(512),
    "weight_kg"    	                    DECIMAL(21,6),
    is_crossbred 	                    VARCHAR(512),
    breed_component 	                VARCHAR(512),
    reproductive_status 	            VARCHAR(512)
);

CREATE TABLE dw.active_ingredient(
    "ingredient_id" VARCHAR(64),
    "drugID" VARCHAR(8),
    "name" VARCHAR(256),
    "dose_fraction" DECIMAL(21,6),
    "dose_unit" VARCHAR(128)
);

CREATE TABLE dw.drug(
    drug_id                             VARCHAR(512),
    "route"                             VARCHAR(64),
    dosage_form                         VARCHAR(512),
    used_according_to_label             BOOLEAN,
    off_label_use                       VARCHAR(512),
    first_exposure_date                 VARCHAR(512),
    last_exposure_date                  VARCHAR(512),
    administered_by                     VARCHAR(512),
    previous_exposure_to_drug           BOOLEAN,
    previous_ae_to_drug                 BOOLEAN,
    frequency_of_administration_value   VARCHAR(512),
    frequency_of_administration_unit    VARCHAR(512),
    ae_abated_after_stopping_drug       VARCHAR(512),
    ae_reappeared_after_resuming_drug   VARCHAR(512)
);

CREATE TABLE dw.incident(
    aer                                             VARCHAR(512),
    receive_date                                    DATE,
    animals_affected                                VARCHAR(512),
    animals_treated                                 VARCHAR(512),
    health_assessment_prior_to_exposure_condition   VARCHAR(512),
    onset_date                                      VARCHAR(512),
    time_between_exposure_and_onset                 VARCHAR(512),
    treated_for_ae                                  BOOLEAN
);

CREATE TABLE dw.outcome(
    outcome_id                          VARCHAR(512),
    outcome_medical_status              VARCHAR(512),
    outcome_number_of_animals_affected  VARCHAR(512)
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
    reaction_id     VARCHAR(512),
    animal_id       VARCHAR(512),
    aer             VARCHAR(512),
    drug_id         VARCHAR(512),
    outcome_id      VARCHAR(512)
);
