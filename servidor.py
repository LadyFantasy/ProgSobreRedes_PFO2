from flask import Flask, request, jsonify, render_template
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

DATABASE = 'usuarios.db'

def obtener_conexion_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def inicializar_db():
    db = obtener_conexion_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            contrasena_hash TEXT NOT NULL
        )
    ''')
    db.commit()
    db.close()

@auth.verify_password
def autenticar(usuario, contrasena):
    db = obtener_conexion_db()
    user = db.execute('SELECT * FROM usuarios WHERE usuario = ?', (usuario,)).fetchone()
    db.close()
    if user and check_password_hash(user['contrasena_hash'], contrasena):
        return usuario

@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    if not datos or 'usuario' not in datos or 'contraseña' not in datos:
        return jsonify({'error': 'Faltan datos de usuario o contraseña'}), 400

    usuario = datos['usuario']
    contrasena = datos['contraseña']
    contrasena_hasheada = generate_password_hash(contrasena)

    try:
        db = obtener_conexion_db()
        db.execute('INSERT INTO usuarios (usuario, contrasena_hash) VALUES (?, ?)',
                     (usuario, contrasena_hasheada))
        db.commit()
        db.close()
        return jsonify({'mensaje': 'Usuario registrado exitosamente'}), 201
    except sqlite3.IntegrityError:
        db.close()
        return jsonify({'error': 'El nombre de usuario ya existe'}), 409

@app.route('/login', methods=['POST'])
@auth.login_required
def login():
    return jsonify({'mensaje': f'Inicio de sesión exitoso para el usuario: {auth.current_user()}'})

@app.route('/tareas')
@auth.login_required
def obtener_tareas():
    user_agent = request.headers.get('User-Agent', '')
    if 'Mozilla' in user_agent:
        return render_template('index.html', usuario=auth.current_user())
    else:
        return (
            f"Bienvenido a la gestión de tareas, {auth.current_user()}!\n"
            "(También puedes ver esta página en formato HTML desde tu navegador en: http://127.0.0.1:5000/tareas)",
            200,
            {'Content-Type': 'text/plain; charset=utf-8'}
        )

if __name__ == '__main__':
    inicializar_db()
    app.run(debug=True) 