
# Proyecto de Pruebas Automatizadas Urban Grocers API

Este proyecto contiene la suite de pruebas automatizadas para la API de Urban Grocers, enfocadas en la validación de la creación de kits de productos (/api/v1/kits) bajo distintas condiciones y valores límite según la lista de comprobación.

## Requisitos previos

- Python 3.x instalado.
- Librerías necesarias: requests y pytest.

## Instrucciones para ejecutar las pruebas

1. Clona el repositorio a tu máquina local.
2. Asegúrate de que el servidor de Urban Grocers esté encendido y actualiza la variable URL_SERVICE en el archivo configuration.py con la URL activa.
3. Instala las dependencias ejecutando:
   pip install requests pytest
4. Ejecuta la suite de pruebas con PyTest corriendo el siguiente comando en la terminal:
   pytest create_kit_name_kit_test.py