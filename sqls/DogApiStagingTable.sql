
CREATE Schema IF NOT EXISTS staging;

DROP TABLE IF EXISTS staging.DogApiData;
CREATE TABLE IF NOT EXISTS staging.DogApiData
(
    id                 INT, --SERIAL NOT NULL PRIMARY KEY,
    name               VARCHAR(64),
    bred_for           VARCHAR(1024),
    breed_group        VARCHAR(64),
    life_span          VARCHAR(32),
    temperament        VARCHAR(1024),
    origin             VARCHAR(64),
    reference_image_id VARCHAR(16),
    weight_imperial    VARCHAR(16),
    weight_metric      VARCHAR(16),
    height_imperial    VARCHAR(16),
    height_metric      VARCHAR(16),
    image_id           VARCHAR(16),
    image_width        INT,
    image_height       INT,
    image_url          VARCHAR(1024),
    country_code       VARCHAR(16),
    description        VARCHAR(1024),
    history            VARCHAR(1024)
);