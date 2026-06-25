def validar_nombre(nombre):
    for letra in nombre:
        if letra != " ":
            return True
    return False


def validar_edad(edad):
    try:
        edad = int(edad)
        if edad > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def validar_salario(salario):
    try:
        salario = float(salario)
        if salario > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def ingreso_datos(listado):
    nombre = input("Ingrese el nombre del empleado: ")
    if not validar_nombre(nombre):
        print("El nombre no puede estar vacío.")
        return

    edad = input("Ingrese la edad del empleado: ")
    if not validar_edad(edad):
        print("Edad inválida.")
        return

    salario = input("Ingrese el salario del empleado: ")
    if not validar_salario(salario):
        print("Salario inválido.")
        return

    empleado = {
        "nombre": nombre,
        "edad": int(edad),
        "salario": float(salario),
        "activo": False
    }
    listado.append(empleado)
    print("Empleado agregado correctamente.")


def buscar_empleado(listado, nombre_buscar):
    posicion = 0
    for empleado in listado:
        if empleado["nombre"] == nombre_buscar:
            return posicion
        posicion += 1
    return -1


def eliminar_empleado(listado):
    nombre = input("Ingrese el nombre del empleado a eliminar: ")
    posicion = buscar_empleado(listado, nombre)
    if posicion == -1:
        print(f"El empleado '{nombre}' no se encuentra registrado.")
    else:
        listado.pop(posicion)
        print("Empleado eliminado correctamente.")

def actualizar_estado(listado):
    for empleado in listado:
        if empleado["edad"] >= 18:
            empleado["activo"] = True
        else:
            empleado["activo"] = False
    print("Estados actualizados.")

def mostrar_empleados(listado):
    actualizar_estado(listado)
    print("\n=== LISTA DE EMPLEADOS ===")
    if len(listado) == 0:
        print("No hay empleados registrados")
        return
    for empleado in listado:
        if empleado["activo"] == True:
            estado = "ACTIVO"
        else:
            estado = "INACTIVO"
        print(f"""
Nombre: {empleado["nombre"]}
Edad: {empleado["edad"]}
Salario: {empleado["salario"]}
Estado: {estado}
************************************
""")

def mostrar_menu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Agregar empleado
2. Buscar empleado
3. Eliminar empleado
4. Actualizar estado
5. Mostrar empleados
6. Salir
===================================
""")


def leer_opcion():
    while True:
        opcion = input("Ingrese una opción: ")

        if opcion in ("1", "2", "3", "4", "5", "6"):
            return opcion
        else:
            print("Opción inválida.")


def menu():
    empleados = []
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        match opcion:
            case "1":
                ingreso_datos(empleados)
            case "2":
                nombre = input("Ingrese el nombre del empleado: ")
                posicion = buscar_empleado(empleados, nombre)
                if posicion == -1:
                    print("Empleado no encontrado.")
                else:
                    print(f"""
Empleado encontrado en la posición: {posicion}
Nombre: {empleados[posicion]["nombre"]}
Edad: {empleados[posicion]["edad"]}
Salario: {empleados[posicion]["salario"]}
Estado: {empleados[posicion]["activo"]}
""")
            case "3":
                eliminar_empleado(empleados)
            case "4":
                actualizar_estado(empleados)
            case "5":
                mostrar_empleados(empleados)
            case "6":
                print("Gracias por usar el sistema. Vuelva pronto.")
                break

menu()