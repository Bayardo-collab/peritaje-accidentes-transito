
classDiagram
    direction TB

    class Persona {
        -nombre
        -identificacion
        +identificacion
        +mostrar_datos()
    }

    class Conductor {
        -licencia
        +mostrar_datos()
    }

    class Peaton {
        -observacion
        +mostrar_datos()
    }

    class Vehiculo {
        -placa
        -marca
        -tipo
        -danos
        +placa
        +mostrar_datos()
    }

    class Accidente {
        -codigo
        -fecha
        -lugar
        -descripcion
        -vehiculos
        -personas
        -evidencias
        +codigo
        +vehiculos
        +personas
        +evidencias
        +agregar_vehiculo()
        +agregar_persona()
        +agregar_evidencia()
        +mostrar_resumen()
    }

    class Evidencia {
        -codigo
        -tipo
        -descripcion
        -ubicacion
        -observacion
        +codigo
        +mostrar_detalle()
    }

    class Peritaje {
        -numero_informe
        -accidente
        +mostrar_informe()
    }

    Persona <|-- Conductor
    Persona <|-- Peaton

    Accidente o-- Persona
    Accidente o-- Vehiculo
    Accidente o-- Evidencia

    Peritaje --> Accidente
