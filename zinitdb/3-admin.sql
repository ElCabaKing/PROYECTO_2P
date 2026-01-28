-- ADMIN TABLES

-- Tabla: restaurantes (tenant principal)
CREATE TABLE IF NOT EXISTS restaurantes (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(150) NOT NULL,
  legal_name VARCHAR(255),
  tax_id VARCHAR(50),
  logo_url VARCHAR(500),
  is_active BOOLEAN DEFAULT TRUE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  CONSTRAINT chk_name_length CHECK (LENGTH(name) >= 2)
);

-- Tabla: sucursales
CREATE TABLE IF NOT EXISTS sucursales (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  restaurante_id UUID NOT NULL,
  name VARCHAR(150) NOT NULL,
  address VARCHAR(500) NOT NULL,
  phone VARCHAR(20),
  email VARCHAR(255),
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  tolerance_minutes INTEGER DEFAULT 15 NOT NULL,
  is_active BOOLEAN DEFAULT TRUE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  CONSTRAINT fk_sucursal_restaurante FOREIGN KEY (restaurante_id) REFERENCES restaurantes(id) ON DELETE CASCADE,
  CONSTRAINT chk_tolerance_positive CHECK (
    tolerance_minutes > 0
    AND tolerance_minutes <= 60
  ),
  CONSTRAINT chk_latitude_range CHECK (
    latitude IS NULL
    OR (
      latitude >= -90
      AND latitude <= 90
    )
  ),
  CONSTRAINT chk_longitude_range CHECK (
    longitude IS NULL
    OR (
      longitude >= -180
      AND longitude <= 180
    )
  )
);

-- Tabla: mesas
CREATE TABLE IF NOT EXISTS mesas (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  sucursal_id UUID NOT NULL,
  table_number VARCHAR(20) NOT NULL,
  capacity_min INTEGER NOT NULL DEFAULT 1,
  capacity_max INTEGER NOT NULL,
  location VARCHAR(100),
  description TEXT,
  is_active BOOLEAN DEFAULT TRUE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  CONSTRAINT fk_mesa_sucursal FOREIGN KEY (sucursal_id) REFERENCES sucursales(id) ON DELETE CASCADE,
  CONSTRAINT chk_capacity_valid CHECK (
    capacity_min > 0
    AND capacity_max >= capacity_min
  ),
  CONSTRAINT uq_mesa_sucursal UNIQUE (sucursal_id, table_number)
);

-- Tabla: horarios
CREATE TABLE IF NOT EXISTS horarios (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  sucursal_id UUID NOT NULL,
  day_of_week INTEGER NOT NULL,
  opening_time TIME NOT NULL,
  closing_time TIME NOT NULL,
  is_active BOOLEAN DEFAULT TRUE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  CONSTRAINT fk_horario_sucursal FOREIGN KEY (sucursal_id) REFERENCES sucursales(id) ON DELETE CASCADE,
  CONSTRAINT chk_day_of_week CHECK (
    day_of_week >= 0
    AND day_of_week <= 6
  ),
  CONSTRAINT chk_time_valid CHECK (opening_time < closing_time),
  CONSTRAINT uq_horario_sucursal_day UNIQUE (sucursal_id, day_of_week)
);

-- Tabla: promociones
CREATE TABLE IF NOT EXISTS promociones (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  sucursal_id UUID NOT NULL,
  name VARCHAR(150) NOT NULL,
  description TEXT,
  discount_percentage DECIMAL(5, 2),
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  is_active BOOLEAN DEFAULT TRUE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  CONSTRAINT fk_promocion_sucursal FOREIGN KEY (sucursal_id) REFERENCES sucursales(id) ON DELETE CASCADE,
  CONSTRAINT chk_dates_valid CHECK (end_date >= start_date),
  CONSTRAINT chk_discount_range CHECK (
    discount_percentage IS NULL
    OR (
      discount_percentage >= 0
      AND discount_percentage <= 100
    )
  )
);

-- Relación usuarios-sucursales (acceso multitenant)
CREATE TABLE IF NOT EXISTS usuario_sucursales (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  usuario_id UUID NOT NULL,
  sucursal_id UUID NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  CONSTRAINT fk_us_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
  CONSTRAINT fk_us_sucursal FOREIGN KEY (sucursal_id) REFERENCES sucursales(id) ON DELETE CASCADE,
  CONSTRAINT uq_usuario_sucursal UNIQUE (usuario_id, sucursal_id)
);

-- TRIGGERS
CREATE TRIGGER trg_restaurantes_updated_at BEFORE
UPDATE
  ON restaurantes FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER trg_sucursales_updated_at BEFORE
UPDATE
  ON sucursales FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER trg_mesas_updated_at BEFORE
UPDATE
  ON mesas FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER trg_horarios_updated_at BEFORE
UPDATE
  ON horarios FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER trg_promociones_updated_at BEFORE
UPDATE
  ON promociones FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER trg_usuario_sucursales_updated_at BEFORE
UPDATE
  ON usuario_sucursales FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

