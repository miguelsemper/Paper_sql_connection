import pyodbc
import pandas as pd
# insert data from csv file into dataframe.
# working directory for csv file: type "pwd" in Azure Data Studio or Linux
# working directory in Windows c:\users\username
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'DESKTOP-4G71TMD\MS_LOCALDB'
database = 'Reference_Papers'
username = 'test'
password = 'password'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()
# Insert Dataframe into SQL Server:
cursor.execute("INSERT INTO Papers (title,main_author_id,pub_year,summary) VALUES ('test title',1,2022,'This is a test summary for the database connection.')")
cnxn.commit()
cursor.close()