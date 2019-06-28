from Model.connection import mydb


def existe_usuario(usuario): 	
    cursor = mydb.cursor() 	
    consulta = (f'select count(*) from usuario where userName="{usuario}";') 	
    cursor.execute(consulta) 	
    resultado = cursor.fetchone() 	
    cursor.close() 
    return resultado[0]
