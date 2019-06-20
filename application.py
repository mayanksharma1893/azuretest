"""Cloud Foundry test"""
from flask import Flask,render_template
import os
import pyodbc
import csv

app = Flask(__name__)

port = int(os.getenv("PORT", 5000))

@app.route('/')
def hello_world():
    con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd=Mayank180493#;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    # query="Select mag,latitude from EARTHQUAKE where mag >= 6.2"
    query="select place,mag from EARTHQUAKE where (latitude between 65 and 135) AND (longitude BETWEEN -150 AND -35)"
    columns=['mag','latitude']
    dic=dict()
    cur=con.cursor()
    mem=[]
    cur.execute(query)
    result=list(cur.fetchall())
    for row in result:
        memdict=dict()
        for j,val in enumerate(row):
            memdict[columns[j]]=val
        mem.append(memdict)
    # print(mem)
    a=[1,2,3,4,5]
    # print(a)
    return render_template('chart.html',a=mem,chart="bar")

# @app.route('/streaming.csv')
# def streaming():
#     result=[]
#     with open('streaming.csv') as csv_file:
        
#         csv_reader = csv.reader(csv_file, delimiter=',')
        
#         line_count = 0
#         for row in csv_reader:
#             result.append(row)
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             else:
#                 print(row)
#                 line_count += 1
#             print(f'Processed {line_count} lines.')
        
#     return tuple(result)

# port = os.getenv("PORT", 5000)

if __name__ == '__main__':
    # app.run(debug="true",port=int(port))
    app.run(port=port,debug=True)
