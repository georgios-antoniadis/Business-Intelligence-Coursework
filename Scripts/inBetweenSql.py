from inBetweenScripts import Dim_Loading
from inBetweenScripts import Fact_Loading


import psycopg2

def connect():
    # try:
    connection = psycopg2.connect(host='localhost',
                                            database='vets_dw',
                                            user='postgres',
                                            password='sa')
    connection.autocommit = True

    cursor = connection.cursor()

    # truncTables = ['temp.reaction',
    #                 'temp.animal',
    #                 'temp.incident',
    #                 'temp.outcome',
    #                 'temp.drug',
    #                 'temp.active_ingredient']

    # for table in truncTables:
    #         cursor.execute('TRUNCATE TABLE ' + table)
    # print('Truncated tables!')
    
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