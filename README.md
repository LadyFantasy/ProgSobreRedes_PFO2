# PFO 2: Sistema de gestión de tareas con API y DB

Este proyecto implementa una API RESTful simple utilizando Flask para gestionar usuarios y tareas. Proporciona endpoints para el registro de usuarios, inicio de sesión y acceso a un área de tareas protegida. La persistencia de datos se maneja con SQLite y las contraseñas se almacenan de forma segura utilizando hashing.

## Características

- **API REST**: Endpoints para gestionar recursos.
- **Autenticación**: Autenticación básica para proteger rutas.
- **Seguridad**: Hashing de contraseñas para un almacenamiento seguro.
- **Base de datos**: SQLite para la persistencia de datos de usuario.
- **Cliente de consola**: Un cliente interactivo para interactuar con la API.

## Instrucciones de instalación y ejecución

### 1. Prerrequisitos

- Python 3.6+
- `pip` y `venv`

### 2. Clonar el repositorio

```bash
git clone <URL-DEL-REPOSITORIO>
cd <NOMBRE-DEL-DIRECTORIO>
```

### 3. Crear y activar un entorno virtual

Para Windows:

```bash
python -m venv venv
venv\\Scripts\\activate
```

Para macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Iniciar el servidor

```bash
python servidor.py
```

El servidor Flask se ejecutará en `http://127.0.0.1:5000`. La primera vez que se inicie, creará automáticamente el archivo de base de datos `usuarios.db`.

### 6. Usar el cliente de consola

En una nueva terminal (con el entorno virtual activado), ejecutar el cliente:

```bash
python cliente.py
```

Sigue las instrucciones en la consola para registrarte, iniciar sesión y ver la página de bienvenida.

## Documentación de la API

Puedes probar la API utilizando `curl` o cualquier otro cliente de API.

### Registro de usuario

- **Endpoint**: `POST /registro`
- **Descripción**: Registra un nuevo usuario.
- **Body (JSON)**:
  ```json
  {
    "usuario": "nombre_de_usuario",
    "contraseña": "tu_contraseña"
  }
  ```
- **Ejemplo con `curl`**:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d "{\"usuario\":\"testuser\",\"contraseña\":\"1234\"}" http://127.0.0.1:5000/registro
  ```
- **Respuesta exitosa (201)**:
  ```json
  {
    "mensaje": "Usuario registrado exitosamente"
  }
  ```

### Inicio de sesión

- **Endpoint**: `POST /login`
- **Descripción**: Verifica las credenciales del usuario. Utiliza autenticación básica.
- **Ejemplo con `curl`**:
  ```bash
  curl -X POST -u "testuser:1234" http://127.0.0.1:5000/login
  ```
- **Respuesta exitosa (200)**:
  ```json
  {
    "mensaje": "Inicio de sesión exitoso para el usuario: testuser"
  }
  ```

### Ver tareas (página de bienvenida)

- **Endpoint**: `GET /tareas`
- **Descripción**: Muestra una página de bienvenida en HTML. Requiere autenticación básica.
- **Ejemplo con `curl`**:
  ```bash
  curl -u "testuser:1234" http://127.0.0.1:5000/tareas
  ```
- **Respuesta exitosa (200)**:
  ```html
  <!DOCTYPE html>
  <html lang="es">
    ...
    <h1>¡Bienvenido a la Gestión de Tareas, testuser!</h1>
    ...
  </html>
  ```

## Dependencias y para qué se usan

- **Flask**: Framework principal para crear la API y servir las rutas.
- **flask_httpauth**: Para proteger rutas con autenticación básica HTTP.
- **werkzeug**: Para el hash seguro de contraseñas y utilidades de seguridad.
- **requests**: Usado en el cliente de consola para hacer peticiones HTTP al servidor.
