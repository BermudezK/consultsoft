from Model.connection import mydb
from mysql.connector import Error

def select_secretarias():
    try:
        if mydb.is_connected():
            cursor = mydb.cursor()
            consulta = 'SELECT personal_DNI,nombre, apellido, telefono FROM personal WHERE rol_id = 2;'
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(mydb.is_connected()):
            cursor.close()

def insert_personal(dni, usuario, rol, nombre, apellido, telefono):
    cursor = mydb.cursor()
    consulta = "INSERT into personal(Personal_DNI, Usuario_ID, Rol_ID, Nombre, Apellido, Telefono)values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(consulta,(dni, usuario, rol, nombre, apellido, telefono))
    mydb.commit()
    cursor.close()

def insertar_usuario(user_name, password):
    cursor = mydb.cursor() 	
    consulta = "insert into usuario(userName, password) value(%s,%s);" 	
    cursor.execute(consulta, (user_name, password)) 	
    mydb.commit() 	
    resultado_usuarioID = select_IDuser(user_name) 	
    cursor.close() 
    return resultado_usuarioID

def select_IDuser(user_name): 	
    cursor = mydb.cursor() 	
    consulta = (f'select usuario_ID from usuario where userName = "{user_name}";') 	
    cursor.execute(consulta) 	
    resultado = cursor.fetchall() 	
    cursor.close() 	
    return resultado[0][0]

def select_pacientes():
    try:
        if mydb.is_connected():
            cursor = mydb.cursor()
            consulta = 'SELECT personal_DNI,nombre, apellido, telefono FROM personal WHERE rol_id = 3;'
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(mydb.is_connected()):
            cursor.close()


def select_secretario(usuario_ID):
    cursor = mydb.cursor()
    consulta = (f'select P.personal_DNI, P.nombre,P.apellido, P.telefono,U.usuario_ID, U.userName, U.password from personal P inner join usuario U on P.usuario_ID = U.usuario_ID where P.personal_DNI = {usuario_ID};')  
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    mydb.commit()
    cursor.close()    
    return resultado[0]

def modificar_personal(dni, nuevosDatos):
    cursor = mydb.cursor()
    updatePersonal = f"""
        UPDATE personal
            SET Personal_DNI = {nuevosDatos['dni']},
                Nombre = "{nuevosDatos['nombre']}",
                Apellido = "{nuevosDatos['apellido']}",
                Telefono = {nuevosDatos['telefono']}
            WHERE Personal_DNI = {dni};
    """
    
    cursor.execute(updatePersonal)
    mydb.commit()
    cursor.close()

def modificar_usuario(username, nuevosDatos):
    cursor = mydb.cursor()
    updateUsuario = f"""
        UPDATE usuario
            SET userName = "{nuevosDatos['username']}", 
                password = "{nuevosDatos['password']}"
            WHERE userName = "{username}";
    """

    cursor.execute(updateUsuario)
    mydb.commit()
    cursor.close()


# def insert_personal(dni, usuario, rol, nombre, apellido, telefono):
#     cursor = mydb.cursor()
#     consulta = "INSERT into personal(Personal_DNI, Usuario_ID, Rol_ID, Nombre, Apellido, Telefono)values(%s,%s,%s,%s,%s,%s)"
#     cursor.execute(consulta,(dni, usuario, rol, nombre, apellido, telefono))
#     mydb.commit()
#     cursor.close()

# def insertar_usuario(user_name, password):
#     cursor = mydb.cursor() 	
#     consulta = "insert into usuario(userName, password) value(%s,%s);" 	
#     cursor.execute(consulta, (user_name, password)) 	
#     mydb.commit() 	
#     resultado_usuarioID = select_IDuser(user_name) 	
#     cursor.close() 
#     return resultado_usuarioID
