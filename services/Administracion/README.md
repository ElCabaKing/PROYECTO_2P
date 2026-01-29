# MS Administración

Microservicio de administración para la gestión de restaurantes, sucursales, mesas, horarios y promociones.

## Requisitos

- Python 3.11+
- PostgreSQL 16+

## Estructura de Módulos

```
app/modules/
├── restaurantes/    # Gestión de restaurantes (tenants)
├── sucursales/      # Sucursales por restaurante
├── mesas/           # Mesas con capacidad y ubicación
├── horarios/        # Horarios de operación
└── promociones/     # Promociones activas
```

## Ejecución Local

### 1. Crear entorno virtual

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Crear archivo `.env`:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/restauvation
JWT_SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
CORS_ORIGINS=["http://localhost:3000"]
SECURITY_SERVICE_URL=http://localhost:5001
```

### 4. Ejecutar servidor

```bash
uvicorn src.main:app --reload --port 5001
```

El servidor estará disponible en: http://localhost:5001

### 5. Documentación API

- Swagger UI: http://localhost/api/admin/docs

## Ejecución con Docker

### Build individual

```bash
docker build -t .
docker run -p 5001:5001 --env-file .env ms-admin
```

### Con Docker Compose (desde raíz del proyecto)

```bash
cd ..
docker compose up-d
```

## Endpoints Principales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/restaurantes/` | Listar restaurantes |
| POST | `/restaurantes/` | Crear restaurante |
| GET | `/restaurantes/{id}` | Obtener restaurante |
| PUT | `/restaurantes/{id}` | Actualizar restaurante |
| DELETE | `/restaurantes/{id}` | Eliminar restaurante |
| GET | `/sucursales/` | Listar sucursales |
| POST | `/sucursales/` | Crear sucursal |
| GET | `/mesas/` | Listar mesas |
| POST | `/mesas/` | Crear mesa |
| GET | `/horarios/` | Listar horarios |
| POST | `/horarios/` | Crear horario |
| GET | `/promociones/` | Listar promociones |
| POST | `/promociones/` | Crear promoción |

## Esquema de Base de Datos

Este microservicio usa el esquema `administracion` con las tablas:

- `restaurantes` - Cadenas de restaurantes
- `sucursales` - Sucursales por restaurante
- `mesas` - Mesas por sucursal
- `horarios` - Horarios de operación
- `promociones` - Promociones activas
