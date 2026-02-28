import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.estudiante_model import Estudiante
from fastapi.encoders import jsonable_encoder

class EstudianteController:
        
    def create_estudiante(self, estudiante: Estudiante):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO estudiantes (codigo_estudiantil,nombres,apellidos,id_usuario,id_facultad) VALUES (%s, %s, %s, %s, %s)", (estudiante.codigo_estudiantil, estudiante.nombres, estudiante.apellidos, estudiante.id_usuario, estudiante.id_facultad))
            conn.commit()
            conn.close()
            return {"resultado": "Estudiante creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_estudiante(self, id_estudiante: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estudiantes WHERE id_estudiante = %s", (id_estudiante,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            result = cursor.fetchone()

            if result is None:
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")

            content = {
                'id_estudiante': int(result[0]),
                'codigo_estudiantil': result[1],
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
       
    def get_estudiantes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estudiantes")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_estudiante':int(data[0]),
                    'codigo_estudiantil':data[1],
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
                raise HTTPException(status_code=404, detail="Estudiante no encontrado")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_estudiante(self, id_estudiante: int, estudiante: Estudiante):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE estudiantes
                SET id_estudiante = %s,
                    codigo_estudiantil = %s,
                    nombres = %s,
                    apellidos = %s,
                    id_usuario = %s,
                    id_facultad = %s
                WHERE id_estudiante = %s
            """, (
                estudiante.id_estudiante,
                estudiante.codigo_estudiantil,
                estudiante.nombres,
                estudiante.apellidos,
                estudiante.id_usuario,
                estudiante.id_facultad,
                id_estudiante
            ))
            conn.commit()
            return {"resultado": "Estudiante actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_estudiante(self, id_estudiante: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM estudiantes WHERE id_estudiante = %s", (id_estudiante,))
            conn.commit()
            return {"resultado": "Estudiante eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
##estudiante_controller = EstudianteController()