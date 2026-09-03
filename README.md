# Sprint 8: Proyecto Urban Grocers - TripleTen

Este proyecto implementa funciones y pruebas automatizadas para validar la creación de usuarios y kits de producto mediante solicitudes a la API de **Urban Grocers**.  
El objetivo es comprobar el comportamiento de la API en distintos escenarios, evaluando tanto casos positivos como negativos:

- **Casos positivos**: cuando los datos enviados cumplen con el formato y tipo esperado.  
- **Casos negativos**: cuando la información ingresada no cumple con las reglas definidas (por ejemplo, tipos de datos incorrectos o valores fuera de rango).

De esta forma, se asegura que la API maneje correctamente las solicitudes válidas y rechace aquellas que contienen errores, garantizando su correcto funcionamiento.


---

## 📂 Estructura del proyecto


- `configuration.py` → Configuración de URLs y rutas
- `data.py` → Diccionarios de datos (headers, body de usuario, body de kit)
- `sender_stand_request.py` → Funciones para enviar solicitudes POST
- `create_kit_name_kit_test.py` → Pruebas automatizadas con Pytest

## ⚙️ Requisitos

- Python 3.9 o superior
- Librerías necesarias:
  - `requests`
  - `pytest`

Instalación de dependencias:

```python
pip install requests pytest
```
## 📖 Documentación
La documentación de la API se basa en **apiDoc** y en los endpoints proporcionados por Urban Grocers.

## 🛠️ Tecnologías utilizadas
- **Python 3.9+**
- **Requests** para enviar solicitudes HTTP
- **Pytest** para pruebas automatizadas
- **apiDoc** como referencia de documentación

## ▶️ Ejecutar scripts manuales
Si quieres probar directamente las solicitudes y ver los resultados en consola:

```python
python sender_stand_request.py
```

Esto mostrará el código de respuesta y el **JSON** recibido.

## 🧪 Ejecutar pruebas con Pytest
Las pruebas están en el archivo `create_kit_name_kit_test.py`.

**Ejecuta todas las pruebas:**

```python
pytest -v
```

**Ejecuta solo el archivo de kits:**

```python
pytest create_kit_name_kit_test.py -v
```
> **🔎 Nota:** -v muestra más detalle de cada prueba.

## ✅ Casos de prueba incluidos
El proyecto consta de los siguientes casos de prueba:

* Nombre con 1 carácter → 201 
* Nombre con 511 caracteres → 201
* Nombre vacío → 400
* Nombre con 512 caracteres → 400
* Nombre con caracteres especiales → 201
* Nombre con espacios → 201
* Nombre con números → 201
* Sin parámetro name → 400
* Nombre con tipo numérico → 400

## 📌 Notas importantes
- Siempre usa `copy()` al modificar diccionarios de `data.py` para evitar errores.

- Si la solicitud falla, revisa las rutas en `configuration.py` y asegúrate de que no haya `//` extra en las URLs.

- Los tokens de usuario se generan en cada prueba para garantizar independencia.

> Con este **README** cualquier persona podrá instalar dependencias, correr tus scripts y validar las pruebas fácilmente.