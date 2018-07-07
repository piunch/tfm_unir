import mysql.connector

from mysql.connector import errorcode

def exec(query, args):
    
    try:    # Abrir la conexión
        
        cnx = mysql.connector.connect(
                                    user='tfmunir', 
                                    password='achusico123',
                                    host='172.17.0.2',
                                    database='TFMUNIRBD')                           
    
    except mysql.connector.Error as err: # en caso de error
        
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        
        return None

    cursor = cnx.cursor()
    print("QUERY {")
    print(query)
    print(args)
    print("}")
    cursor.execute(query, args)

    results = []

    for row in cursor:
        results.append(row)

    cursor.close()
    cnx.close()
    return results