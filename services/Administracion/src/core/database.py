import psycopg2
from psycopg2.extras import RealDictCursor

from app.core.config import Parametros
from app.core.logs import HandleLogs
from app.shared.response import internal_response


def conn_db():
    """Creando la coneccion del ejemplo del taller"""
    return psycopg2.connect(
        host=Parametros.db_host,
        port=int(Parametros.db_port),
        user=Parametros.db_user,
        password=Parametros.db_pass,
        database=Parametros.db_name,
        cursor_factory=RealDictCursor
    )


class DataBaseHandle:
    """Handler de las queries"""

    @staticmethod
    def getRecords(query, tamanio, record=()):
        """
        Execute SELECT queries.

        Args:
            query: SQL query string
            tamanio: 0=all, 1=one, >1=n records
            record: tuple of query parameters

        Returns:
            internal_response with result, data, message
        """
        result = False
        message = None
        data = None
        conn = None
        cursor = None
        try:
            conn = conn_db()
            cursor = conn.cursor()
            if len(record) == 0:
                cursor.execute(query)
            else:
                cursor.execute(query, record)

            if tamanio == 0:
                res = cursor.fetchall()
            elif tamanio == 1:
                res = cursor.fetchone()
            else:
                res = cursor.fetchmany(tamanio)

            data = res
            result = True
        except Exception as ex:
            HandleLogs.write_error(ex)
            message = str(ex)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return internal_response(result, data, message)

    @staticmethod
    def ExecuteNonQuery(query, record=()):
        """
        Execute INSERT, UPDATE, DELETE queries.

        Args:
            query: SQL query string
            record: tuple of query parameters

        Returns:
            internal_response with result, data (last id for INSERT), message
        """
        result = False
        message = None
        data = None
        conn = None
        cursor = None
        try:
            conn = conn_db()
            cursor = conn.cursor()
            if len(record) == 0:
                cursor.execute(query)
            else:
                cursor.execute(query, record)

            # Check RETURNING first since INSERT/UPDATE with RETURNING should fetch the returned row
            if 'RETURNING' in query.upper():
                data = cursor.fetchone()
                conn.commit()
            elif 'INSERT' in query.upper():
                cursor.execute('SELECT LASTVAL()')
                ult_id = cursor.fetchone()['lastval']
                conn.commit()
                data = ult_id
            else:
                conn.commit()
                data = cursor.rowcount
            result = True
        except Exception as ex:
            HandleLogs.write_error(ex)
            message = str(ex)
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return internal_response(result, data, message)

