# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 10:18:54 2022

@author: pgk
"""

import psycopg2

connection = psycopg2.connect(host='localhost',
                                            database='vets_dw',
                                            user='postgres',
                                            password='password')
connection.autocommit = True
cursor = connection.cursor()

cursor.execute('CREATE Schema IF NOT EXISTS temp')
cursor.execute('CREATE Schema IF NOT EXISTS dw')


TEMPTABLES ='''
DROP TABLE if exists temp.reaction;
DROP TABLE if exists temp.animal;
DROP TABLE if exists temp.incident;
DROP TABLE if exists temp.outcome;
DROP TABLE if exists temp.drug;
DROP TABLE if exists temp.active_ingredient;

CREATE TABLE temp.active_ingredient(
    p_record_id            VARCHAR(128),
    ingredient_id          VARCHAR(128),
    active_ingredient_name VARCHAR(256)
);

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
    age                                 DECIMAL(21,6),
    age_unit 	                        VARCHAR(128),
    "weight_kg"    	                    DECIMAL(21,6),
    is_crossbred 	                    VARCHAR(128),
    breed_component 	                VARCHAR(640),
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
    ae_abated_after_stopping_drug       VARCHAR(128),
    ae_reappeared_after_resuming_drug   VARCHAR(128)
);

CREATE TABLE temp.incident(
    p_record_id                                     VARCHAR(128),
    incident_id                                     VARCHAR(128),
    primary_reporter                                VARCHAR(128),
    receive_date                                    DATE,
    animals_affected                                NUMERIC,
    animals_treated                                 NUMERIC,
    health_assessment_prior_to_exposure_condition   VARCHAR(128),
    onset_date                                      VARCHAR(128),
    treated_for_ae                                  BOOLEAN,
    time_between_exposure_and_onset                 VARCHAR(64),
    serious_ae                                      VARCHAR(8)
);

CREATE TABLE temp.outcome(
    p_record_id                         VARCHAR(128),
    outcome_id                          VARCHAR(128),
    outcome_medical_status              VARCHAR(128),
    outcome_number_of_animals_affected  NUMERIC
);
'''
cursor.execute(TEMPTABLES)




DWTABLES='''

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
    serious_ae                                      BOOLEAN,
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
    ae_abated_after_stopping_drug       BOOLEAN,
    ae_reappeared_after_resuming_drug   BOOLEAN
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
'''
cursor.execute(DWTABLES)
#Close cursor and connection
cursor.close()
connection.close()