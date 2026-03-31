from dotenv import load_dotenv
load_dotenv()

import common

common.init()

import src.rutas.zi
import src.rutas.ruta_cliente
import src.rutas.ruta_reserva

if __name__ == "__main__":
    common.app.run(debug=True)
