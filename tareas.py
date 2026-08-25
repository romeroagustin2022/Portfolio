import json  # ❌ Tú pusiste "jsonschema" (esa librería no existe). Es "json" a secas.

ARCHIVO = "tareas.json"  # Usé mayúsculas para constante, pero es solo nombre

def cargar_tareas():
    try:
        # ❌ Tú pusiste: "with open open(archivo, "r) as archivo:"
        # ✅ Debía ser: with open(archivo, "r") as archivo:  (sin "open" repetido y cerrar comillas)
        with open(ARCHIVO, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []  # Si no existe, devuelve lista vacía

def guardar_tareas(tareas):
    # ❌ Tú pusiste "lista_tareas" dentro, pero el parámetro se llama "tareas"
    # ✅ Lo corrijo para que use el nombre correcto
    with open(ARCHIVO, "w") as archivo:
        json.dump(tareas, archivo, indent=4)  # Uso "tareas" en vez de "lista_tareas"

def agregar_tarea(lista_tareas):  # ❌ Tú no pusiste el parámetro aquí, pero lo llamabas en main
    nueva = input("📝 Escribe la nueva tarea: ")
    lista_tareas.append(nueva)
    guardar_tareas(lista_tareas)  # Guarda la lista actualizada
    print("✅ Tarea agregada exitosamente.")

def ver_tareas(lista_tareas):
    if not lista_tareas:
        print("📭 No hay tareas pendientes.")
    else:
        print("\n📋 Tareas pendientes:")
        for i, tarea in enumerate(lista_tareas, start=1):
            print(f"{i}. {tarea}")

def menu():
    print("\n------------ Menú de opciones ------------")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")
    return input("Seleccione una opción: ")

def main():
    tareas = cargar_tareas()  # Carga las tareas al empezar
    
    while True:  # ✅ Usé un bucle while en vez de llamar a main() recursivamente
        opcion = menu()
        
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            print("👋 Saliendo del programa... ¡Tus tareas están guardadas!")
            break  # Sale del bucle y termina el programa
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()