import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.periodo_academico_model import PeriodoAcademico
from fastapi.encoders import jsonable_encoder

class PeriodoAcademicoController:
        
    def create_periodo_academico(self, periodo_academico: PeriodoAcademico):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO periodo_academico (codigo_periodo,fecha_inicio,fecha_fin) VALUES (%s, %s, %s)", (periodo_academico.codigo_periodo, periodo_academico.fecha_inicio, periodo_academico.fecha_fin))
            conn.commit()
            conn.close()
            return {"resultado": "Periodo académico creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_periodo_academico(self, id_periodo: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM periodo_academico WHERE id_periodo = %s", (id_periodo,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            result = cursor.fetchone()

            if result is None:
                raise HTTPException(status_code=404, detail="Periodo académico no encontrado")

            content = {
                'id_periodo': int(result[0]),
                'codigo_periodo': result[1],
                'fecha_inicio': result[2],
                'fecha_fin': result[3]
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
       
    def get_periodos_academicos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM periodo_academico")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_periodo':int(data[0]),
                    'codigo_periodo':data[1],
                    'fecha_inicio':data[2],
                    'fecha_fin':data[3]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Periodo académico no encontrado")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
    
       

##periodo_academico_controller = PeriodoAcademicoController()