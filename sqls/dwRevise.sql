CREATE Schema IF NOT EXISTS dw;
DROP TABLE if exists dw.Dim_Animal;
DROP TABLE if exists dw.Dim_Outcome;
DROP TABLE if exists dw.Dim_Reaction;
DROP TABLE if exists dw.Dim_Drug;
DROP TABLE if exists dw.Dim_Date;
DROP TABLE if exists dw.Fact_Animal;
DROP TABLE if exists dw.Fact_Incident;
DROP TABLE if exists dw.Fact_Drug;

CREATE TABLE dw.Dim_Animal(
    animal_id                 VARCHAR(128),
    species                   VARCHAR(128)
);

CREATE TABLE dw.Fact_animal(
    aer                         VARCHAR(128),
    animal_id                   VARCHAR(128),
    gender 	                    VARCHAR(128),
    age                         DECIMAL(21,6),
    age_unit                    VARCHAR(128),
    "weight_kg"    	            DECIMAL(21,6),
    is_crossbred 	            BOOLEAN,
    breed_component 	        VARCHAR(640),
    reproductive_status 	    VARCHAR(128)
);

CREATE TABLE dw.Dim_Outcome(
    outcome_id               VARCHAR(128),
    outcome_medical_status   VARCHAR(128)
);

CREATE TABLE dw.Dim_Reaction(
    reaction_id                 VARCHAR(128),
    veddra_version              VARCHAR(128),
    veddra_term_code            VARCHAR(128),
    veddra_term_name            VARCHAR(128)
);

CREATE TABLE dw.Fact_Incident(
    aer                                             VARCHAR(128),
    reaction_id                                     VARCHAR(128),
    outcome_id                                      VARCHAR(128),
    drug_id                                         VARCHAR(256),
    primary_reporter                                VARCHAR(128),
    total_animals_affected                          NUMERIC,
    total_animals_treated                           NUMERIC,
    onset_date                                      DATE,
    receive_date                                    DATE,
    treated_for_ae                                  BOOLEAN,
    time_between_exposure_and_onset                 VARCHAR(128),
    health_assessment_prior_to_exposure_condition   VARCHAR(128),
    serious_ae                                      VARCHAR(128),
    outcome_animals_affected                        NUMERIC,
    reaction_animals_affected                       NUMERIC
);

CREATE TABLE dw.Fact_Drug(
    aer                                 VARCHAR(128),
    drug_id                             VARCHAR(128),
    "route"                             VARCHAR(64),
    dosage_form                         VARCHAR(128),
    used_according_to_label             BOOLEAN,
    off_label_use                       VARCHAR(128),
    first_exposure_date                 DATE,
    last_exposure_date                  DATE,
    administered_by                     VARCHAR(128),
    previous_exposure_to_drug           BOOLEAN,
    previous_ae_to_drug                 BOOLEAN,
    frequency_of_administration_value   NUMERIC,
    frequency_of_administration_unit    VARCHAR(128),
    ae_abated_after_stopping_drug       VARCHAR(128),
    ae_reappeared_after_resuming_drug   VARCHAR(128)
);


CREATE TABLE dw.Dim_Drug(
    drug_id                     VARCHAR(128),
    active_ingredient_name      VARCHAR(256)
);

CREATE TABLE dw.Dim_Date(
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