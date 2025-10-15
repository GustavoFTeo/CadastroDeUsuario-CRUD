import pymysql as mySQLdb

def conectar():
    return mySQLdb.connect(
        host='localhost',
        user='root',
        passwd='admin',
        database='cadastro'
    )