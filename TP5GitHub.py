Datos = {
    "Alumnos": []
}
Campos = ["Nombre", "Apellido", "DNI", "Fecha de nacimiento", "Tutor", "Notas", "Faltas", "Amonestaciones"]
notas =[]


def agregar_alumno(Datos):
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (dia/mes/año): ")
    tutor = input("Ingrese el nombre del tutor del alumno: ")
    faltas = input("Ingrese las faltas del alumno: ")
    amonestaciones = input("Ingrese las amonestaciones del alumno: ")
    
    while True:
        numero = int(input("Ingrese la nota: "))
        notas.append(numero)
        confirm=input("Desea añadir otro nota? (si/no): " )
        if confirm == "no":
            break
        
            
    nuevo_alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": notas,
        "Faltas": faltas,
        "Amonestaciones": amonestaciones
    }
    Datos["Alumnos"].append(nuevo_alumno)
    print("Alumno agregado con éxito.")


def mostrar_datos(Datos):
    dni = input("Ingrese el DNI del alumno a mostrar: ")
    for alumno in Datos["Alumnos"]:
        if alumno["DNI"] == dni:
            print("Datos del alumno:")
            for clave, valor in alumno.items():
                print(f"{clave}: {valor}")
            return
    print("Alumno no encontrado.")


def modificar_datos(Datos):
    dni = input("Ingrese el DNI del alumno a modificar: ")
    for alumno in Datos["Alumnos"]:
        if alumno["DNI"] == dni:
            while True:
                campo = input("Ingrese el campo a modificar (Nombre, Apellido, Fecha de nacimiento, Tutor, Notas, Faltas, Amonestaciones): ")
                if campo not in Campos:
                    print("Error: El campo no existe.")
                    continue

                nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
                alumno[campo] = nuevo_valor
                print("Datos modificados con éxito.")

                respuesta = input("¿Desea cambiar otro dato? (si/no): ")
                if respuesta != "si":
                    break
            return
    print("Alumno no encontrado.")



def expulsar_alumno(Datos):
    dni = input("Ingrese el DNI del alumno a expulsar: ")
    for i, alumno in enumerate(Datos["Alumnos"]):
        if alumno["DNI"] == dni:
            confirmacion = input("¿Está seguro de que desea expulsar al alumno? (si/no): ")
            if confirmacion == "si":
                Datos["Alumnos"].pop(i)
                print("Alumno expulsado con éxito.")
            else:
                print("Expulsión cancelada.")
            return
    print("Alumno no encontrado.")
    
    
def inicio():
    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar un nuevo alumno")
        print("2. Mostrar datos de un alumno")
        print("3. Modificar datos de un alumno")
        print("4. Expulsar un alumno")
        print("5. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            agregar_alumno(Datos)
        elif opcion == "2":
            mostrar_datos(Datos)
        elif opcion == "3":
            modificar_datos(Datos)
        elif opcion == "4":
            expulsar_alumno(Datos)
        elif opcion == "5":
            print("Cerrando programa")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


inicio()
