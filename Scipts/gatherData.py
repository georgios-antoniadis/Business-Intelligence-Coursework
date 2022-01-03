import numpy as np
import pandas as pd
import requests
import json
import zipfile, io
import os
import re

downloadURL = 'https://api.fda.gov/download.json'

#Get only the animal and veterinary data and load them in a pandas dataframe
links_df=pd.json_normalize(requests.get(downloadURL).json()['results']['animalandveterinary']['event']['partitions'])

#df manipulations and sorting
links_df.sort_values(by=['display_name'], inplace=True)
links_df.reset_index(drop=True, inplace=True)

print(len(links_df))

for i in range(len(links_df)):
    r = requests.get(links_df['file'][i])
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('AllDataHere')
    res = re.findall(r"\d\d\d\d\w\d",links_df['file'][i])
    if i == len(links_df)-1:#The very last quarter does not have a date in it!
        newPath = 'AllDataHere/all_other.json'
    else:
        newPath = 'AllDataHere/' + res[0] + '.json'
        sourcePath = "AllDataHere/animalandveterinary-event-0001-of-0001.json"
    try: #Renaming and replacing files to update them all!
        os.rename(sourcePath, newPath)
    except FileExistsError:
        os.replace(sourcePath, newPath)

print('Downloaded all', len(links_df), 'files!') #Download check
