import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.inscripcion_model import Inscripcion
from fastapi.encoders import jsonable_encoder

class InscripcionController:
        
    def create_inscripcion(self, inscripcion: Inscripcion):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO inscripcion (id_estudiante,id_curso,fecha_registro,id_estado) VALUES (%s, %s, %s, %s)", (inscripcion.id_estudiante, inscripcion.id_curso, inscripcion.fecha_registro, inscripcion.id_estado))
            conn.commit()
            conn.close()
            return {"resultado": "Inscripción creada"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_inscripcion(self, id_inscripcion: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inscripcion WHERE id_inscripcion = %s", (id_inscripcion,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            result = cursor.fetchone()

            if result is None:
                raise HTTPException(status_code=404, detail="Inscripción no encontrada")

            content = {
                'id_inscripcion': int(result[0]),
                'id_estudiante': int(result[1]),
                'id_curso': int(result[2]),
                'fecha_registro': result[3],
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
       
    def get_inscripciones(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inscripcion")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_inscripcion':int(data[0]),
                    'id_estudiante':int(data[1]),
                    'id_curso':int(data[2]),
                    'fecha_registro':data[3],
                    'id_estado':int(data[4])
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Inscripción no encontrada")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_inscripcion(self, id_inscripcion: int, inscripcion: Inscripcion):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE inscripcion
                SET id_estudiante = %s,
                    id_curso = %s,
                    fecha_registro = %s,
                    id_estado = %s
                WHERE id_inscripcion = %s
            """, (
                inscripcion.id_estudiante,
                inscripcion.id_curso,
                inscripcion.fecha_registro,
                inscripcion.id_estado,
                id_inscripcion
            ))
            conn.commit()
            return {"resultado": "Inscripción actualizada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_inscripcion(self, id_inscripcion: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM inscripcion WHERE id_inscripcion = %s", (id_inscripcion,))
            conn.commit()
            return {"resultado": "Inscripción eliminada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    
##inscripcion_controller = InscripcionController()