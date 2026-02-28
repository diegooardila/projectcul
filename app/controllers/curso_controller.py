import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.curso_model import Curso
from fastapi.encoders import jsonable_encoder

class CursoController:
        
    def create_curso(self, curso: Curso):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO curso (codigo_curso,nombre_curso,cupo_maximo,fecha_hora,id_docente,id_aula,id_periodo,id_estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (curso.codigo_curso, curso.nombre_curso, curso.cupo_maximo, curso.fecha_hora, curso.id_docente, curso.id_aula, curso.id_periodo, curso.id_estado))
            conn.commit()
            conn.close()
            return {"resultado": "Curso creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_curso(self, id_curso: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM curso WHERE id_curso = %s", (id_curso,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            result = cursor.fetchone()

            if result is None:
                raise HTTPException(status_code=404, detail="Curso no encontrado")

            content = {
                'id_curso': int(result[0]),
                'codigo_curso': result[1],
                'nombre_curso': result[2],
                'cupo_maximo': int(result[3]),
                'fecha_hora': result[4],
                'id_docente': int(result[5]),
                'id_aula': int(result[6]),
                'id_periodo': int(result[7]),
                'id_estado': int(result[8])
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
       
    def get_cursos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM curso")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_curso':int(data[0]),
                    'codigo_curso':data[1],
                    'nombre_curso':data[2],
                    'cupo_maximo':int(data[3]),
                    'fecha_hora':data[4],
                    'id_docente':int(data[5]),
                    'id_aula':int(data[6]),
                    'id_periodo':int(data[7]),
                    'id_estado':int(data[8])
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Curso no encontrado")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_curso(self, id_curso: int, curso: Curso):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE curso
                SET codigo_curso = %s,
                    nombre_curso = %s,
                    cupo_maximo = %s,
                    fecha_hora = %s,
                    id_docente = %s,
                    id_aula = %s,
                    id_periodo = %s,
                    id_estado = %s
                WHERE id_curso = %s
            """, (
                curso.codigo_curso,
                curso.nombre_curso,
                curso.cupo_maximo,
                curso.fecha_hora,
                curso.id_docente,
                curso.id_aula,
                curso.id_periodo,
                curso.id_estado,
                id_curso
            ))
            conn.commit()
            return {"resultado": "Curso actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_curso(self, id_curso: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM curso WHERE id_curso = %s", (id_curso,))
            conn.commit()
            return {"resultado": "Curso eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    
##cursocontroller = CursoController()
