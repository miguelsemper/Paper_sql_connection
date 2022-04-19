import PySimpleGUI as sg
import pyodbc

server = 'DESKTOP-4G71TMD\MS_LOCALDB'
database = 'Reference_Papers'
username = 'test'
password = 'password'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        cursor.execute("INSERT INTO Papers (title,main_author_id,pub_year,publication,summary) VALUES ('test title',1,2022,'test publication','This is a test summary for the database connection.')")
        cnxn.commit()
        cursor.close()
        break

window.close()