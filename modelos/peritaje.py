
class Peritaje:
    def __init__(self, numero_informe, accidente):
        self._numero_informe = numero_informe
        self._accidente = accidente

    def mostrar_informe(self):
        print("\nINFORME DE PERITAJE TÉCNICO DOCUMENTAL")
        print(f"Número de informe: {self._numero_informe}")

        print("\nDATOS DEL ACCIDENTE")
        print(self._accidente.mostrar_resumen())

        print("\nVEHÍCULOS")
        if self._accidente.vehiculos:
            for vehiculo in self._accidente.vehiculos:
                print(f"- {vehiculo.mostrar_datos()}")
        else:
            print("- No se registraron vehículos.")

        print("\nPERSONAS REGISTRADAS")
        if self._accidente.personas:
            for persona in self._accidente.personas:
                print(f"- {persona.mostrar_datos()}")
        else:
            print("- No se registraron personas.")

        print("\nEVIDENCIAS")
        if self._accidente.evidencias:
            for evidencia in self._accidente.evidencias:
                print(evidencia.mostrar_detalle())
        else:
            print("- No se registraron evidencias.")
