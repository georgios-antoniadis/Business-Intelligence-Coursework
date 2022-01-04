
CREATE Schema IF NOT EXISTS raw;

DROP TABLE IF EXISTS raw.raw;
CREATE TABLE IF NOT EXISTS raw.raw
(
    unique_aer_id_number VARCHAR(64)
    ,raw_data VARCHAR
);