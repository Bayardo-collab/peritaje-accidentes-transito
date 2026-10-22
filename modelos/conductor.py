
from .persona import Persona


class Conductor(Persona):
    def __init__(self, nombre, identificacion, licencia):
        super().__init__(nombre, identificacion)
        self._licencia = licencia

    def mostrar_datos(self):
        return f"{super().mostrar_datos()} | Licencia: {self._licencia}"
