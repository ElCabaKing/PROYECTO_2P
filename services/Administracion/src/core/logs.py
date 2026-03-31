import datetime
import inspect
import os


class HandleLogs:
    """Handler for logging information and errors to files."""

    @staticmethod
    def write_log(*mensaje):
        """Write informational log entry."""
        try:
            fun = inspect.currentframe().f_back.f_code.co_name
            now = datetime.datetime.now()
            path = os.path.abspath(os.path.dirname(__file__))
            name_file = os.path.join(path, "LOGS")
            if not os.path.exists(name_file):
                os.makedirs(name_file)
            name_file = os.path.join(name_file, "LOG_" + now.strftime('%d_%m_%Y') + ".log")
            res = now.strftime("%H:%M:%S") + " - INF - " + fun + " - " + str(mensaje)
            with open(name_file, "a") as f:
                f.write(res + "\n")
            print(res)
        except Exception as e:
            print("Error al crear log: " + str(e))

    @staticmethod
    def write_error(*err):
        """Write error log entry."""
        try:
            fun = inspect.currentframe().f_back.f_code.co_name
            now = datetime.datetime.now()
            path = os.path.abspath(os.path.dirname(__file__))
            name_file = os.path.join(path, "LOGS")
            if not os.path.exists(name_file):
                os.makedirs(name_file)
            name_file = os.path.join(name_file, "ERR_" + now.strftime('%d_%m_%Y') + ".log")
            res = now.strftime("%H:%M:%S") + " - ERR - " + fun + " - " + str(err)
            with open(name_file, "a") as f:
                f.write(res + "\n")
            print(res)
        except Exception as e:
            print("Error al crear log: " + str(e))
