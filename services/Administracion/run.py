from app import create_app
from src.core.logs import HandleLogs
from dotenv import load_dotenv

load_dotenv()
app = create_app()

if __name__ == '__main__':
    try:
        HandleLogs.write_log("Servicio Iniciado")
        app.run(host='0.0.0.0', port=5001, debug=True, threaded=True)
    except Exception as err:
        HandleLogs.write_error(err)
    finally:
        HandleLogs.write_log("Servicio Finalizado")