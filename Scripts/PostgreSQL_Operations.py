import psycopg2

#============================================================================================================
#CALL THIS FUNCTION TO TRUNCATE TABLES BEFORE LOADING DATA
def truncateTables(dbConnection):
    
    truncTables = ['staging.fdaapiactiveingredient',
                   'staging.fdaapidrug',
                   'staging.fdaapiincident',
                   'staging.fdaapioutcome',
                   'staging.fdaapireaction']
    
    connection = psycopg2.connect(dbConnection)
    connection.autocommit = True
    cursor = connection.cursor()
    
    for table in truncTables:
         cursor.execute('TRUNCATE TABLE ' + table)
    
    #Close cursor and connection
    cursor.close()
    connection.close()

#============================================================================================================
def insertDataToDatabase(dbConnection, insertSQL, inputdf):

    connection = psycopg2.connect(dbConnection)

    connection.autocommit = True
    cursor = connection.cursor()

    for index, datarow in inputdf.iterrows():
        cursor.execute(insertSQL, datarow)


    cursor.close()
    connection.close()
#============================================================================================================    

insert_FdaApiReaction = """
INSERT INTO staging.FdaApiReaction
    (
    "p_recordID"
    ,"Period"
    ,"veddra_version"
    ,"veddra_term_code"
    ,"veddra_term_name"
    ,"number_of_animals_affected"
    ,"accuracy"
    )
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

#============================================================================================================   

insert_FdaApiOutcome = """
INSERT INTO staging.FdaApiOutcome
    (
    "p_recordID"
    ,"Period"
    ,"medical_status"
    ,"number_of_animals_affected"
    )
VALUES (%s, %s, %s, %s)
"""

#============================================================================================================   

insert_FdaApiActiveIngredient = """
INSERT INTO staging.FdaApiActiveIngredient
    ("p_recordID" 
    ,"Period"
    ,"drugID"
    ,"name" 
    ,"dose.numerator" 
    ,"dose.numerator_unit" 
    ,"dose.denominator" 
    ,"dose.denominator_unit"
    )
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

#============================================================================================================   

insert_FdaApiDrug = """
INSERT INTO staging.FdaApiDrug
    ("p_recordID"  
    ,"Period"
    ,"drugID"
    ,"route" 
    ,"brand_name" 
    ,"dosage_form" 
    ,"atc_vet_code"
    ,"manufacturer.name" 
    ,"manufacturer.registration_number" 
    ,"used_according_to_label" 
    ,"off_label_use" 
    ,"lot_number" 
    ,"first_exposure_date" 
    ,"last_exposure_date" 
    ,"administered_by" 
    ,"previous_exposure_to_drug" 
    ,"previous_ae_to_drug" 
    ,"product_ndc"  
    ,"frequency_of_administration.value" 
    ,"frequency_of_administration.unit" 
    ,"dose.numerator" 
    ,"dose.numerator_unit" 
    ,"dose.denominator" 
    ,"dose.denominator_unit" 
    ,"ae_abated_after_stopping_drug" 
    ,"ae_reappeared_after_resuming_drug" 
    ,"lot_expiration" 
    ,"number_of_items_returned" 
    ,"manufacturing_date"
    ,"number_of_defective_items"
    )
VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

#============================================================================================================   

insert_FdaApiIncident = """
INSERT INTO staging.FdaApiIncident
    ( "unique_aer_id_number"
,"Period"
,"original_receive_date"
,"number_of_animals_affected"
,"primary_reporter"
,"number_of_animals_treated"
,"onset_date"
,"report_id"
,"type_of_information"
,"receiver.organization"
,"receiver.street_address"
,"receiver.city"
,"receiver.state"
,"receiver.postal_code"
,"receiver.country"
,"health_assessment_prior_to_exposure.assessed_by"
,"animal.species"
,"animal.gender"
,"animal.female_animal_physiological_status"
,"animal.age.min"
,"animal.age.unit"
,"animal.age.qualifier"
,"animal.weight.min"
,"animal.weight.unit"
,"animal.weight.qualifier"
,"animal.breed.is_crossbred"
,"animal.breed.breed_component"
,"animal.age.max"
,"animal.weight.max"
,"animal.reproductive_status"
,"treated_for_ae"
,"time_between_exposure_and_onset"
,"health_assessment_prior_to_exposure.condition"
,"serious_ae"
,"secondary_reporter"
,"duration.value"
,"duration.unit"   
    )
VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


##############################################################################################


insert_LogTable = """
INSERT INTO staging.Log_Table
    (
    "OperationDescription"
   ,"Period"
   ,"RowsNum"
   ,"Datetime"
   ,"Timestamp"
    )
VALUES (%s, %s, %s, %s, %s)
"""

def insertLogEntry(dbConnection, insertSQL, inputList):
    
    try:
        connection = psycopg2.connect(dbConnection)
    
        connection.autocommit = True
        cursor = connection.cursor()    
           
        cursor.execute(insert_LogTable, inputList)
    
        cursor.close()
        connection.close()

    except Exception as e:
        print("Oops!", e.__class__, "occurred.")