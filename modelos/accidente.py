
class Accidente:
    def __init__(self, codigo, fecha, lugar, descripcion):

        
        if len(codigo) != 6:
            raise ValueError("El código debe tener 6 caracteres.")

        
        if fecha.strip() == "":
            raise ValueError("La fecha no puede estar vacía.")

        
        if lugar.strip() == "":
            raise ValueError("El lugar no puede estar vacío.")

        
        if descripcion.strip() == "":
            raise ValueError("La descripción no puede estar vacía.")

        
        self._codigo = codigo
        self._fecha = fecha
        self._lugar = lugar
        self._descripcion = descripcion

        
        self._vehiculos = []
        self._personas = []
        self._evidencias = []

    
    @property
    def codigo(self):
        return self._codigo

    
    def agregar_vehiculo(self, vehiculo):
        self._vehiculos.append(vehiculo)

    
    def agregar_persona(self, persona):
        self._personas.append(persona)

    
    def agregar_evidencia(self, evidencia):
        self._evidencias.append(evidencia)

    
    @property
    def vehiculos(self):
        return tuple(self._vehiculos)

    
    @property
    def personas(self):
        return tuple(self._personas)

    
    @property
    def evidencias(self):
        return tuple(self._evidencias)

    
    def mostrar_resumen(self):
        return (
            f"Código: {self._codigo}\n"
            f"Fecha: {self._fecha}\n"
            f"Lugar: {self._lugar}\n"
            f"Descripción: {self._descripcion}"
        )
