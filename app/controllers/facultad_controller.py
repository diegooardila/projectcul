import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.facultad_model import Facultad
from fastapi.encoders import jsonable_encoder

class FacultadController:
        
    def create_facultad(self, facultad: Facultad):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO facultades (nombre_facultad) VALUES (%s)", (facultad.nombre_facultad,))
            conn.commit()
            conn.close()
            return {"resultado": "Facultad creada"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_facultad(self, id_facultad: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM facultades WHERE id_facultad = %s", (id_facultad,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            result = cursor.fetchone()

            if result is None:
                raise HTTPException(status_code=404, detail="Facultad no encontrada")

            content = {
                'id_facultad': int(result[0]),
                'nombre_facultad': result[1]
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
       
    def get_facultades(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM facultades")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_facultad':int(data[0]),
                    'nombre_facultad':data[1]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Facultad no encontrada")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
    
       

##facultad_controller = FacultadController()