import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.docente_model import Docente
from fastapi.encoders import jsonable_encoder

class DocenteController:
        
    def create_docente(self, docente: Docente):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO docente (numero_documento,nombres,apellidos,id_usuario,id_facultad) VALUES (%s, %s, %s, %s, %s)", (docente.numero_documento, docente.nombres, docente.apellidos, docente.id_usuario, docente.id_facultad))
            conn.commit()
            conn.close()
            return {"resultado": "Docente creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_docente(self, id_docente: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM docentes WHERE id_docente = %s", (id_docente,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            result = cursor.fetchone()

            if result is None:
                raise HTTPException(status_code=404, detail="Docente no encontrado")

            content = {
                'id_docente': int(result[0]),
                'numero_documento': result[1],
                'nombres': result[2],
                'apellidos': result[3],
                'id_usuario': int(result[4]),
                'id_facultad': int(result[5])
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
       
    def get_docentes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM docentes")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_docente':int(data[0]),
                    'numero_documento':data[1],
                    'nombres':data[2],
                    'apellidos':data[3],
                    'id_usuario':int(data[4]),
                    'id_facultad':int(data[5])
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Docente no encontrado")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
    
    
##docente_controller = DocenteController()