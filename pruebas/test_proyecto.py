
# Importar las clases del proyecto
from modelos.conductor import Conductor
from modelos.peaton import Peaton
from modelos.vehiculo import Vehiculo
from modelos.accidente import Accidente
from modelos.evidencia import Evidencia
from modelos.peritaje import Peritaje


# Prueba 1: Crear accidente
accidente = Accidente(
    "AT-002",
    "22/10/2026",
    "Quito",
    "Choque entre dos vehículos"
)

assert accidente.codigo == "AT-002"
print("Prueba 1 correcta: Accidente creado.")


# Prueba 2: Registrar conductor
conductor = Conductor("Juan Pérez", "1234567890", "Tipo C")
accidente.agregar_persona(conductor)

assert len(accidente.personas) == 1
print("Prueba 2 correcta: Conductor registrado.")


# Prueba 3: Registrar peatón
peaton = Peaton("Ana López", "0987654321", "Testigo del accidente")
accidente.agregar_persona(peaton)

assert len(accidente.personas) == 2
print("Prueba 3 correcta: Peatón registrado.")


# Prueba 4: Registrar vehículo
vehiculo = Vehiculo(
    "PBC-1234",
    "Toyota",
    "Automóvil",
    "Daños en el parachoques"
)

accidente.agregar_vehiculo(vehiculo)

assert len(accidente.vehiculos) == 1
print("Prueba 4 correcta: Vehículo registrado.")


# Prueba 5: Registrar evidencia
evidencia = Evidencia(
    "EV-002",
    "Fotografía",
    "Imagen del vehículo",
    "Av. Simón Bolívar",
    "Se observan daños"
)

accidente.agregar_evidencia(evidencia)

assert len(accidente.evidencias) == 1
print("Prueba 5 correcta: Evidencia registrada.")


# Prueba 6: Herencia y polimorfismo
assert "Licencia" in conductor.mostrar_datos()
assert "Observación" in peaton.mostrar_datos()

print("Prueba 6 correcta: Herencia y polimorfismo.")


# Prueba 7: Crear peritaje
peritaje = Peritaje("INF-002", accidente)

assert peritaje is not None
print("Prueba 7 correcta: Peritaje creado.")


# Prueba 8: Código incorrecto
error_codigo = False

try:
    accidente_incorrecto = Accidente(
        "ABC",
        "22/10/2026",
        "Quito",
        "Choque entre vehículos"
    )
except ValueError:
    error_codigo = True

assert error_codigo == True
print("Prueba 8 correcta: Código incorrecto rechazado.")


# Prueba 9: Lugar vacío
error_lugar = False

try:
    accidente_incorrecto = Accidente(
        "AT-003",
        "22/10/2026",
        "",
        "Choque entre vehículos"
    )
except ValueError:
    error_lugar = True

assert error_lugar == True
print("Prueba 9 correcta: Lugar vacío rechazado.")


# Prueba 10: Descripción vacía
error_descripcion = False

try:
    accidente_incorrecto = Accidente(
        "AT-004",
        "22/10/2026",
        "Quito",
        ""
    )
except ValueError:
    error_descripcion = True

assert error_descripcion == True
print("Prueba 10 correcta: Descripción vacía rechazada.")


# Resultado final
print("\nTODAS LAS PRUEBAS TERMINARON CORRECTAMENTE.")
