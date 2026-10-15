# Proyecto: Peritaje técnico documental de accidentes de tránsito

class Persona:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def mostrar_datos(self):
        return f"Nombre: {self.nombre} | Identificación: {self.identificacion}"


class Conductor(Persona):
    def __init__(self, nombre, identificacion, licencia):
        super().__init__(nombre, identificacion)
        self.licencia = licencia

    def mostrar_datos(self):
        return f"{super().mostrar_datos()} | Licencia: {self.licencia}"


class Peaton(Persona):
    def __init__(self, nombre, identificacion, observacion):
        super().__init__(nombre, identificacion)
        self.observacion = observacion

    def mostrar_datos(self):
        return f"{super().mostrar_datos()} | Observación: {self.observacion}"


class Vehiculo:
    def __init__(self, placa, marca, tipo, danos):
        self.placa = placa
        self.marca = marca
        self.tipo = tipo
        self.danos = danos

    def mostrar_datos(self):
        return f"{self.marca} ({self.tipo}), placa {self.placa}. Daños: {self.danos}"


class Accidente:
    def __init__(self, codigo, fecha, lugar, descripcion):
        self.codigo = codigo
        self.fecha = fecha
        self.lugar = lugar
        self.descripcion = descripcion
        self.vehiculos = []
        self.personas = []
        self.evidencias = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def agregar_persona(self, persona):
        self.personas.append(persona)


class Peritaje:
    def __init__(self, numero_informe, accidente):
        self.numero_informe = numero_informe
        self.accidente = accidente

    def mostrar_informe(self):
        print("INFORME DE PERITAJE TÉCNICO DOCUMENTAL")
        print(f"Número de informe: {self.numero_informe}")
        print(f"Código del accidente: {self.accidente.codigo}")
        print(f"Fecha: {self.accidente.fecha}")
        print(f"Lugar: {self.accidente.lugar}")
        print(f"Descripción: {self.accidente.descripcion}")

        print("\nVEHÍCULOS")
        if self.accidente.vehiculos:
            for vehiculo in self.accidente.vehiculos:
                print(f"- {vehiculo.mostrar_datos()}")
        else:
            print("- No se registraron vehículos.")

        print("\nPERSONAS REGISTRADAS")
        if self.accidente.personas:
            for persona in self.accidente.personas:
                print(f"- {persona.mostrar_datos()}")
        else:
            print("- No se registraron personas.")


if __name__ == "__main__":
    # Crear el accidente
    accidente = Accidente(
        "AT-001",
        "15/10/2026",
        "Quito, Simon Bolivar",
        "Colisión entre un automóvil y una motocicleta."
    )

    # Crear objetos y agregarlos al accidente
    conductor = Conductor("Bayarod Paredes", "1724308349", "TIPO C")
    peaton = Peaton("Ana López", "0506070809", "Se encontraba en la acera.")
    vehiculo = Vehiculo("PWP-0184", "Chevrolet", "automóvil", "Daño en el parachoques delantero.")
    

    accidente.agregar_persona(conductor)
    accidente.agregar_persona(peaton)
    accidente.agregar_vehiculo(vehiculo)

    # Crear el peritaje y mostrar el resultado
    peritaje = Peritaje("INF-001", accidente)
    peritaje.mostrar_informe()
