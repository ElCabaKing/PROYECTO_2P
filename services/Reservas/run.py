from src.app import create_app
from dotenv import load_dotenv

import common

common.init()
app = common.app

load_dotenv()

import src.rutas.zi
import src.rutas.ruta_cliente
import src.rutas.ruta_reserva

@common.app.route('/')
def asdf():
    return "asdf"

if __name__ == "__main__":
    common.app.run(host='0.0.0.0', port=5002, debug=True)
