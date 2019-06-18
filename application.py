from flask import Flask,render_template,request
import os
import pyodbc
import random
import redis
import time
import hashlib
from json import loads, dumps

app = Flask(__name__)



myHostname = "mayankazureredis.redis.cache.windows.net"
myPassword = "fmfPJNauvusKKndVvRJoYrskAsdN+sxYgN9WGeu9Px0="

r = redis.StrictRedis(host=myHostname, port=6380, password=myPassword, ssl=True)

# result = r.ping()
# print("Ping returned : " + str(result))

# result = r.set("Message", "Hello!, The cache is working with Python!")
# print("SET Message returned : " + str(result))

# result = r.get("Message")
# print("GET Message returned : " + result.decode("utf-8"))

# result = r.client_list()
# print("CLIENT LIST returned : ")
# for c in result:
#     print("id : " + c['id'] + ", addr : " + c['addr'])

@app.route('/')
def hello_world():
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd=Mayank180493#;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    lstDictionaryData = []
    cursor = conn.cursor()
    startingtime = time.time()
    query = "SELECT TOP 15 latitude, longitude, mag, place FROM EARTHQUAKE"
    # print(query)
    cursor.execute(query)
    # print(tmp)
    endingtime = time.time()
    row = cursor.fetchone()
    while row:
        lstDictionaryData.append(row)
        # print("hi!" + str(row))
        row = cursor.fetchone()
    # return "hello!!"
    conn.close()
    Exectime = (endingtime - startingtime) * 1000
    return render_template('index.html', tableData=lstDictionaryData, tableDataLen=lstDictionaryData.__len__(), Exectime=Exectime)

@app.route('/showdb', methods=['GET', 'POST'])
def showdb():
    limit = request.form['limit']
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd=Mayank180493#;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    cursor = cnxn.cursor()
    cursor.execute("SELECT TOP "+limit+" * from EARTHQUAKE ")
    row = cursor.fetchall()
    return render_template("showdb.html", row=row)


@app.route('/createtable',methods=['GET', 'POST'])
def createTable():
    # lstDictionaryData = []
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd=Mayank180493#;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    cursor = conn.cursor()
    # query = "CREATE TABLE dbo.all_month (\"time\" datetime, \"latitude\" FLOAT, \"longitude\" FLOAT, \"depth\" FLOAT, \"mag\" FLOAT, \"magType\" TEXT, \"nst\" INT, \"gap\" INT, \"dmin\" FLOAT, \"rms\" FLOAT, \"net\" TEXT, \"id\" TEXT, \"updated\" datetime, \"place\" TEXT, \"type\" TEXT, \"horontalError\" FLOAT, \"depthError\" FLOAT, \"magError\" FLOAT, \"magNst\" INT, \"status\" TEXT, \"locationSource\" TEXT, \"magSource\" TEXT)"
    query = 'CREATE TABLE azuredbtest.dbo.EARTHQUAKE1("time" DATETIME,latitude FLOAT,longitude FLOAT,depth FLOAT,mag FLOAT,magType TEXT,nst INT,gap INT,dmin FLOAT,rms FLOAT,net TEXT,id TEXT,updated DATETIME,place TEXT,type TEXT,horontalError FLOAT,depthError FLOAT,magError FLOAT,magNst INT,status TEXT,locationSource TEXT,magSource TEXT)'
    # print(query)
    startingtime = time.time()
    # cursor.execute(query)
    cursor.execute(query)
    cursor.execute("CREATE INDEX EARTHQUAKE_mag__index ON azuredbtest.dbo.EARTHQUAKE1 (mag)")
    cursor.execute("CREATE INDEX EARTHQUAKE_lat__index ON azuredbtest.dbo.EARTHQUAKE1 (latitude)")
    cursor.execute("CREATE INDEX EARTHQUAKE_long__index ON sazuredbtest.dbo.EARTHQUAKE1 (longitude)")
    conn.commit()
    endingtime = time.time()
    conn.close()
    Exectime = (endingtime - startingtime) * 1000
    return render_template('createtable.html', Exectime=Exectime)

@app.route('/location', methods=['GET', 'POST'])
def location():
    lat1 = request.form['lat1']
    lon1 = request.form['lon1']
    # lat2 = request.form['lat2']
    # lon2 = request.form['lon2']
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd=Mayank180493#;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    cursor = cnxn.cursor()
    cursor.execute("Select * from EARTHQUAKE where latitude between '"+lat1+"' and '"+lat2+"' ")
    result = cursor.fetchall()
    print(result)
    return render_template("location.html", row=result)


@app.route('/randomqueries', methods=['GET', 'POST'])
def randomQueries():
    firstlat = int(request.form['lat1'])
    secondlat = int(request.form['lat2'])
    queryCount = int(request.form['count'])
    useCache = int(request.form['Cache'])
    # queryCount = request.form["quer"]
    # print(type(queryCount))
    # useCache = int(request.form['cache'])
    # firstlat = float(request.form['firstlat'])
    # secondlat = float(request.form['secondlat'])

    list_dict_Data = []
    list_dict_DataDisplay = []

    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:mayankazuredb.database.windows.net,1433;Database=azuredbtest;Uid=mayanksharma1893@mayankazuredb;Pwd=Mayank180493#;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    cursor = conn.cursor()
    totalExecutionTime = 0
    columns = ['time', 'latitude', 'longitude', 'place', 'mag']

    # without cache
    if useCache == 0:
        # print("hi!")

        latitude_value = round(random.uniform(firstlat, secondlat), 2)
        print(latitude_value)
        startingtime = time.time()
        query = "SELECT 'time', latitude, longitude, place, mag FROM EARTHQUAKE WHERE latitude = '" + str(latitude_value) + "'"
        cursor.execute(query)
        endingtime = time.time()
        # print(query)
        list_dict_DataDisplay = cursor.fetchall()
        # print(list_dict_DataDisplay)
        Exectime = (endingtime - startingtime) * 1000
        firstExecutionTime = Exectime

        for i in range(queryCount-1):
            totalExecutionTime = totalExecutionTime + Exectime
            latitude_value = round(random.uniform(firstlat, secondlat), 2)
            startingtime = time.time()
            query = "SELECT 'time', latitude , longitude, place, mag FROM EARTHQUAKE WHERE latitude = '" + str(latitude_value) + "'"
            cursor.execute(query)
            endingtime = time.time()
            list_dict_Data = list(cursor.fetchall())
            # print("inside if")
            # print(lstDictionaryData)

            memData = []
            for row in list_dict_Data:
                memDataDict = dict()
                for i, val in enumerate(row):
                    # if type(val) == datetime:
                    #     val = time.mktime(val.timetuple())
                    memDataDict[columns[i]] = val
                memData.append(memDataDict)
            r.set(query, dumps(memData))

            Exectime = (endingtime - startingtime) * 1000
            # totalExecutionTime = totalExecutionTime + Exectime
        # print(totalExecutionTime)
    # with cache
    else:
        print('Cache inside')
        for x in range(queryCount):
            print('x')
            print(x)
            latitude_value = round(random.uniform(firstlat, secondlat), 2)
            query = "SELECT 'time', latitude , longitude, place, mag FROM EARTHQUAKE WHERE latitude = '" + str(latitude_value) + "'"
            # print("inside else")
            memhash = hashlib.sha256(query.encode()).hexdigest()
            startingtime = time.time()
            list_dict_Data = r.get(memhash)

            # print(list_dict_Data[0])
            # print(i)
            if not list_dict_Data:
                # print("from db")
                print('Not in cache')

                cursor.execute(query)
                list_dict_Data = cursor.fetchall()
                # print('list_dict_Data')
                # print(list_dict_Data)
                if x == 0:
                    # print("from db")
                    print('Hi first block')
                    list_dict_DataDisplay = list_dict_Data
                endingtime = time.time()
                memData = []
                for row in list_dict_Data:
                    # print('row')
                    # print(row)
                    memDataDict = dict()
                    for i, val in enumerate(row):
                        # print('i')
                        # print(i)
                        # if type(val) == datetime:
                        #     val = time.mktime(val.timetuple())
                        memDataDict[columns[i]] = val
                    memData.append(memDataDict)
                r.set(memhash, dumps(memData))
                print('Hi')
                Exectime = (endingtime - startingtime) * 1000
                if x == 0:
                    print('Hi again')
                    firstExecutionTime = Exectime
                else:
                    print('Not 0 iteration')    
                totalExecutionTime = totalExecutionTime + Exectime
                

            else:
                print('In cache')
                list_dict_Data = loads(list_dict_Data.decode())
                if x == 0:
                    list_dict_DataDisplay = list_dict_Data
                endingtime = time.time()
            Exectime = (endingtime - startingtime) * 1000
            if x == 0:
                    firstExecutionTime = Exectime
            totalExecutionTime = totalExecutionTime + Exectime
    conn.close()
    # print(list_dict_Data)
    return render_template('index.html', tableData=list_dict_DataDisplay, tableDataLen=list_dict_DataDisplay.__len__(), Exectime=totalExecutionTime, firstExecutionTime=firstExecutionTime)

# @app.route('/magsearch',methods=['GET', 'POST'])

# def magsearch():
#         limit = request.form['limit']
#         mag1 = request.form['magnitude1']
#         mag2 = request.form['magnitude2']
#         # mag = random.randrange(mag1,mag2,1)
#         cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:sagarserver3122.database.windows.net,1433;Database=sagar3122sql;Uid=sagar3122@sagarserver3122;Pwd=steve@3122HOLMES;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#         cursor = cnxn.cursor()
#         for x in random.randrange(mag1,mag2,1)
#         cursor.execute("Select TOP "+limit+" * from all_month WHERE mag= '"+mag+"'")
#         result = cursor.fetchall()
#             print(result)
#         return render_template("magsearch.html", row=result)






port = os.getenv("PORT", 5000)

if __name__ == '__main__':
   app.run(debug="true",port=int(port))
    #  app.run("0.0.0.0",port=port)
