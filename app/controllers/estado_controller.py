import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.estado_model import Estado
from fastapi.encoders import jsonable_encoder

class EstadoController:
        
    def create_estado(self, estado: Estado):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO estado (nombre_estado) VALUES (%s)", (estado.nombre_estado,))
            conn.commit()
            conn.close()
            return {"resultado": "Estado creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_estado(self, id_estado: int):

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estados WHERE id_estado = %s", (id_estado,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            result = cursor.fetchone()

            if result is None:
                raise HTTPException(status_code=404, detail="Estado no encontrado")

            content = {
                'id_estado': int(result[0]),
                'nombre_estado': result[1]
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
       
    def get_estados(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estados")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_estado':int(data[0]),
                    'nombre_estado':data[1]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Estado no encontrado")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
    def update_estado(self, id_estado: int, estado: Estado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE estados SET nombre_estado = %s WHERE id_estado = %s", (estado.nombre_estado, id_estado))
            conn.commit()
            conn.close()
            return {"resultado": "Estado actualizado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el UPDATE, los datos no quedan guardados parcialmente en la base de datos
             # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
       
##estado_controller = EstadoController()