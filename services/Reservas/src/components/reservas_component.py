from ..utils.database.connection_db import DataBaseHandle
from ..utils.general.logs import HandleLogs
from ..utils.general.response import internal_response


def listar_reservas():
    try:
        sql = """
            SELECT * FROM reserva;
        """

        result_db = DataBaseHandle.getRecords(sql, 0)

        if not result_db['result']:
            return internal_response(False, None, "Error al obtener reservas")

        return internal_response(True, result_db['data'], "Exitoso")

    except Exception as err:
        HandleLogs.write_error(err)
        return internal_response(False, None, "Error en Reservas -> " + str(err))

def crear_reserva(cliente, restaurante, fini, ffin):
    try:
        sql = """
            INSERT INTO reserva (
                reserva_fi
                reserva_ff
                reserva_fr
                reserva_cid
                reserva_rid
            ) VALUES (%s, %s, %s, %s, %s)
        """

        result_db = DataBaseHandle.ExecuteNonQuery(sql, (
            fini,
            ffin,
            fini,
            cliente,
            restaurante
        ))

        if not result_db['result']:
            return internal_response(False, None, "Error al crear cliente")

        return internal_response(True, result_db['data'], "Exitoso")

    except Exception as err:
        HandleLogs.write_error(err)
        return internal_response(False, None, "Error en Clientes -> " + str(err))

def cancelar_reserva(reserva):
    try:
        sql = """
            DELETE FROM reserva
            WHERE reserva_id = %s
            AND reserva_fi > (CURRENT_DATE + INTERVAL '7 DAYS')
        """

        result_db = DataBaseHandle.ExecuteNonQuery(sql, (reserva,))

        if not result_db['result']:
            return internal_response(False, None,
                "No existe la reserva o ya es tarde para eliminar la reserva")

        return internal_response(True, result_db['data'], "Exitoso")

    except Exception as err:
        HandleLogs.write_error(err)
        return internal_response(False, None, "Error en Reserva -> " + str(err))

def checkin_reserva(reserva):
    try:
        sql = """
            UPDATE reserva
            SET reserva_checkin = TRUE
            WHERE reserva_id = %s
            AND reserva_ff > CURRENT_DATE
        """

        result_db = DataBaseHandle.ExecuteNonQuery(sql, (reserva, ahora))

        if not result_db['result']:
            return internal_response(False, None,
                "No existe la reserva o ya es tarde para eliminar la reserva")

        return internal_response(True, result_db['data'], "Exitoso")

    except Exception as err:
        HandleLogs.write_error(err)
        return internal_response(False, None, "Error en Reserva -> " + str(err))
