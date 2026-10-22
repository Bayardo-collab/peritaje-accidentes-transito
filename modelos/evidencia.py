class Evidencia:
    def __init__(self, codigo, tipo, descripcion, ubicacion, observacion):
        self._codigo = codigo
        self._tipo = tipo
        self._descripcion = descripcion
        self._ubicacion = ubicacion
        self._observacion = observacion

    @property
    def codigo(self):
        return self._codigo

    def mostrar_detalle(self):
        return (
            f"Código: {self._codigo}\n"
            f"Tipo: {self._tipo}\n"
            f"Descripción: {self._descripcion}\n"
            f"Ubicación: {self._ubicacion}\n"
            f"Observación: {self._observacion}"
        )
