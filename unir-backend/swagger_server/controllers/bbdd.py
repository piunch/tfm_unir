import mysql.connector

from mysql.connector import errorcode

def select(query, args):
    try:
        cnx = mysql.connector.connect(
                                    user='tfmunir', 
                                    password='achusico123',
                                    host='172.17.0.2',
                                    database='TFMUNIRBD')                           
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    cursor = cnx.cursor()

    cursor.execute(query, args)

    for row in cursor:
        print(row)

    cursor.close()
    cnx.close()

    return ""