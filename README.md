
# Sistema de peritaje técnico documental de accidentes de tránsito

## Problema
La información de los accidentes de tránsito puede estar desorganizada, ya que incluye datos de personas, vehículos y evidencias. Esto dificulta su registro y consulta.

## Usuario
El sistema está dirigido al personal de agentes civiles de tránsito de Quito.

## Objetivo
Desarrollar un programa en Python que permita registrar accidentes de tránsito, personas involucradas, vehículos y evidencias, para generar informes organizados en la consola.

## Funcionalidades
1. Registrar accidentes de tránsito.
2. Registrar conductores y peatones.
3. Registrar vehículos involucrados.
4. Registrar evidencias del accidente.
5. Consultar informes de peritaje.
6. Validar códigos, fechas, identificaciones y placas.
7. Evitar registros repetidos dentro de un mismo accidente.

## Clases del proyecto

- Persona: contiene los datos generales de una persona.
- Conductor: hereda de Persona y agrega la licencia.
- Peaton: hereda de Persona y agrega una observación.
- Vehiculo: almacena los datos y daños de un vehículo.
- Accidente: registra los datos del accidente y relaciona personas, vehículos y evidencias.
- Evidencia: guarda información de las evidencias.
- Peritaje: muestra un informe del accidente.

## Programación Orientada a Objetos

El proyecto utiliza:

- Clases y objetos.
- Constructores.
- Atributos y métodos.
- Encapsulación mediante atributos protegidos y propiedades.
- Herencia con super().
- Sobrescritura de métodos.
- Polimorfismo.
- Relaciones entre objetos.

## Cómo ejecutar el programa

1. Abrir la carpeta del proyecto en VS Code.
2. Abrir la terminal.
3. Ejecutar:

python main.py

4. Seleccionar una opción del menú.

## Pruebas

El proyecto incluye pruebas básicas con assert.

Para ejecutarlas:

python -m pruebas.test_proyecto

## Limitaciones

- Los registros se almacenan temporalmente mientras el programa está abierto.
- Al cerrar el programa, los registros nuevos se pierden.
- No determina culpabilidad ni responsabilidades legales.
- No reemplaza un peritaje oficial.
- Es un proyecto académico desarrollado en Python.
