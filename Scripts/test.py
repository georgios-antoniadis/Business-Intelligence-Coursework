from xmlrpc.client import boolean
import psycopg2

connection = psycopg2.connect(host='localhost',
                                            database='vets_dw',
                                            user='postgres',
                                            password='password')
connection.autocommit = True

cursor = connection.cursor()

sql = 'SELECT * FROM staging.FdaApiIncident LIMIT 1000'

cursor.execute(sql)

results = cursor.fetchall()

for res in results:

    if 'true' or 'false' in res[25]:
        print('Is boolean')
        print(res[25])
    elif 'NaN' in res[25]:
        print(res[25])
        print('Is not boolean')
