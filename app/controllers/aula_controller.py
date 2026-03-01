import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.aula_model import Aula
from fastapi.encoders import jsonable_encoder

class AulaController:
        
    def create_aula(self, aula: Aula):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO aula (codigo_aula,capacidad_maxima,id_estado) VALUES (%s, %s, %s, %s)", (aula.codigo_aula, aula.capacidad_maxima, aula.id_estado))
            conn.commit()
            conn.close()
            return {"resultado": "Aula creada"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_aula(self, id_aula: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM aula WHERE id_aula = %s", (id_aula,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            result = cursor.fetchone()

            if result is None:
                raise HTTPException(status_code=404, detail="Aula no encontrada")

            content = {
                'id_aula': int(result[0]),
                'codigo_aula': result[1],
                'capacidad_maxima': int(result[2]),
                'id_estado': int(result[3])
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
       
    def get_aulas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM aula")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_aula':int(data[0]),
                    'codigo_aula':data[1],
                    'capacidad_maxima':int(data[2]),
                    'id_estado':int(data[3])
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Aula no encontrada")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
    
    
##aula_controller = AulaController()