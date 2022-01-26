from inBetweenScripts import Dim_Loading
from inBetweenScripts import Fact_Loading


import psycopg2

def connect():
    # try:
    connection = psycopg2.connect(host='localhost',
                                            database='vets_dw',
                                            user='postgres',
                                            password='password')
    connection.autocommit = True

    cursor = connection.cursor()

    truncTables = ['dw.dim_animal',
                    'dw.dim_outcome',
                    'dw.dim_reaction',
                    'dw.dim_date',
                    'dw.dim_drug',
                    'dw.fact_animal',
                    'dw.fact_drug',
                    'dw.fact_incident',
                    'dw.fact_outcome',
                    'dw.fact_reaction']

    for table in truncTables:
            cursor.execute('TRUNCATE TABLE ' + table)
    print('Truncated tables!')
    
    return cursor, connection


if __name__ == '__main__':
    cursor, connection = connect()

    Dim_Loading.Load_Dim_Animal(cursor)
    Dim_Loading.Load_Dim_Date(cursor)
    Dim_Loading.Load_Dim_Drug(cursor)
    Dim_Loading.Load_Dim_Outcome(cursor)
    Dim_Loading.Load_Dim_Reaction(cursor)
    
    Fact_Loading.Load_Fact_Animal(cursor)
    Fact_Loading.fact_Drug(cursor)
    Fact_Loading.fact_Incident(cursor)
    Fact_Loading.Load_Fact_Outcome(cursor)
    Fact_Loading.Load_Fact_Reaction(cursor)