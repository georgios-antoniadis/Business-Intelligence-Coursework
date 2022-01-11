CREATE Schema IF NOT EXISTS staging;

DROP TABLE IF EXISTS staging.FdaApiActiveIngredient;

CREATE TABLE IF NOT EXISTS staging.FdaApiActiveIngredient
(
    "p_recordID" VARCHAR(64)
    ,"Period" VARCHAR(8)
    ,"drugID" VARCHAR(8)
    ,"name" VARCHAR(256)
    ,"dose.numerator" DECIMAL(21,6)
    ,"dose.numerator_unit" VARCHAR(128)
    ,"dose.denominator" DECIMAL(21,6)
    ,"dose.denominator_unit" VARCHAR(128)

);

DROP TABLE IF EXISTS staging.FdaApiDrug;

CREATE TABLE IF NOT EXISTS staging.FdaApiDrug
(
    "p_recordID"  VARCHAR(64)
    ,"Period" VARCHAR(8)
    ,"drugID" VARCHAR(8)
    ,"route" VARCHAR(64)
    ,"brand_name" VARCHAR(128)
    ,"dosage_form" VARCHAR(128)
    ,"atc_vet_code" VARCHAR(128)
    ,"manufacturer.name" VARCHAR(128)
    ,"manufacturer.registration_number" VARCHAR(128)
    ,"used_according_to_label" VARCHAR(128)
    ,"off_label_use" VARCHAR(128)
    ,"lot_number" VARCHAR(128)
    ,"first_exposure_date" VARCHAR(128)
    ,"last_exposure_date" VARCHAR(128)
    ,"administered_by" VARCHAR(128)
    ,"previous_exposure_to_drug" VARCHAR(128)
    ,"previous_ae_to_drug" VARCHAR(128)
    ,"product_ndc"  VARCHAR(128)
    ,"frequency_of_administration.value" VARCHAR(128)
    ,"frequency_of_administration.unit" VARCHAR(128)
    ,"dose.numerator" DECIMAL(21,6)
    ,"dose.numerator_unit" VARCHAR(128)
    ,"dose.denominator" DECIMAL(21,6)
    ,"dose.denominator_unit" VARCHAR(128)
    ,"ae_abated_after_stopping_drug" VARCHAR(128)
    ,"ae_reappeared_after_resuming_drug" VARCHAR(128)
    ,"lot_expiration" VARCHAR(128)
    ,"number_of_items_returned" VARCHAR(128)
    ,"manufacturing_date" VARCHAR(128)
    ,"number_of_defective_items" VARCHAR(128)
    );

DROP TABLE IF EXISTS staging.FdaApiOutcome;

CREATE TABLE IF NOT EXISTS staging.FdaApiOutcome
(
    "p_recordID"         VARCHAR(64)
    ,"Period"    VARCHAR(8)
    ,"medical_status"  VARCHAR(64)
    ,"number_of_animals_affected" INT
);

DROP TABLE IF EXISTS staging.FdaApiReaction;

CREATE TABLE IF NOT EXISTS staging.FdaApiReaction
    (
    "p_recordID"         VARCHAR(64)
    ,"Period"    VARCHAR(8)
    ,"veddra_version" VARCHAR(128)--INT
    ,"veddra_term_code" VARCHAR(128) --INT
    ,"veddra_term_name" VARCHAR(128)
    ,"number_of_animals_affected" VARCHAR(64)-- INT
    ,"accuracy" VARCHAR(64)

);

DROP TABLE IF EXISTS staging.FdaApiIncident;

CREATE TABLE IF NOT EXISTS staging.FdaApiIncident
(
"unique_aer_id_number"	VARCHAR(256)
,"Period"	VARCHAR(8)
,"original_receive_date"	VARCHAR(256)
,"number_of_animals_affected"	VARCHAR(256)
,"primary_reporter"	VARCHAR(256)
,"number_of_animals_treated"	VARCHAR(256)
,"onset_date"	VARCHAR(256)
,"report_id"	VARCHAR(256)
,"type_of_information"	VARCHAR(256)
,"receiver.organization"	VARCHAR(256)
,"receiver.street_address"	VARCHAR(256)
,"receiver.city"	VARCHAR(256)
,"receiver.state"	VARCHAR(8)
,"receiver.postal_code"	VARCHAR(8)
,"receiver.country"	VARCHAR(256)
,"health_assessment_prior_to_exposure.assessed_by"	VARCHAR(256)
,"animal.species"	VARCHAR(256)
,"animal.gender"	VARCHAR(256)
,"animal.female_animal_physiological_status"	VARCHAR(256)
,"animal.age.min"	DECIMAL(21,6)
,"animal.age.unit"	VARCHAR(256)
,"animal.age.qualifier"	VARCHAR(256)
,"animal.weight.min"	DECIMAL(21,6)
,"animal.weight.unit"	VARCHAR(256)
,"animal.weight.qualifier"	VARCHAR(256)
,"animal.breed.is_crossbred"	VARCHAR(256)
,"animal.breed.breed_component"	VARCHAR(256)
,"animal.age.max"	DECIMAL(21,6)
,"animal.weight.max"	DECIMAL(21,6)
,"animal.reproductive_status"	VARCHAR(256)
,"treated_for_ae"	VARCHAR(8)
,"time_between_exposure_and_onset"	VARCHAR(256)
,"health_assessment_prior_to_exposure.condition"	VARCHAR(256)
,"serious_ae"	VARCHAR(8)
,"secondary_reporter"	VARCHAR(256)
,"duration.value"	VARCHAR(256)
,"duration.unit"	VARCHAR(256)

    );

DROP TABLE IF EXISTS staging.log_table;

CREATE TABLE IF NOT EXISTS staging.Log_Table
(
    "OperationDescription" VARCHAR(64)
   ,"Period" VARCHAR(8)
   ,"RowsNum" INT
   ,"Datetime" VARCHAR(16)
   ,"Timestamp" TIMESTAMP
);