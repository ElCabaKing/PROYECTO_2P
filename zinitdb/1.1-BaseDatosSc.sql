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
    restaurant_id INT NOT NULL,
    CONSTRAINT fk_sucursal_restaurante
        FOREIGN KEY (restaurant_id) REFERENCES tb_restaurante(Id)
);

CREATE TABLE tb_user (
    id SERIAL PRIMARY KEY,
    cedula VARCHAR(20) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    contrasena_hash VARCHAR(100) NOT NULL,
    role_id INT NOT NULL,
    restaurant_id INT NOT NULL,
    Activo BOOLEAN DEFAULT TRUE,
    sucursal_id INT,
    CONSTRAINT fk_user_role
        FOREIGN KEY (role_id) REFERENCES tb_roles(Id),
    CONSTRAINT fk_user_restaurante
        FOREIGN KEY (restaurant_id) REFERENCES tb_restaurante(Id),
    CONSTRAINT fk_user_sucursal
        FOREIGN KEY (sucursal_id) REFERENCES tb_sucursal(Id)
);


ALTER TABLE tb_user
ADD CONSTRAINT uq_tb_user_correo UNIQUE (correo);

ALTER TABLE tb_user
ADD CONSTRAINT uq_tb_user_cedula UNIQUE (cedula);

ALTER TABLE tb_user
ADD CONSTRAINT chk_director_sucursal
CHECK (
    NOT (role_id = 1 AND sucursal_id IS NOT NULL)
);