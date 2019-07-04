from Model.connection import mydb


def existe_usuario(usuario): 	
    cursor = mydb.cursor() 	
    consulta = (f'select count(*) from usuario where userName="{usuario}";') 	
    cursor.execute(consulta) 	
    resultado = cursor.fetchone() 	
    cursor.close() 
    return resultado[0]


def logIn(userName, password):
  cursor = mydb.cursor()
  consulta = (
      f'SELECT u.usuario_id, u.username, p.personal_dni, r.rol_id, r.nombre_rol, p.nombre, p.apellido FROM usuario u inner join personal p on u.Usuario_ID = p.Usuario_ID inner join rol r on p.Rol_ID = r.Rol_ID WHERE u.userName = "{userName}" AND u.password = "{password}" AND u.Usuario_ID in (SELECT distinct (Usuario_ID) FROM personal );')
  cursor.execute(consulta)
  resultado = cursor.fetchone()
  cursor.close()
  return resultado
