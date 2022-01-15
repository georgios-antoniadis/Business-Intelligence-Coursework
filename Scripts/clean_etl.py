from table_scripts.drug import drugs
from table_scripts.incident_and_animal import incident_and_animals
from table_scripts.active import active_ingredients
from table_scripts.outcome import outcomes
from table_scripts.reaction import reactions 

import psycopg2

def connect():
    # try:
    connection = psycopg2.connect(host='localhost',
                                            database='vets_dw',
                                            user='postgres',
                                            password='password')
    connection.autocommit = True

    cursor = connection.cursor()

    truncTables = ['temp.reaction',
                    'temp.animal',
                    'temp.incident',
                    'temp.outcome',
                    'temp.drug',
                    'temp.active_ingredient']

    for table in truncTables:
            cursor.execute('TRUNCATE TABLE ' + table)
    
    return cursor, connection

if __name__ == '__main__':
    cursor, connection = connect()
    reactions(cursor)
    outcomes(cursor)
    active_ingredients(cursor)
    drugs(cursor)
    incident_and_animals(cursor) 
    connection.close()
    cursor.close()