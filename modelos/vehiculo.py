
class Vehiculo:
    def __init__(self, placa, marca, tipo, danos):
        self._placa = placa
        self._marca = marca
        self._tipo = tipo
        self._danos = danos

    @property
    def placa(self):
        return self._placa

    def mostrar_datos(self):
        return f"{self._marca} ({self._tipo}), placa {self._placa}. Daños: {self._danos}"
