# PROYECTO_2P

Proyecto correspondiente al Segundo Parcial de DAWA (Desarrollo de Aplicaciones Web y Apps).  
Consiste en una aplicación Full Stack desplegada mediante contenedores Docker, compuesta por:

- Frontend (cliente web)
- Backend (API REST)
- Base de datos
- Orquestación con Docker Compose

---

## Descripción General

El sistema implementa una arquitectura cliente-servidor donde:

- El frontend permite la interacción del usuario.
- El backend expone servicios REST.
- La base de datos gestiona la persistencia.
- Docker Compose permite levantar todos los servicios de forma integrada.

---

## Arquitectura

Usuario (Browser)
        |
        v
Frontend (TypeScript / JavaScript)
        | HTTP / REST
        v
Backend (Python)
        |
        v
Base de Datos

Cada componente se ejecuta en su propio contenedor Docker.

---

## Tecnologías Utilizadas

### Frontend
- TypeScript
- JavaScript
- CSS

### Backend
- Python
- API REST

### Base de Datos
- Sistema relacional configurado vía Docker
- Scripts de inicialización en `zinitdb/`

### DevOps
- Docker
- Docker Compose

---

## Estructura del Proyecto

PROYECTO_2P/
│
├── frontend/              Aplicación cliente
├── services/              Backend / APIs
├── zinitdb/               Scripts de inicialización de BD
├── docker-compose.yml     Orquestación de contenedores
└── README.md

---

## Instalación y Ejecución

### Requisitos

- Docker
- Docker Compose

Verificar instalación:

docker --version
docker compose version

---

### Clonar el repositorio

git clone https://github.com/ElCabaKing/PROYECTO_2P.git
cd PROYECTO_2P

---

### Construir y levantar el proyecto

docker compose up --build

Esto iniciará:

- Contenedor del frontend
- Contenedor del backend
- Contenedor de la base de datos

---

### Acceso al sistema

Una vez levantados los contenedores:

- Frontend: http://localhost:<puerto>
- Backend API: http://localhost:<puerto>

Los puertos específicos están definidos en docker-compose.yml.

---

## Funcionalidades Generales

- Consumo de API REST desde el frontend
- Operaciones CRUD
- Persistencia en base de datos
- Inicialización automática de datos mediante scripts

---

## Endpoints (Ejemplo REST)

| Método | Endpoint         | Descripción            |
|--------|------------------|------------------------|
| GET    | /api/...         | Obtener registros      |
| POST   | /api/...         | Crear registro         |
| PUT    | /api/.../{id}    | Actualizar registro    |
| DELETE | /api/.../{id}    | Eliminar registro      |

---

## Docker

El archivo docker-compose.yml define los servicios:

- Frontend
- Backend
- Base de datos

Para detener los servicios:

docker compose down

---

## Licencia

Proyecto con fines académicos.
"""
