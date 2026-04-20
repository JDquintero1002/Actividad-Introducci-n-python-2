#  Sistema de Estudiantes - SENA

Aplicación de consola desarrollada en Python que permite gestionar información básica de estudiantes, sedes y materias. Desarrollada como actividad integradora del módulo de introducción a Python con el Ing. Andrés.

---

##  Descripción

El sistema permite registrar estudiantes, consultar el listado completo, ver las sedes disponibles de la institución y consultar las materias ofrecidas. Todo desde un menú interactivo en consola.

---

##  Instrucciones de ejecución

1. Asegúrate de tener Python instalado (versión 3.x)
2. Clona el repositorio:
   ```
   git clone https://github.com/JDquintero1002/Actividad-Introducci-n-python-2.git
   ```
3. Navega a la carpeta del proyecto:
   ```
   cd Actividad-Introducci-n-python-2
   ```
4. Ejecuta el archivo principal:
   ```
   python sistemaEstudiantes.py
   ```

---

## 🗂️ Estructuras de datos utilizadas

### 📦 Diccionario
Cada estudiante se representa como un diccionario con los campos: `Nombre`, `Edad`, `ID`, `fecha_nacimiento`, `direccion`, `numero_de_contacto`, `Faltas` y `es_estudiante`.

```python
estudiante = {
    "Nombre": "Juan David",
    "Edad": "25",
    "ID": "1321465431541",
    ...
    "es_estudiante": True
}
```

###  Lista
Se utiliza una lista para almacenar todos los estudiantes registrados durante la ejecución del programa.

```python
estudiantes = []
estudiantes.append(estudiante)
```

###  Tupla
Las sedes de la institución se almacenan en una tupla porque son datos fijos que no cambian.

```python
sedes = ("Norte", "Centro")
```

###  Set
Las materias se almacenan en un set para garantizar que no haya duplicados. Por su naturaleza, los sets no garantizan un orden fijo.

```python
materias = {"Matemáticas", "Español", "Historia", "Filosofia", "Informatica"}
```

###  Ciclo for
Se utiliza para recorrer e imprimir la lista de estudiantes, las sedes y las materias.

```python
for listadoEstudiantes in estudiantes:
    print(listadoEstudiantes)
```

###  Ciclo while
Se utiliza para mantener el menú activo hasta que el usuario elija la opción de salir.

```python
while opciones != "5":
    # mostrar menú y procesar opciones
```

---

##  Capturas

Las capturas del programa en funcionamiento se encuentran en la carpeta `/capturas` del repositorio.

---

## Autor

Juan David Quintero  
SENA - Análisis y Desarrollo de Software
