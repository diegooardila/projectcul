import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.usuario_model import Usuario
from fastapi.encoders import jsonable_encoder

class UsuarioController:
        
    def create_usuario(self, usuario: Usuario):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (correo_electronico,contrasena_hash,rol,id_estado) VALUES (%s, %s, %s, %s)", (usuario.correo_electronico, usuario.contrasena_hash, usuario.rol, usuario.id_estado))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_usuario(self, id_usuario: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            result = cursor.fetchone()

            if result is None:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

            content = {
                'id_usuario': int(result[0]),
                'correo_electronico': result[1],
                'contrasena_hash': result[2],
                'rol': result[3],
                'id_estado': int(result[4])
            }

            json_data = jsonable_encoder(content)
            return json_data
                
        except psycopg2.Error as err:
            print(err)
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            ##Maneja el estado de la transacción en la base de datos.Si un INSERT, UPDATE o DELETE falla dentro de una transacción, rollback() revierte esos cambios.
            conn.rollback()
        finally:
            conn.close()
       
    def get_usuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_usuario':int(data[0]),
                    'correo_electronico':data[1],
                    'contrasena_hash':data[2],
                    'rol':data[3],
                    'id_estado':int(data[4])
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
    
       

##user_controller = UserController()