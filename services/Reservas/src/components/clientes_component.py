from ..utils.database.connection_db import DataBaseHandle
from ..utils.general.logs import HandleLogs
from ..utils.general.response import internal_response


def listar_clientes():
    try:
        sql = """
            SELECT
                cliente_id,
                cliente_nombre,
                cliente_contacto
            FROM cliente;
        """

        result_db = DataBaseHandle.getRecords(sql, 0)

        if not result_db['result']:
            return internal_response(False, None, "Error al obtener clientes")

        return internal_response(True, result_db['data'], "Exitoso")

    except Exception as err:
        HandleLogs.write_error(err)
        return internal_response(False, None, "Error en Clientes -> " + str(err))

def crear_cliente(nombre, contacto):
    try:
        sql = """
            INSERT INTO cliente (cliente_nombre, cliente_contacto) VALUES (%s, %s)
        """

        result_db = DataBaseHandle.ExecuteNonQuery(sql, (nombre, contacto))

        if not result_db['result']:
            return internal_response(False, None, "Error al crear cliente")

        return internal_response(True, result_db['data'], "Exitoso")

    except Exception as err:
        HandleLogs.write_error(err)
        return internal_response(False, None, "Error en Clientes -> " + str(err))
