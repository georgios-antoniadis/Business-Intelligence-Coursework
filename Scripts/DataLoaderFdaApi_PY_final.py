import numpy as np # library to handle data in a vectorized manner
import pandas as pd # library for data analsysis
import datetime as datetime

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import requests
import json
import zipfile, io #libraries to save zip files in project directory

import PostgreSQL_Operations

#now = datetime.datetime.now() #+ datetime.timedelta(hours=2) #3 during summertime
print('01.Operation started',datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))

connection_string = 'postgresql://postgres:sa@localhost:5432/vets_dw'
######
#Download url for the required json files
downloadURL = 'https://api.fda.gov/download.json'


PostgreSQL_Operations.insertLogEntry(connection_string,
                                     PostgreSQL_Operations.insert_LogTable,
                                     ['Operation started'
                                      ,''
                                      ,0
                                      ,datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                                      ,datetime.datetime.now()])

####
#Get only the animal and veterinary data and load them in a pandas dataframe
links_df=pd.json_normalize(requests.get(downloadURL).json()['results']['animalandveterinary']['event']['partitions'])

#dataframe manipulations and sorting
links_df.sort_values(by=['display_name'], inplace=True)
links_df.reset_index(drop=True, inplace=True)

#============================================================================================================
#links_df=links_df[:][0:20].reset_index()
#links_df=links_df[:][20:40].reset_index()
#links_df=links_df[:][40:60].reset_index() #CHECK THE PERIODS FROM 1997Q1 TO 1998Q4
#links_df=links_df[:][60:80].reset_index()
#links_df=links_df[:][80:100].reset_index()
#links_df=links_df[:][100:110].reset_index() #ERROR ON 108TH (LARGE VALUE) RERUN 108 - 109
#links_df=links_df[:][108:110].reset_index()
#links_df=links_df[:][110:111].reset_index()
#links_df=links_df[:][111:112].reset_index()
#links_df=links_df[:][112:114].reset_index()
#links_df=links_df[:][114:120].reset_index()
#links_df=links_df[:][120:124].reset_index()
#links_df=links_df[:][124:128].reset_index()
#links_df=links_df[:][128:132].reset_index()
#------------>>links_df=links_df[:][132:136].reset_index() THIS IS THE LAST RUN
#links_df=links_df[:][136:139].reset_index()
#links_df=links_df[:][0:5].reset_index()


#links_df=links_df[:][128:129].reset_index()
#links_df = links_df.head(1)
#============================================================================================================
#from zipfile import ZipFile
# Create a ZipFile Object and load sample.zip in it
#with ZipFile(url, 'r') as zipObj:
   # Extract all the contents of zip file in current directory
#   zipObj.extractall()

#https://stackoverflow.com/questions/5710867/downloading-and-unzipping-a-zip-file-without-writing-to-disk

####################################################################### 
#######################################################################    
def getAndExtract(dataframe):
    
    r = requests.get(dataframe) #links_df['file'][120]
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

####################################################################### 
####################################################################### 


####################################################################### 
####################################################################### 
def openAndLoad(jsonfile):
    
    f = open(jsonfile)#'animalandveterinary-event-0001-of-0001.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    data['results']
    return pd.json_normalize(data['results'])
####################################################################### 
####################################################################### 


####################################################################### 
####################################################################### 
def createDataFrames(dfcolumns):
       
    return pd.DataFrame(columns=dfcolumns)
####################################################################### 
####################################################################### 

reaction_df_columns=['p_recordID','Period','veddra_version','veddra_term_code','veddra_term_name',
                                    'number_of_animals_affected','accuracy']
    
outcome_df_columns = ['p_recordID','Period','medical_status','number_of_animals_affected'] 
   

    
drug_df_columns = ['p_recordID','Period','drugID','route','brand_name','dosage_form','atc_vet_code',
                                    'manufacturer.name','manufacturer.registration_number',
                                    'used_according_to_label','off_label_use','lot_number','first_exposure_date',
                                    'last_exposure_date','administered_by','previous_exposure_to_drug',
                                    'previous_ae_to_drug','product_ndc','frequency_of_administration.value',
                                    'frequency_of_administration.unit','dose.numerator','dose.numerator_unit',
                                    'dose.denominator','dose.denominator_unit','ae_abated_after_stopping_drug',
                                    'ae_reappeared_after_resuming_drug','lot_expiration','number_of_items_returned',
                                    'manufacturing_date','number_of_defective_items']
    
active_ingredient_df_columns = ['p_recordID','Period','drugID','name','dose.numerator','dose.numerator_unit',
                                                  'dose.denominator','dose.denominator_unit']
    
df_columns=['unique_aer_id_number','Period','original_receive_date','number_of_animals_affected',
                             'primary_reporter','number_of_animals_treated','onset_date','report_id','type_of_information',
                             'receiver.organization','receiver.street_address','receiver.city','receiver.state',
                             'receiver.postal_code','receiver.country','health_assessment_prior_to_exposure.assessed_by',
                             'animal.species','animal.gender','animal.female_animal_physiological_status','animal.age.min',
                             'animal.age.unit','animal.age.qualifier','animal.weight.min','animal.weight.unit',
                             'animal.weight.qualifier','animal.breed.is_crossbred','animal.breed.breed_component',
                             'animal.age.max','animal.weight.max','animal.reproductive_status','treated_for_ae',
                             'time_between_exposure_and_onset','health_assessment_prior_to_exposure.condition',
                             'serious_ae','secondary_reporter','duration.value','duration.unit']


reaction_df = createDataFrames(reaction_df_columns)
outcome_df = createDataFrames(outcome_df_columns)
drug_df = createDataFrames(drug_df_columns)
active_ingredient_df = createDataFrames(active_ingredient_df_columns)
incident_df = createDataFrames(df_columns)


############################################
#THIS LINE WILL BE COMMENTED DUE TO PARTIAL DATA LOADING
#IT IS NECESSARY IN A FULL LOADING CYCLE
#PostgreSQL_Operations.truncateTables(connection_string)
############################################


for linksIndex, LinksRow in links_df.iterrows():
    
    #============================================================================================================
    #print(LinksRow['file'])
    #print('=======================================================')
    #print(linksIndex, LinksRow)
    #print('=======================================================')
    #============================================================================================================

    getAndExtract(links_df.iloc[linksIndex]['file'])
    periodValue = links_df['display_name'][linksIndex][0:4]+links_df['display_name'][linksIndex][5:7]

    incident_df_temp = openAndLoad('animalandveterinary-event-0001-of-0001.json')

    #COMMENT THIS FOR FULL LOAD
    ############################################
    #incident_df_temp = incident_df_temp.head(100)
    ############################################
    
    for index, row in incident_df_temp.iterrows():
        #assign the unique aer number to a variable
        unique_aer_id_number = incident_df_temp['unique_aer_id_number'][index]

        if type(incident_df_temp.loc[index,'reaction']) != float:

            #normalize the current line's data and load them in the temp dataframe
            reaction_df_temp = pd.json_normalize(incident_df_temp.loc[index,'reaction'])

            #append the column with the unique aer number
            reaction_df_temp['p_recordID'] = unique_aer_id_number
            reaction_df_temp['Period'] = periodValue

            #Append rows to the final dataframe
            reaction_df = reaction_df.append(reaction_df_temp)

        if type(incident_df_temp.loc[index,'outcome']) != float:
            outcome_df_temp = pd.json_normalize(incident_df_temp.loc[index,'outcome'])
            outcome_df_temp['p_recordID'] = unique_aer_id_number
            outcome_df_temp['Period'] = periodValue
            outcome_df = outcome_df.append(outcome_df_temp)

        if type(incident_df_temp.loc[index, 'drug']) != float:
            drug_df_temp = pd.json_normalize(incident_df_temp.loc[index,'drug'])
            
            
            for drIndex, drRow in drug_df_temp.iterrows():
                
                drug_df_temp.loc[drIndex,'p_recordID'] = unique_aer_id_number
                drug_df_temp.loc[drIndex,'Period']= periodValue
                drug_df_temp.loc[drIndex,'drugID'] = 'DRUG' + str(drIndex+1).zfill(3)
 
                drug_df = drug_df.append(drug_df_temp.loc[drIndex, drug_df_temp.columns!='active_ingredients'])

                active_ingredient_df_temp = pd.json_normalize(incident_df_temp.loc[index,'drug'][drIndex],record_path=['active_ingredients'])
                active_ingredient_df_temp['p_recordID'] = unique_aer_id_number
                active_ingredient_df_temp['Period'] = periodValue
                active_ingredient_df_temp['drugID'] = 'DRUG' + str(drIndex+1).zfill(3)
                active_ingredient_df = active_ingredient_df.append(active_ingredient_df_temp)
        
    #this is already normalized and can be appended to the dataframe without looping
    #actually this operation is much faster that loading one line per iteration
    incident_df_temp['Period'] = periodValue
    incident_df = incident_df.append(incident_df_temp[[icol for icol in list(incident_df_temp.columns) if icol not in ['reaction','drug','outcome']]])
    
    #============================================================================================================
    #print('02.DataFrames created beginning loading',periodValue,datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
    #============================================================================================================
    PostgreSQL_Operations.insertLogEntry(connection_string,
                                         PostgreSQL_Operations.insert_LogTable,
                                         ['DataFrames created beginning loading'
                                          ,periodValue
                                          ,0
                                          ,datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                                          ,datetime.datetime.now()])
    
    #Start loading dataframes to staging tables
    PostgreSQL_Operations.insertDataToDatabase(connection_string, 
                                               PostgreSQL_Operations.insert_FdaApiReaction, 
                                               reaction_df)
    
    PostgreSQL_Operations.insertDataToDatabase(connection_string, 
                                               PostgreSQL_Operations.insert_FdaApiOutcome, 
                                               outcome_df)
    
    PostgreSQL_Operations.insertDataToDatabase(connection_string, 
                                               PostgreSQL_Operations.insert_FdaApiActiveIngredient, 
                                               active_ingredient_df)
    
    PostgreSQL_Operations.insertDataToDatabase(connection_string, 
                                               PostgreSQL_Operations.insert_FdaApiDrug, 
                                               drug_df)
    
    PostgreSQL_Operations.insertDataToDatabase(connection_string, 
                                               PostgreSQL_Operations.insert_FdaApiIncident, 
                                               incident_df)
    
    #============================================================================================================
    print('03.Period finished loading',periodValue,incident_df.shape[0],datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
    #============================================================================================================
    PostgreSQL_Operations.insertLogEntry(connection_string,
                                         PostgreSQL_Operations.insert_LogTable,
                                         ['Period finished loading'
                                          ,periodValue
                                          ,incident_df.shape[0]
                                          ,datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                                          ,datetime.datetime.now()])
    
    
    #####################################################
    #DID NOT WORK AS EXPECTED. HUNG WITHOUT ERROR MESSAGE
    #Initialize dataframes by deleting the inserted rows
    #incident_df.drop(incident_df.index, inplace=True)
    #reaction_df.drop(reaction_df.index, inplace=True)
    #outcome_df.drop(outcome_df.index, inplace=True)
    #active_ingredient_df.drop(active_ingredient_df.index, inplace=True)
    #drug_df.drop(drug_df.index, inplace=True)
    #####################################################
 
    #============================================================================================================
    #print('reaction_df rows:',reaction_df.shape[0])
    #print('outcome_df rows:',outcome_df.shape[0])
    #print('drug_df rows:',drug_df.shape[0])
    #print('active_ingredient_df rows:',active_ingredient_df.shape[0])
    #print('incident_df rows:',incident_df.shape[0])
    #============================================================================================================
    
    reaction_df = createDataFrames(reaction_df_columns)
    outcome_df = createDataFrames(outcome_df_columns)
    drug_df = createDataFrames(drug_df_columns)
    active_ingredient_df = createDataFrames(active_ingredient_df_columns)
    incident_df = createDataFrames(df_columns)
    
    #============================================================================================================
    #print('04.DataFrames initialization completed',datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
    #============================================================================================================
    PostgreSQL_Operations.insertLogEntry(connection_string,
                                         PostgreSQL_Operations.insert_LogTable,
                                         ['DataFrames initialization completed'
                                          ,''
                                          ,0
                                          ,datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                                          ,datetime.datetime.now()])

    #============================================================================================================    
    #print('reaction_df rows:',reaction_df.shape[0])
    #print('outcome_df rows:',outcome_df.shape[0])
    #print('drug_df rows:',drug_df.shape[0])
    #print('active_ingredient_df rows:',active_ingredient_df.shape[0])
    #print('incident_df rows:',incident_df.shape[0])
    #============================================================================================================



#============================================================================================================
print('05.Operation finished',datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
#============================================================================================================
PostgreSQL_Operations.insertLogEntry(connection_string,
                                     PostgreSQL_Operations.insert_LogTable,
                                     ['Operation finished'
                                      ,''
                                      ,0
                                      ,datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                                      ,datetime.datetime.now()])