
from .persona import Persona


class Peaton(Persona):
    def __init__(self, nombre, identificacion, observacion):
        super().__init__(nombre, identificacion)
        self._observacion = observacion

    def mostrar_datos(self):
        return f"{super().mostrar_datos()} | Observación: {self._observacion}"
