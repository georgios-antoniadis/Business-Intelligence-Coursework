This project deploys a fully operational Business Intelligence system with a complete local database involving a staging, a temporary and a data warehouse environment. 

The project comes with fully automated scripts for downloading the data, running the ETL pipeline and loading the data into the DW environment. 

Requirements (Please visit the softwares' websites and follow the installation instructions):
- Python 3 (any version) https://www.python.org/downloads/ 

- PostgresSQL (version installed on machine during development 12+214) https://www.postgresql.org/download/

To have a fully operational copy of the project installed locally on your machine please follow these steps:

1) Download a postgresql database management tool Data Grip. (For the purposes of this project we chose DataGrip which is also the project that this tutorial will be based upon. Should you choose an alternative one, please refer to the software's documentation for more informatio)


2) Create a new postgres data source by clicking on the plus icon (Located in the 'Database Explorer' tab) and then Data Source>PostgreSQL

2.1) Once inside the pop-up window navigate to the 'General' tab (It should be the default opening tab) and enter the following:

- Database: vets_dw
- Host: localhost 
- User: postgres 
- Password: password
- Port: 5432

Please note that it is reccomended that the values you enter in these fields match your postgres installation credentials, the values given here are placeholders.

2.2) Click on 'Test Connection' in the bottom left of the window and you shall receive a Succeeded pop-up message. If not, please check your credentials.


3) Download a zip file or clone this repository on your local machine inside its own new directory


4) Navigate to the 'Scripts' directory inside your copy of the repository and execute the DataLoaderFdaApi_PY_final.py script. (e.g. python DataLoaderFdaApi_PY_final.py inside cmd or terminal). Please note that one needs to fill in his/hers credentials in line 17 "connection_string = 'postgresql://postgres:sa@localhost:5432/vets_dw' " To match the postgresql setup from step 2.


5) You shall observe the project running with confirmation messages every time the script has successfuly downloaded one of the dataset's files. (e.g. 03.Period finished loading 1987Q1). 

Please note that depending on your system's specifications and internet connection speed, step 5 can take an average of 18 hours to fully execute. It is recommended for faster results to execute the script from either the CMD (for Microsoft Windows) or Terminal (for Linux operating systems) for better efficiency.

Please wait for all files to download and the proceed to step 6


6 schemas_temp.py) Execute script located inside the 'Scripts' directory. Please note that one needs to fill in his/hers credentials in line 3 connection = psycopg2.connect(host='localhost',
                                            database='vets_dw',
                                            user='postgres',
                                            password='password')
To match the postgresql setup from step 2.

 
7 clean_etl.py) Execute script located inside the 'Scripts' directory. Please note that one needs to fill in his/hers credentials in line 11 connection = psycopg2.connect(host='localhost',
                                            database='vets_dw',
                                            user='postgres',
                                            password='password')
To match the postgresql setup from step 2.


Please note that depending on your system's specifications, step 7 can take up to several hours to execute. It is recommended for faster results to execute the script from either the CMD (for Microsoft Windows) or Terminal (for Linux operating systems) for better efficiency.

Please wait for all files to download and the proceed to step 6


8 temp_to_dw.py) Execute script located inside the 'Scripts' directory. Please note that one needs to fill in his/hers credentials in line 9 connection = psycopg2.connect(host='localhost',
                                            database='vets_dw',
                                            user='postgres',
                                            password='password')
To match the postgresql setup from step 2.


In the end you should be able to see all of your data loaded inside the corresponding tables and schemas. 



