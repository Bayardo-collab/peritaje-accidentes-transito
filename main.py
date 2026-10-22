
# Proyecto: Peritaje técnico documental de accidentes de tránsito

from modelos.conductor import Conductor
from modelos.peaton import Peaton
from modelos.vehiculo import Vehiculo
from modelos.accidente import Accidente
from modelos.evidencia import Evidencia
from modelos.peritaje import Peritaje
from datetime import datetime


def crear_datos_ejemplo():
    accidente = Accidente(
        "AT-001",
        "15/10/2026",
        "Quito, Simón Bolívar",
        "Colisión entre un automóvil y una motocicleta."
    )

    conductor = Conductor("Carlos Pérez", "1724308349", "Tipo C")
    peaton = Peaton("Ana López", "0506070809", "Se encontraba en la acera.")

    vehiculo = Vehiculo(
        "PWP-0184",
        "Chevrolet",
        "Automóvil",
        "Daño en el parachoques delantero."
    )

    evidencia = Evidencia(
        "EV-001",
        "Fotografía",
        "Imagen del vehículo después del accidente.",
        "Av. Simón Bolívar, Quito",
        "Se observa daño en la parte delantera."
    )

    accidente.agregar_persona(conductor)
    accidente.agregar_persona(peaton)
    accidente.agregar_vehiculo(vehiculo)
    accidente.agregar_evidencia(evidencia)

    return accidente


def mostrar_menu():
    print("\nSISTEMA DE PERITAJE DE ACCIDENTES")
    print("1. Registrar un accidente")
    print("2. Registrar una persona")
    print("3. Registrar un vehículo")
    print("4. Registrar una evidencia")
    print("5. Mostrar informe")
    print("0. Salir")




def pedir_codigo(accidentes):
    while True:
        codigo = input("Código (Ejemplo: AT-001): ").strip().upper()

        if not (len(codigo) == 6 and codigo.startswith("AT-") and codigo[3:].isdigit()):
            print("Error: El código debe tener el formato AT-001.")
            continue

        if codigo in accidentes:
            print("Error: Este código ya está registrado.")
            continue

        return codigo



def pedir_fecha():
    while True:
        fecha = input("Fecha (DD/MM/AAAA): ").strip()

        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha

        except ValueError:
            print("Error: Ingrese una fecha válida. Ejemplo: 22/10/2026.")




def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if not texto:
            print("Error: Este campo no puede estar vacío.")

        elif not any(letra.isalpha() for letra in texto):
            print("Error: Debe escribir una descripción con letras.")

        else:
            return texto


def pedir_identificacion():
    while True:
        identificacion = input("Identificación (10 números): ").strip()

        if len(identificacion) != 10:
            print("Error: La identificación debe tener 10 dígitos.")

        elif not identificacion.isdigit():
            print("Error: La identificación solo debe contener números.")

        else:
            return identificacion



def pedir_placa():
    while True:
        placa = input("Placa (Ejemplo: PBC-1234): ").strip().upper()

        if len(placa) != 8:
            print("Error: La placa debe tener 8 caracteres.")

        elif not placa[:3].isalpha():
            print("Error: Los primeros 3 caracteres deben ser letras.")

        elif placa[3] != "-":
            print("Error: Debe colocar un guion después de las letras.")

        elif not placa[4:].isdigit():
            print("Error: Los últimos 4 caracteres deben ser números.")

        else:
            return placa



def registrar_accidente(accidentes):
    print("\nREGISTRO DE ACCIDENTE")

    codigo = pedir_codigo(accidentes)
    fecha = pedir_fecha()
    lugar = pedir_texto("Lugar del accidente: ")
    descripcion = pedir_texto("Descripción del accidente: ")

    accidente = Accidente(codigo, fecha, lugar, descripcion)
    accidentes[codigo] = accidente
    print("\nAccidente registrado correctamente.")
    return accidente



def registrar_persona(accidentes):
    print("\nREGISTRO DE PERSONA")

    codigo = input("Código del accidente (Ejemplo: AT-001): ").strip().upper()

    if codigo not in accidentes:
        print("Error: No existe un accidente con ese código.")
        return

    accidente = accidentes[codigo]

    print("\nTipo de persona:")
    print("1. Conductor")
    print("2. Peatón")

    tipo = input("Seleccione una opción: ")

    if tipo != "1" and tipo != "2":
        print("Error: Opción incorrecta.")
        return

    nombre = pedir_texto("Nombre completo: ")
    identificacion = input("Identificación: ").strip()
    repetida = False
    for persona_registrada in accidente.personas:
        if persona_registrada.identificacion == identificacion:
            repetida = True


    if repetida:
        print("Error: Esta identificación ya está registrada en el accidente.")
        return


    if tipo == "1":
        licencia = pedir_texto("Tipo de licencia (Ejemplo: Tipo C): ")
        persona = Conductor(nombre, identificacion, licencia)

    else:
        observacion = pedir_texto("Observación del peatón: ")
        persona = Peaton(nombre, identificacion, observacion)

    accidente.agregar_persona(persona)

    print("\nPersona registrada correctamente.")




def registrar_vehiculo(accidentes):
    print("\nREGISTRO DE VEHÍCULO")

    codigo = input("Código del accidente (Ejemplo: AT-001): ").strip().upper()

    if codigo not in accidentes:
        print("Error: No existe un accidente con ese código.")
        return

    accidente = accidentes[codigo]

    placa = pedir_placa()

    # Comprobar si la placa ya está registrada
    repetida = False

    for vehiculo_registrado in accidente.vehiculos:
        if vehiculo_registrado.placa == placa:
            repetida = True

    if repetida:
        print("Error: Esta placa ya está registrada en el accidente.")
        return

    marca = pedir_texto("Marca (Ejemplo: Chevrolet): ")
    tipo = pedir_texto("Tipo (Ejemplo: Automóvil): ")
    danos = pedir_texto("Daños del vehículo: ")

    vehiculo = Vehiculo(placa, marca, tipo, danos)

    accidente.agregar_vehiculo(vehiculo)

    print("\nVehículo registrado correctamente.")



def registrar_evidencia(accidentes):
    print("\nREGISTRO DE EVIDENCIA")

    codigo_accidente = input("Código del accidente (Ejemplo: AT-001): ").strip().upper()

    if codigo_accidente not in accidentes:
        print("Error: No existe un accidente con ese código.")
        return

    accidente = accidentes[codigo_accidente]

    # Solicitar el código de la evidencia
    while True:
        codigo = input("Código de evidencia (Ejemplo: EV-001): ").strip().upper()

        if len(codigo) != 6:
            print("Error: El código debe tener 6 caracteres.")

        elif not codigo.startswith("EV-"):
            print("Error: El código debe comenzar con EV-.")

        elif not codigo[3:].isdigit():
            print("Error: Los últimos 3 caracteres deben ser números.")

        else:
            break

    # Comprobar si la evidencia ya existe
    repetida = False

    for evidencia_registrada in accidente.evidencias:
        if evidencia_registrada.codigo == codigo:
            repetida = True

    if repetida:
        print("Error: Esta evidencia ya está registrada en el accidente.")
        return

    tipo = pedir_texto("Tipo de evidencia (Ejemplo: Fotografía): ")
    descripcion = pedir_texto("Descripción de la evidencia: ")
    ubicacion = pedir_texto("Ubicación de la evidencia: ")
    observacion = pedir_texto("Observación: ")

    evidencia = Evidencia(codigo, tipo, descripcion, ubicacion, observacion)

    accidente.agregar_evidencia(evidencia)

    print("\nEvidencia registrada correctamente.")




def ejecutar():
    accidente = crear_datos_ejemplo()

    accidentes = {
        "AT-001": accidente
    }

    peritajes = {
        "AT-001": Peritaje("INF-001", accidente)
    }

    siguiente_informe = 2

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nuevo_accidente = registrar_accidente(accidentes)

            numero_informe = f"INF-{siguiente_informe:03d}"

            peritajes[nuevo_accidente._codigo] = Peritaje(
                numero_informe,
                nuevo_accidente
            )

            siguiente_informe += 1

            print(f"Número de informe asignado: {numero_informe}")

        elif opcion == "2":
            registrar_persona(accidentes)

        elif opcion == "3":
            registrar_vehiculo(accidentes)

        elif opcion == "4":
            registrar_evidencia(accidentes)

        elif opcion == "5":
            print("\nINFORMES DISPONIBLES")

            for codigo in peritajes:
                print(f"- {codigo}")

            codigo = input("Código del accidente a consultar: ").strip().upper()

            if codigo in peritajes:
                peritajes[codigo].mostrar_informe()
            else:
                print("No existe un accidente con ese código.")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción incorrecta. Intente nuevamente.")



if __name__ == "__main__":
    ejecutar()
