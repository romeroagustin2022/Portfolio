import json  # <-- CAMBIO: importar json, no jsonschema

ARCHIVO = "tareas.json"  # <-- Usamos mayúsculas para constantes (buena práctica)

def cargar_tareas():
    try:
        with open(ARCHIVO, "r") as archivo:  # <-- CORREGIDO: open una vez, cierre de comillas
            return json.load(archivo)         # <-- indentado correctamente
    except FileNotFoundError:
        return []  # Si no existe el archivo, devolvemos lista vacía

def guardar_tareas(tareas):  # <-- parámetro se llama tareas (no lista_tareas)
    with open(ARCHIVO, "w") as archivo:
        json.dump(tareas, archivo, indent=4)  # <-- CORREGIDO: tareas en lugar de lista_tareas

def agregar_tarea(tareas):  # <-- AHORA RECIBE LA LISTA como parámetro
    nueva = input("📝 Escribe la nueva tarea: ")
    tareas.append(nueva)      # <-- usamos el parámetro
    guardar_tareas(tareas)    # <-- guardamos
    print("✅ Tarea agregada exitosamente.")

def ver_tareas(tareas):  # <-- parámetro se llama tareas
    if not tareas:
        print("📭 No hay tareas pendientes.")
    else:
        print("\n📋 Tareas pendientes:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def menu():
    print("\n--- Menú de opciones ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")
    return input("Seleccione una opción: ")

def main():
    tareas = cargar_tareas()  # Cargamos las tareas al iniciar
    
    while True:  # <-- Bucle infinito hasta que el usuario elija salir
        opcion = menu()
        
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            print("👋 Saliendo del programa...")
            break  # <-- Salimos del bucle, terminando el programa
        else:
            print("❌ Opción inválida. Por favor, seleccione 1, 2 o 3.")
            # No llamamos a main() recursivamente, solo seguimos en el bucle

if __name__ == "__main__":
    main()