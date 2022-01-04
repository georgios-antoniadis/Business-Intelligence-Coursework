
import requests
import psycopg2
import json


connection_string = 'postgresql://postgres:sa@localhost:5432/vets_dw'

connection = psycopg2.connect(connection_string)
connection.autocommit = True

cursor = connection.cursor()

insert_qry = """
INSERT INTO raw.raw(unique_aer_id_number, raw_data) VALUES (%s, %s)
"""

def fetch_data():
    
    url = 'https://api.fda.gov/animalandveterinary/event.json?limit=50'
    
    response = requests.get(url)
    
    yield response.json().get('results')
    
    #print(response.links)
    
    while response.links.get('next').get('url') is not None:
        url = response.links.get('next').get('url')
        response = requests.get(url)
        yield response.json().get('results')
        #print(url)


for page in fetch_data():
    for result in page:
        cursor.execute(insert_qry, (result.get('unique_aer_id_number'), json.dumps(result)))


cursor.close()
connection.close()

#if __name__ == "__main__"
#    fetch_data()
    

