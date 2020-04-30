import pyodbc
import numpy as np

server = 'den1.mssql8.gear.host'
db = 'englishteacher'
usr = 'englishteacher'
psword = 'Rt0b2!c9Um_i'

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + server + ';DATABASE=' + db + ';UID=' + usr + ';PWD=' + psword)
cursor = conn.cursor()


def test_flags_return(userId):
    cursor.execute('select * from Test_check where (user_id = ?)', userId)
    temp = cursor.fetchall()
    flags = []
    for i in temp:
        flags.append([i.test_id, i.flag])
    return flags
