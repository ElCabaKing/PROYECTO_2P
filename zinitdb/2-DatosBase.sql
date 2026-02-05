-- =========================
-- ROLES
-- =========================
INSERT INTO roles (nombre) VALUES
('Director'),
('Administrador'),
('Empleado');

-- =========================
-- RESTAURANTES
-- =========================
INSERT INTO restaurantes (name) VALUES
('Restaurante El Buen Sabor'),
('Restaurante Costa Grill');

-- =========================
-- SUCURSALES
-- =========================
INSERT INTO sucursales (name, address, restaurante_id) VALUES
('Sucursal Centro', 'Av. Principal y Calle 10', 1),
('Sucursal Mall', 'Mall Central - Local 45', 1),
('Sucursal Malecón', 'Av. Malecón y Olmedo', 2),
('Sucursal Norte', 'Centro Comercial Norte', 2);

-- =========================
-- USUARIOS
-- =========================

-- DIRECTOR (SIN SUCURSAL)
INSERT INTO usuarios (
    cedula, nombre, apellido, correo, contrasena_hash,
    role_id, restaurante_id, sucursal_id
) VALUES (
    '0102030405',
    'Carlos',
    'Mendoza',
    'director@buensabor.com',
    '$2b$12$jTZhFv0NUoxGEaeFbbWSw.eZlN.1CQnHGTIN/.IZ5ZhsK/4D4OApy',
    1,
    1,
    NULL
);

-- ADMINISTRADORES
INSERT INTO usuarios (
    cedula, nombre, apellido, correo, contrasena_hash,
    role_id, restaurante_id, sucursal_id
) VALUES
(
    '0912345678',
    'Ana',
    'Lopez',
    'admin1@buensabor.com',
    '$2b$12$jTZhFv0NUoxGEaeFbbWSw.eZlN.1CQnHGTIN/.IZ5ZhsK/4D4OApy',
    2,
    1,
    1
),
(
    '0923456789',
    'Luis',
    'Perez',
    'admin2@costagrill.com',
    '$2b$12$jTZhFv0NUoxGEaeFbbWSw.eZlN.1CQnHGTIN/.IZ5ZhsK/4D4OApy',
    2,
    2,
    3
);

-- EMPLEADOS
INSERT INTO usuarios (
    cedula, nombre, apellido, correo, contrasena_hash,
    role_id, restaurante_id, sucursal_id
) VALUES
(
    '0934567890',
    'Maria',
    'Gomez',
    'empleado1@buensabor.com',
    '$2b$12$jTZhFv0NUoxGEaeFbbWSw.eZlN.1CQnHGTIN/.IZ5ZhsK/4D4OApy',
    3,
    1,
    2
),
(
    '0945678901',
    'Juan',
    'Castro',
    'empleado2@costagrill.com',
    '$2b$12$jTZhFv0NUoxGEaeFbbWSw.eZlN.1CQnHGTIN/.IZ5ZhsK/4D4OApy',
    3,
    2,
    4
);

-- =========================
-- MENUS
-- =========================
INSERT INTO menus (nombre, path, icono, descripcion) VALUES
('Dashboard', '/dashboard', 'home', 'Panel principal de control'),
('Usuarios', '/users', 'users', 'Gestión de usuarios del sistema'),
('Perfil', '/profile', 'user', 'Mi perfil de usuario'),
('Inventario', '/inventory', 'box', 'Gestión de productos'),
('Reportes', '/reports', 'bar-chart', 'Reportes del sistema'),
('Configuración', '/settings', 'settings', 'Configuración del sistema');

-- =========================
-- PERMISOS (ROL ↔ MENU)
-- =========================
INSERT INTO rol_menu (role_id, menu_id) VALUES
-- Director
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),

-- Administrador
(2, 1),
(2, 2),
(2, 3),
(2, 4),
(2, 5),

-- Empleado
(3, 1),
(3, 3),
(3, 4);
