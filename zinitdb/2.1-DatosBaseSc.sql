INSERT INTO tb_roles (Nombre) VALUES
('Director'),
('Administrador'),
('Empleado');

-- RESTAURANTES
INSERT INTO tb_restaurante (Nombre) VALUES
('Restaurante El Buen Sabor'),
('Restaurante Costa Grill');

-- SUCURSALES
INSERT INTO tb_sucursal (Direccion, RestauranteId) VALUES
('Av. Principal y Calle 10', 1),
('Mall Central - Local 45', 1),
('Av. Malecón y Olmedo', 2),
('Centro Comercial Norte', 2);

-- USUARIOS
-- DIRECTOR (SIN SUCURSAL)
INSERT INTO tb_user (
    Cedula, Nombre, Apellido, Correo, ContrasenaHash,
    roleId, RestauranId, SucursalId
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
    Cedula, Nombre, Apellido, Correo, ContrasenaHash,
    roleId, RestauranId, SucursalId
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
    Cedula, Nombre, Apellido, Correo, ContrasenaHash,
    roleId, RestauranId, SucursalId
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
