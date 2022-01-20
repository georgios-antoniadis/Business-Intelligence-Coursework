import re
import psycopg2

connection = psycopg2.connect(host='localhost',
                                            database='vets_dw',
                                            user='postgres',
                                            password='password')
connection.autocommit = True
cursor = connection.cursor()

sql = """SELECT "number_of_animals_affected", "animal.breed.breed_component" FROM staging.fdaapiincident"""

cursor.execute(sql)

results = cursor.fetchall()

counter = 0

for row in results: 

    if float(row[0]) > 1:

        breed_component = str(row[1])

        # print(breed_component)

        patBefore = r'\{(.*?)\,'
        patBetween = r'\,(.*?)\,'
        patAfter = r'\{(.*?)\}'

        before = re.findall(patBefore, breed_component)
        between = re.findall(patBetween, breed_component)
        after = re.findall(patAfter, breed_component)

        # Rule for deleting ubnormal entries
        if len(between) > 1 or len(after) > 1:
            print(breed_component)
            counter += 1

print(counter)