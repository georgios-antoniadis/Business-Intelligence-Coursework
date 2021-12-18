CREATE Schema IF NOT EXISTS staging;
DROP TABLE if exists staging.reactions;
DROP TABLE if exists staging.receivers;
DROP TABLE if exists staging.incidents;
DROP TABLE if exists staging.active_ingredients;
DROP TABLE if exists staging.animals;


CREATE TABLE staging.reactions
(
    veddraVersion              INT NOT NULL,
    veddraTermCode             INT NOT NULL,
    veddraTermName             VARCHAR() NOT NULL
);

CREATE TABLE staging.receivers
(
    organization                VARCHAR() NOT NULL,
    streetAddress               VARCHAR() NOT NULL,
    veddraTermName              VARCHAR() NOT NULL,
    city                        VARCHAR() NOT NULL,
    state                       VARCHAR() NOT NULL,
    postalCode                  VARCHAR() NOT NULL,
    country                     VARCHAR() NOT NULL
);

CREATE TABLE staging.incidents
(
    unique_aer_id_number            VARCHAR() NOT NULL,
    original_receive_date           DATE NOT NULL,
    number_of_animals_affected      INT NOT NULL,
    primary_reporter                VARCHAR() NOT NULL,
    number_of_animals_treated       INT NOT NULL,
    assessedBy                      VARCHAR() NOT NULL,
    onset_date                      DATE NOT NULL,
    report_id                       VARCHAR() NOT NULL,
    typeOfInformation               VARCHAR() NOT NULL,
    outcomeMedicalStatus            VARCHAR() NOT NULL,
    outcomeNumberOfAnimalsAffected  VARCHAR() NOT NULL

);

CREATE TABLE staging.animals
(
    species         VARCHAR() NOT NULL,
    gender          VARCHAR() NOT NULL,
    ageMin          INT NOT NULL,
    ageMax          INT NOT NULL,
    ageUnit         VARCHAR() NOT NULL,
    ageQualifier    VARCHAR() NOT NULL,
    weightMin       INT NOT NULL,
    weightMax       INT NOT NULL,
    weightUnit      VARCHAR() NOT NULL,
    weightQualifier VARCHAR() NOT NULL,
    isCrossbred     BOOLEAN NOT NULL,
    breedComponent  VARCHAR() NOT NULL,
);