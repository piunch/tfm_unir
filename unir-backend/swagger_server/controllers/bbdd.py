import mysql.connector
import configparser

from mysql.connector import errorcode

def select(query, args):
    
    try:    # Abrir la conexión
        
        config = configparser.ConfigParser()
        config_files=config.read('config.ini')

        if config is None or not config.has_section('BBDD'):
            print("No se encuentra el config.ini en " + str(config_files) +" con los parametros de conexión para la BD")
            return None

        bd_user = config['BBDD']['USER']
        bd_password = config['BBDD']['PASSWORD']
        bd_host = config['BBDD']['HOST']
        bd_name = config['BBDD']['DATABASE']
        
        cnx = mysql.connector.connect(
                                user=bd_user, 
                                password=bd_password, 
                                host=bd_host, 
                                database=bd_name)                           
    
    except mysql.connector.Error as err: # en caso de error
        
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error en las credenciales de la BD")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("No se encuentra la BD")
        else:
            print(err)
        
        return None

    cursor = cnx.cursor()
    """
    print("SELECT {")
    print("\t" + str(query))
    print("\t" + str(args))
    print("}")
    """
    cursor.execute(query, args)

    results = []

    for row in cursor:
        results.append(row)

    cursor.close()
    cnx.close()
    return results

def exec(query, args):
    
    try:    # Abrir la conexión
        
        config = configparser.ConfigParser()
        config_files=config.read('config.ini')

        if config is None or not config.has_section('BBDD'):
            print("No se encuentra el config.ini en " + str(config_files) +" con los parametros de conexión para la BD")
            return None

        bd_user = config['BBDD']['USER']
        bd_password = config['BBDD']['PASSWORD']
        bd_host = config['BBDD']['HOST']
        bd_name = config['BBDD']['DATABASE']
        
        cnx = mysql.connector.connect(
                                user=bd_user, 
                                password=bd_password, 
                                host=bd_host, 
                                database=bd_name)                     
    
    except mysql.connector.Error as err: # en caso de error
        
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error en las credenciales de la BD")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("No se encuentra la BD")
        else:
            print(err)
        
        return None

    cursor = cnx.cursor()
    """
    print("EXEC {")
    print("\t" + str(query))
    print("\t" + str(args))
    print("}")
    """
    cursor.execute(query, args)

    cnx.commit()
    cursor.close()
    cnx.close()

    return None