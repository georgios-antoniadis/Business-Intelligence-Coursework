DROP TABLE IS EXISTS dw.Dim_Animal
DROP TABLE IS EXISTS dw.Dim_Reaction
DROP TABLE IS EXISTS dw.Dim_Outcome
DROP TABLE IS EXISTS dw.Dim_Drug
DROP TABLE IS EXISTS dw.Dim_Active_Ingredient
DROP TABLE IS EXISTS dw.Dim_Date
DROP TABLE IS EXISTS dw.Fact_Incident


CREATE TABLE dw.Dim_Animal(
    Animal_id   VARCHAR(128),
    Animal_name VARCHAR --What is that?
);

CREATE TABLE dw.Dim_Reaction(
    Reaction_id                 VARCHAR(128),
    Number_of_animals_affected  VARCHAR(128),
    Veddra_version              VARCHAR(128),
    Veddra_term_code            VARCHAR(128),
    Veddra_term_name            VARCHAR(128)
);

CREATE TABLE dw.Dim_Outcome(
    Outcome_id  VARCHAR(128),
    Outcome_medical_status VARCHAR(128)
);

CREATE TABLE dw.Dim_Drug(
    Drug_id                             VARCHAR(128),
    "Route"                             VARCHAR(128),
    Dosage_form                         VARCHAR(128),
    Used_according_to_label             BOOLEAN,
    Off_label_use                       VARCHAR(128),
    First_exposure_date                 VARCHAR(128),
    Last_exposure_date                  VARCHAR(128),
    Administered_by                     VARCHAR(128),
    Previous_exposure_to_drug           BOOLEAN,
    Previous_ae_to_drug                 BOOLEAN,
    Frequency_of_administration_value   VARCHAR(128),
    Frequency_of_administration_unit    VARCHAR(128),
    Dose_fraction                       NUMERIC,
    Dose_unit                           VARCHAR(128),
    Ae_abated_after_stopping_drug       VARCHAR(128),
    Ae_reappeared_after_resuming_drug   VARCHAR(128),
    Active_ingredient_id                VARCHAR(128)
);

CREATE TABLE dw.Dim_Active_Ingredient(

    Active_ingredient_id    VARCHAR(128),
    Active_ingredient_name  VARCHAR(128)

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


CREATE TABLE Fact_Incident(
    Incident_id                                     VARCHAR(128),
    Animal_id                                       VARCHAR(128),
    Reaction_id                                     VARCHAR(128),
    Outcome_id                                      VARCHAR(128),
    Active_ingredient_id                            VARCHAR(128),
    Drug_id                                         VARCHAR(128),
    Original_receive_date                           VARCHAR(128),
    Number_of_animals_affected                      VARCHAR(128),
    number_of_animals_treated                       VARCHAR(128),
    onset_date                                      DATE,
    Animal_species                                  VARCHAR(128),
    Animal_gender                                   VARCHAR(128),
    Animal_age                                      VARCHAR(128),
    Animal_weight                                   VARCHAR(128),
    Animal_is_crossbred                             VARCHAR(128),
    Animal_breed_component                          VARCHAR(640),
    Animal_reproductive_status                      VARCHAR(128),
    Treated_for_ae                                  BOOLEAN,
    Time_between_exposure_and_onset                 VARCHAR(128),
    Health_assessment_prior_to_exposure_condition   VARCHAR(128),
    Serious_ae                                      VARCHAR(128)

);