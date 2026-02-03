CREATE TABLE tb_roles (
    Id SERIAL PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL
);


CREATE TABLE tb_restaurante (
    Id SERIAL PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL
);


CREATE TABLE tb_sucursal (
    Id SERIAL PRIMARY KEY,
    Direccion VARCHAR(200) NOT NULL,
    RestauranteId INT NOT NULL,
    CONSTRAINT fk_sucursal_restaurante
        FOREIGN KEY (RestauranteId) REFERENCES tb_restaurante(Id)
);

CREATE TABLE tb_user (
    Id SERIAL PRIMARY KEY,
    Cedula VARCHAR(20) NOT NULL,
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Correo VARCHAR(100) NOT NULL,
    ContrasenaHash VARCHAR(100) NOT NULL,
    roleId INT NOT NULL,
    RestauranId INT NOT NULL,
    Activo BOOLEAN DEFAULT TRUE,
    SucursalId INT,
    CONSTRAINT fk_user_role
        FOREIGN KEY (roleId) REFERENCES tb_roles(Id),
    CONSTRAINT fk_user_restaurante
        FOREIGN KEY (RestauranId) REFERENCES tb_restaurante(Id),
    CONSTRAINT fk_user_sucursal
        FOREIGN KEY (SucursalId) REFERENCES tb_sucursal(Id)
);


ALTER TABLE tb_user
ADD CONSTRAINT uq_tb_user_correo UNIQUE (Correo);

ALTER TABLE tb_user
ADD CONSTRAINT uq_tb_user_cedula UNIQUE (Cedula);

ALTER TABLE tb_user
ADD CONSTRAINT chk_director_sucursal
CHECK (
    NOT (roleId = 1 AND SucursalId IS NOT NULL)
);