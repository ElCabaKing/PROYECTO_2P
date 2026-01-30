CREATE TABLE restaurante (
    restaurante_id SERIAL PRIMARY KEY,
    restaurante_nombre VARCHAR(64) NOT NULL,
    restaurante_sucursal BOOLEAN NOT NULL,
    restaurante_antisipo BOOLEAN NOT NULL,
);

CREATE TABLE usuario (
    usuario_id SERIAL PRIMARY KEY,
    usuario_nombre VARCHAR(64) UNIQUE NOT NULL,
    usuario_contrasenya VARCHAR(64) NOT NULL
);

CREATE TABLE cliente (
    cliente_id SERIAL PRIMARY KEY,
    cliente_nombre VARCHAR(64) NOT NULL,
    cliente_contacto VARCHAR(64) UNIQUE NOT NULL,
);

CREATE TABLE producto (
    producto_id SERIAL PRIMARY KEY,
    producto_nombre VARCHAR(64) NOT NULL,
    prodcuto_precio FLOAT NOT NULL,
    producto_descuento FLOAT
);

CREATE TABLE reserva (
    reserva_id SERIAL PRIMARY KEY,
    reserva_fi DATE NOT NULL -- Fecha de Inicio
    reserva_ff DATE NOT NULL -- Fecha de Fin
    reserva_fr DATE NOT NULL -- Fecha de Recordatorio
    reserva_checkin BOOLEAN NOT NULL DEFAULT FALSE
    reserva_cid INT NOT NULL REFERENCES cliente(cliente_id) ON DELETE CASCADE
    reserva_rid INT NOT NULL REFERENCES restaurante(restaurante_id) ON DELETE CASCADE
);

CREATE TABLE menurese ( -- Menu de la reserva (Reserva - Producto)
    menurese_rid INT REFERENCES reserva ( reserva_id) ON DELETE CASCADE,
    menurese_pid INT REFERENCES producto(producto_id) ON DELETE CASCADE,
    PRIMARY KEY (menurese_reserva_id, menurese_reserva_id),
);

CREATE TABLE menurest ( -- Menu del restaurante (Restaurante - Producto)
    menurest_rid INT REFERENCES restaurante(restaurante_id) ON DELETE CASCADE,
    menurest_pid INT REFERENCES producto   (   producto_id) ON DELETE CASCADE,
    PRIMARY KEY (restaurante_id, producto_id)
);
