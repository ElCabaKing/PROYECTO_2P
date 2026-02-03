
-- ROLES
INSERT INTO tb_roles (Nombre) VALUES
('Director'),
('Administrador'),
('Empleado');

-- RESTAURANTES
INSERT INTO tb_restaurante (Nombre) VALUES
('Restaurante El Buen Sabor'),
('Restaurante Costa Grill');

-- SUCURSALES
INSERT INTO tb_sucursal (Direccion, restaurant_id) VALUES
('Av. Principal y Calle 10', 1),
('Mall Central - Local 45', 1),
('Av. Malecón y Olmedo', 2),
('Centro Comercial Norte', 2);

-- =========================
-- USUARIOS
-- =========================

-- DIRECTOR (SIN SUCURSAL)
INSERT INTO tb_user (
    cedula, nombre, apellido, correo, contrasena_hash,
    role_id, restaurant_id, sucursal_id
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
INSERT INTO tb_user (
    cedula, nombre, apellido, correo, contrasena_hash,
    role_id, restaurant_id, sucursal_id
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
INSERT INTO tb_user (
    cedula, nombre, apellido, correo, contrasena_hash,
    role_id, restaurant_id, sucursal_id
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
INSERT INTO tb_menus (nombre, path, icono, descripcion) VALUES
('Dashboard', '/dashboard', 'home', 'Panel principal de control'),
('Usuarios', '/users', 'users', 'Gestión de usuarios del sistema'),
('Perfil', '/profile', 'user', 'Mi perfil de usuario'),
('Inventario', '/inventory', 'box', 'Gestión de productos'),
('Reportes', '/reports', 'bar-chart', 'Reportes del sistema'),
('Configuración', '/settings', 'settings', 'Configuración del sistema');

-- =========================
-- ASIGNACIONES DE MENUS A ROLES
-- =========================
INSERT INTO tb_rol_menu (role_id, menu_id) VALUES
(1, 1), -- Director: Dashboard
(1, 2), -- Director: Usuarios
(1, 3), -- Director: Perfil
(1, 4), -- Director: Inventario
(1, 5), -- Director: Reportes
(1, 6), -- Director: Configuración
(2, 1), -- Administrador: Dashboard
(2, 2), -- Administrador: Usuarios
(2, 3), -- Administrador: Perfil
(2, 4), -- Administrador: Inventario
(2, 5), -- Administrador: Reportes
(3, 1), -- Empleado: Dashboard
(3, 3), -- Empleado: Perfil
(3, 4); -- Empleado: Inventario