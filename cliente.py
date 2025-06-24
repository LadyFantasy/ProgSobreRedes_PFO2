import requests
import getpass

BASE_URL = 'http://127.0.0.1:5000'

def registrar_usuario():
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese contraseña: ")
    
    url = f"{BASE_URL}/registro"
    payload = {'usuario': usuario, 'contraseña': contraseña}
    
    try:
        response = requests.post(url, json=payload)
        print(response.json())
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar con el servidor.")

def iniciar_sesion_y_ver_tareas():
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese contraseña: ")

   
    login_url = f"{BASE_URL}/login"
    try:
        login_response = requests.post(login_url, auth=(usuario, contraseña))

        if login_response.status_code == 200:
            print("Login exitoso. Accediendo a las tareas...")
            
            tareas_url = f"{BASE_URL}/tareas"
            tareas_response = requests.get(tareas_url, auth=(usuario, contraseña))

            if tareas_response.status_code == 200:
                print("\n--- Página de Tareas ---")
                print(tareas_response.text)
                print("------------------------\n")
            else:
                print(f"Error al acceder a tareas: {tareas_response.status_code}")

        elif login_response.status_code == 401:
            print("Error: Usuario o contraseña incorrectos.")
        else:
            print(f"Error en el login: {login_response.status_code}")
            print(login_response.json())

    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar con el servidor.")

def main():
    while True:
        print("\n--- Sistema de Gestión de Tareas ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión y ver tareas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            iniciar_sesion_y_ver_tareas()
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main() 