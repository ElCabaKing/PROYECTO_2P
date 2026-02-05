-- =========================
-- EXTENSIONES
-- =========================
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- =========================
-- ROLES
-- =========================
CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- =========================
-- RESTAURANTES (TENANT)
-- =========================
CREATE TABLE IF NOT EXISTS restaurantes (
    Id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    legal_name VARCHAR(255),
    tax_id VARCHAR(50),
    logo_url VARCHAR(500),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT chk_name_length CHECK (LENGTH(name) >= 2)
);

-- =========================
-- SUCURSALES
-- =========================
CREATE TABLE IF NOT EXISTS sucursales (
    Id SERIAL PRIMARY KEY,
    restaurante_id INT NOT NULL,
    name VARCHAR(150) NOT NULL,
    address VARCHAR(500) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(255),
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    tolerance_minutes INTEGER DEFAULT 15 NOT NULL,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT fk_sucursal_restaurante
        FOREIGN KEY (restaurante_id) REFERENCES restaurantes(id) ON DELETE CASCADE,
    CONSTRAINT chk_tolerance_positive
        CHECK (tolerance_minutes > 0 AND tolerance_minutes <= 60)
);

-- =========================
-- USUARIOS (CON RESTAURANTE Y SUCURSAL DIRECTOS)
-- =========================
CREATE TABLE IF NOT EXISTS usuarios (
    Id SERIAL PRIMARY KEY,
    cedula VARCHAR(20) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    contrasena_hash VARCHAR(100) NOT NULL,
    role_id INT NOT NULL,
    restaurante_id INT NOT NULL,
    sucursal_id INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT uq_usuario_correo UNIQUE (correo),
    CONSTRAINT uq_usuario_cedula UNIQUE (cedula),

    CONSTRAINT fk_usuario_role
        FOREIGN KEY (role_id) REFERENCES roles(id),

    CONSTRAINT fk_usuario_restaurante
        FOREIGN KEY (restaurante_id) REFERENCES restaurantes(id),

    CONSTRAINT fk_usuario_sucursal
        FOREIGN KEY (sucursal_id) REFERENCES sucursales(id),

    -- Un director (role_id = 1) no debe estar atado a una sucursal
    CONSTRAINT chk_director_sucursal
        CHECK (
            NOT (role_id = 1 AND sucursal_id IS NOT NULL)
        )
);

-- =========================
-- MESAS
-- =========================
CREATE TABLE IF NOT EXISTS mesas (
    Id SERIAL PRIMARY KEY,
    sucursal_id INT NOT NULL,
    table_number VARCHAR(20) NOT NULL,
    capacity_min INTEGER NOT NULL DEFAULT 1,
    capacity_max INTEGER NOT NULL,
    location VARCHAR(100),
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT fk_mesa_sucursal
        FOREIGN KEY (sucursal_id) REFERENCES sucursales(id) ON DELETE CASCADE,

    CONSTRAINT chk_capacity_valid
        CHECK (capacity_min > 0 AND capacity_max >= capacity_min),

    CONSTRAINT uq_mesa_sucursal
        UNIQUE (sucursal_id, table_number)
);

-- =========================
-- HORARIOS
-- =========================
CREATE TABLE IF NOT EXISTS horarios (
    Id SERIAL PRIMARY KEY,
    sucursal_id INT NOT NULL,
    day_of_week INTEGER NOT NULL,
    opening_time TIME NOT NULL,
    closing_time TIME NOT NULL,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT fk_horario_sucursal
        FOREIGN KEY (sucursal_id) REFERENCES sucursales(id) ON DELETE CASCADE,

    CONSTRAINT chk_day_of_week
        CHECK (day_of_week BETWEEN 0 AND 6),

    CONSTRAINT chk_time_valid
        CHECK (opening_time < closing_time),

    CONSTRAINT uq_horario_sucursal_day
        UNIQUE (sucursal_id, day_of_week)
);

-- =========================
-- PROMOCIONES
-- =========================
CREATE TABLE IF NOT EXISTS promociones (
    Id SERIAL PRIMARY KEY,
    sucursal_id INT NOT NULL,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    discount_percentage DECIMAL(5,2),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT fk_promocion_sucursal
        FOREIGN KEY (sucursal_id) REFERENCES sucursales(id) ON DELETE CASCADE,

    CONSTRAINT chk_dates_valid
        CHECK (end_date >= start_date),

    CONSTRAINT chk_discount_range
        CHECK (
            discount_percentage IS NULL
            OR (discount_percentage BETWEEN 0 AND 100)
        )
);

-- =========================
-- MENUS
-- =========================
CREATE TABLE IF NOT EXISTS menus (
    Id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    path VARCHAR(255) NOT NULL UNIQUE,
    icono VARCHAR(100),
    descripcion VARCHAR(255),
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- PERMISOS (ROL ↔ MENU)
-- =========================
CREATE TABLE IF NOT EXISTS rol_menu (
    Id SERIAL PRIMARY KEY,
    role_id INT NOT NULL,
    menu_id INT NOT NULL,

    CONSTRAINT fk_rol_menu_role
        FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE,

    CONSTRAINT fk_rol_menu_menu
        FOREIGN KEY (menu_id) REFERENCES menus(id) ON DELETE CASCADE,

    CONSTRAINT uq_rol_menu
        UNIQUE (role_id, menu_id)
);


-- ================
-- Cosas de reserva
-- ================

-- CREATE TABLE cliente (
--     cliente_id SERIAL PRIMARY KEY,
--     cliente_nombre VARCHAR(64) NOT NULL,
--     cliente_contacto VARCHAR(64) UNIQUE NOT NULL
-- );

CREATE TABLE producto (
    producto_id SERIAL PRIMARY KEY,
    producto_nombre VARCHAR(64) NOT NULL,
    prodcuto_precio FLOAT NOT NULL,
    producto_descuento FLOAT
);

CREATE TABLE reserva (
    reserva_id SERIAL PRIMARY KEY,
    reserva_fi DATE NOT NULL, -- Fecha de Inicio
    reserva_ff DATE NOT NULL, -- Fecha de Fin
    reserva_fr DATE, -- Fecha de Recordatorio
    reserva_estado VARCHAR(64) NOT NULL,
    -- reserva_cid INT NOT NULL REFERENCES cliente(cliente_id) ON DELETE CASCADE,
    reserva_sid INT NOT NULL REFERENCES sucursales(id) ON DELETE CASCADE
);

CREATE TABLE menurese ( -- Menu de la reserva (Reserva - Producto)
    menurese_rid INT REFERENCES reserva ( reserva_id) ON DELETE CASCADE,
    menurese_pid INT REFERENCES producto(producto_id) ON DELETE CASCADE,
    PRIMARY KEY (menurese_rid, menurese_pid)
);

CREATE TABLE menurest ( -- Menu del restaurante (Restaurante - Producto)
    menurest_rid INT REFERENCES restaurantes(id) ON DELETE CASCADE,
    menurest_pid INT REFERENCES producto   (   producto_id) ON DELETE CASCADE,
    PRIMARY KEY (menurest_rid, menurest_pid)
);
