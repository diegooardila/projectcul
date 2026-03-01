import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.administrador_model import Administrador
from fastapi.encoders import jsonable_encoder

class AdministradorController:
        
    def create_administrador(self, administrador: Administrador):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO administrador (numero_documento,nombres,apellidos,id_usuario) VALUES (%s, %s, %s, %s)", (administrador.numero_documento, administrador.nombres, administrador.apellidos, administrador.id_usuario))
            conn.commit()
            conn.close()
            return {"resultado": "Administrador creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_administrador(self, id_administrador: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM administrador WHERE id_administrador = %s", (id_administrador,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            result = cursor.fetchone()

            if result is None:
                raise HTTPException(status_code=404, detail="Administrador no encontrado")

            content = {
                'id_administrador': int(result[0]),
                'numero_documento': result[1],
                'nombres': result[2],
                'apellidos': result[3],
                'id_usuario': int(result[4])
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
       
    def get_administradores(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM administrador")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_administrador':int(data[0]),
                    'numero_documento':data[1],
                    'nombres':data[2],
                    'apellidos':data[3],
                    'id_usuario':int(data[4])
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Administrador no encontrado")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
    
       
##administrador_controller = AdministradorController()