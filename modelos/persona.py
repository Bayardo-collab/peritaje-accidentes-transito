class Persona:
    def __init__(self, nombre, identificacion):
        self._nombre = nombre
        self._identificacion = identificacion

    @property
    def identificacion(self):
        return self._identificacion

    def mostrar_datos(self):
        return f"Nombre: {self._nombre} | Identificación: {self._identificacion}"
