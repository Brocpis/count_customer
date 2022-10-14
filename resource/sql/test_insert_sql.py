import pyodbc
import pandas as pd
import platform

driverSQL = ''    
if (platform.platform().lower().find('window') >= 0):
    driverSQL = '{SQL Server}'
if (platform.platform().lower().find('linux') >= 0):
    driverSQL = '{ODBC Driver 18 for SQL Server}'

def insert2SQL (result):
    """ Function for update result after process 
        and update queue status to done

    Parameters
    ----------
    result : dataframe
        result's dataframe
        
    """
        
    server = '10.10.6.101'
    database = 'AI_COUNTING_CIRA'
    username = 'innovation'
    password = 'innovation1234.'
    
    cnxn = pyodbc.connect('DRIVER='+driverSQL+';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password+";TrustServerCertificate=yes" ,autocommit=True)
    crsr = cnxn.cursor()
    
    crsr.fast_executemany = True 

    Tcolumn = '?'
    for x in range(len(result.columns) - 1):
        Tcolumn = Tcolumn + ',?'
    
    sql = "INSERT INTO result_test (cfg_camera_id,direction_id,data_date,data) VALUES (" + Tcolumn + ")"
    
    print(sql)
    
    params = [ tuple(row[1]) for row in result.iterrows()]
    
    print(params)
    
    print ('start insert ' , str(len(params)) ,' rows')
    
    for i in range (len(params)):
        crsr.execute(sql,params[i])

#direction id (1 IN) (2 OUT) (3 GO-HDI) (4 GO-FUR) (5 GO-WIN)

cfg_camera = 111
direction_id = 1
database_datestring = "2022-01-01 16:00:00.000"
data = 25

data = {'cfg_camera_id': [cfg_camera],'direction_id': [direction_id], 
'data_date':[database_datestring], 
'data':[data]}

result=pd.DataFrame(data)
print(result)

insert2SQL(result)
