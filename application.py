"""Cloud Foundry test"""
from flask import Flask,render_template
import os
import pyodbc
import csv

app = Flask(__name__)

port = int(os.getenv("PORT", 5000))

@app.route('/')
def hello_world():
    # con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd={Mayank180493#};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    # a=10
    # start=0
    # end=100
    # age_interval=[0]
    # val=start
    # while val<end:
    #     val+=10
    #     age_interval.append(val)
    # # columns=['age_group','count']  
    # # print(age_interval)
    # mem=[]
    # # memdict=dict()
    # # for i in range(0,len(age_interval)-1):
    # #     query="select StateName,(Voted/TotalPop*100) AS Perc from voting"
    # #     cur=con.cursor()
    # #     cur.execute(query)
    # #     result=list(cur.fetchall())
        
    # #     age_group=str(age_interval[i])+"-"+str(age_interval[i+1])
    # #     for row in result: 
    # #         memdict=dict()
    # #         for j,val in enumerate(row):
    # #             memdict["StateName"]=StateName  
    # #             memdict["Perc"]=Perc
    # #             mem.append(memdict)
    # #         print(mem)

    # #     # print(mem)
    # # return render_template('chart.html',a=mem,chart="pie")


    
    # query="select StateName,(Voted/TotalPop*100) AS Perc from voting"
    # columns=['StateName','Perc']
    # dic=dict()
    # cur=con.cursor()
    # mem=[]
    # cur.execute(query)
    # result=list(cur.fetchall())
    # for row in result:
    #     memdict=dict()
    #     for j,val in enumerate(row):
    #         memdict[columns[j]]=val
    #     mem.append(memdict)
    # # print(mem)
    # a=[1,2,3,4,5]
    # # print(a)
    # return render_template('chart.html',a=mem,chart="pie")


   nvalue = int(request.form['nvalue'])
   con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd={Mayank180493#};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
   # a=nvalue #chnage this variable
   start=nvalue
   end=80
   age_interval=[0]
   val=start
   while val<end:
       val+=nvalue
       age_interval.append(val)
   mem=[]
   for i in range(0,len(age_interval)-1):
       #query="select (count(*)) as count from voting where age > "+str(age_interval[i])+" and age<"+str(age_interval[i+1])
       query="select count(*) as count from voting where ((voted/Totalpop)*100) >"+str(age_interval[i])+" and ((voted/Totalpop)*100)< "+str(age_interval[i+1])
       cur=con.cursor()
       cur.execute(query)
       result=list(cur.fetchall())
       vtt=str(age_interval[i])+"-"+str(age_interval[i+1])
       for row in result:
           memdict=dict()
           for j,val in enumerate(row):
               memdict["vtt"]=vtt
               memdict["States"]=val
               mem.append(memdict)
           print(mem)

   return render_template('chart.html',a=mem,chart="pie")



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



if __name__ == '__main__':
    app.run(port=port,debug=True)




# """Cloud Foundry test"""
# from flask import Flask,render_template
# import os
# import pyodbc
# import csv

# app = Flask(__name__)

# port = int(os.getenv("PORT", 5000))

# @app.route('/')
# def index():

#     return render_template('index.html')



# @app.route('/Search5', methods=['GET', 'POST'])
# def Search5():

#     cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd={Mayank180493#};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#     cursor = cnxn.cursor()
#     cursor.execute("Select StateName,TotalPop from voting where TotalPop between '5000' and '10000'")
#     row = cursor.fetchall()
#     return render_template("view.html", row=row)



# @app.route('/Search10', methods=['GET', 'POST'])
# def Search10():
    
#     cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd={Mayank180493#};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#     cursor = cnxn.cursor()
#     cursor.execute("Select StateName,TotalPop from voting where TotalPop between '10000' and '50000'")
#     row = cursor.fetchall()
#     return render_template("view.html", row=row)


# @app.route('/chart',methods=['GET', 'POST'])
# def chart():
#         mag = request.form['mag1']
#         con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd={Mayank180493#};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#         query="Select mag,latitude from quake3 where mag >= 7"
#         columns=['mag','latitude']
#         dic=dict()
#         cur=con.cursor()
#         mem=[]
#         cur.execute(query)
#         result=list(cur.fetchall())
#         for row in result:
#             memdict=dict()
#             for j,val in enumerate(row):
#                 memdict[columns[j]]=val
#             mem.append(memdict)
#         # print(mem)
#         a=[1,2,3,4,5]
#         # print(a)
#         return render_template('chart.html',a=mem,chart="bar")

# # @app.route('/streaming.csv')
# # def streaming():
# #     result=[]
# #     with open('streaming.csv') as csv_file:
        
# #         csv_reader = csv.reader(csv_file, delimiter=',')
        
# #         line_count = 0
# #         for row in csv_reader:
# #             result.append(row)
# #             if line_count == 0:
# #                 print(f'Column names are {", ".join(row)}')
# #                 line_count += 1
# #             else:
# #                 print(row)
# #                 line_count += 1
# #             print(f'Processed {line_count} lines.')
        
# #     return tuple(result)


# port = os.getenv("PORT", 5000)

# if __name__ == '__main__':
#    app.run(debug="true",port=int(port))






# """Cloud Foundry test"""
# from flask import Flask,render_template
# import os
# import pyodbc
# import csv

# app = Flask(__name__)

# port = int(os.getenv("PORT", 5000))



# @app.route('/Search5', methods=['GET', 'POST'])
# def Search5():

#     cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:azurevijaydb.database.windows.net,1433;Database=Quakes;Uid=vijaykant009@azurevijaydb;Pwd={J@ik@nt009};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#     cursor = cnxn.cursor()
#     cursor.execute("Select StateName,TotalPop from voting where TotalPop between '5000' and '10000'")
#     row = cursor.fetchall()
#     return render_template("view.html", row=row)



# @app.route('/Search10', methods=['GET', 'POST'])
# def Search10():
    
#     cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:azurevijaydb.database.windows.net,1433;Database=Quakes;Uid=vijaykant009@azurevijaydb;Pwd={J@ik@nt009};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#     cursor = cnxn.cursor()
#     cursor.execute("Select StateName,TotalPop from voting where TotalPop between '10000' and '50000'")
#     row = cursor.fetchall()
#     return render_template("view.html", row=row)






# # @app.route('/')
# # def hello_world():
#     # con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd=Mayank180493#;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#     # # query="Select mag,latitude from EARTHQUAKE where mag >= 6.2"
#     # query="select StateName from voting where Totalpop between 5000000 AND 10000000"
#     # # columns=['mag','latitude']
#     # columns=['place','mag']
#     # dic=dict()
#     # cur=con.cursor()
#     # mem=[]
#     # cur.execute(query)
#     # result=list(cur.fetchall())
#     # for row in result:
#     #     memdict=dict()
#     #     for j,val in enumerate(row):
#     #         memdict[columns[j]]=val
#     #     mem.append(memdict)
#     # # print(mem)
#     # a=[1,2,3,4,5]
#     # # print(a)
#     # return render_template('chart.html',a=mem,chart="bar")

# # @app.route('/')
# # def hello_world():
# #     conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd=Mayank180493#;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
# #     lstDictionaryData = []
# #     cursor = conn.cursor()
# #     startingtime = time.time()
# #     query="select StateName from voting where Totalpop between 5000000 AND 10000000"
# #     # print(query)
# #     cursor.execute(query)
# #     # print(tmp)
# #     endingtime = time.time()
# #     row = cursor.fetchone()
# #     while row:
# #         lstDictionaryData.append(row)
# #         # print("hi!" + str(row))
# #         row = cursor.fetchone()
# #     # return "hello!!"
# #     conn.close()
# #     Exectime = (endingtime - startingtime) * 1000
# #     return render_template('index.html', tableData=lstDictionaryData, tableDataLen=lstDictionaryData.__len__(), Exectime=Exectime)


# # # @app.route('/streaming.csv')
# # # def streaming():
# # #     result=[]
# # #     with open('streaming.csv') as csv_file:
        
# # #         csv_reader = csv.reader(csv_file, delimiter=',')
        
# # #         line_count = 0
# # #         for row in csv_reader:
# # #             result.append(row)
# # #             if line_count == 0:
# # #                 print(f'Column names are {", ".join(row)}')
# # #                 line_count += 1
# # #             else:
# # #                 print(row)
# # #                 line_count += 1
# # #             print(f'Processed {line_count} lines.')
        
# # #     return tuple(result)

# # # port = os.getenv("PORT", 5000)

# if __name__ == '__main__':
#     # app.run(debug="true",port=int(port))
#     app.run(port=port,debug=True)
