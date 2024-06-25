# Examen Recuperatorio de Programación en Python

## Instrucciones de Clonación del Repositorio (5 ptos.)

1. Clona el repositorio del examen:
   ```bash
   git clone https://github.com/FabioDrizZt/UCSE-Examen-recuperatorio-programacion-en-python
   ```

2. Crea un repositorio privado en GitHub.

3. Añade como colaborador al usuario `ing.fabio.arg@gmail.com`.

4. Sube tus soluciones a tu repositorio privado. 

# Gestor de Notas de Alumnos

Diseñar un programa en Python para procesar las notas finales de los alumnos de una materia. Para cada alumno de la materia se ingresan dos notas correspondientes a los dos exámenes tomados durante el cursado de la misma, las cuales deben validarse que sean un valor entre 0 y 10 (incluyendo ambos). El programa debe permitir realizar varias operaciones mediante un menú de opciones.

## Descripción del Menú de Opciones

1. **Cargar Notas de Alumnos** (20 ptos.)
    - Ingresar la cantidad de alumnos.
    - Ingresar las notas de los dos exámenes para cada alumno.
    - Validar que cada nota se encuentre entre 0 y 10 (incluyendo ambos).
2. **Mostrar Notas de Alumnos** (10 ptos.)
    - Mostrar todas las notas finales de los alumnos.
3. **Agregar Notas de un Alumno** (15 ptos.)
    - Ingresar las notas de los dos exámenes para un nuevo alumno.
    - Validar que cada nota se encuentre entre 0 y 10 (incluyendo ambos).
4. **Visualizar el Promedio** (10 ptos.)
    - Calcular y mostrar el promedio de las notas obtenidas por los alumnos.
5. **Ver la Menor Nota** (10 ptos.)
    - Mostrar la menor nota final calculada.
6. **Ver Cantidad de Notas Mayor o Igual a 7** (15 ptos.)
    - Mostrar cuántos alumnos obtuvieron una nota mayor o igual a 7.
7. **Eliminar al Primer Alumno Cargado** (10 ptos.)
    - Eliminar la primera nota del vector.
8. **Sumar un Punto a los Alumnos con Nota 6** (15 ptos.)
    - Reemplazar todas las notas con valor 6 con el valor 7.
0. **Salir**
    - Terminar el programa.

## Ejemplo de Entradas del Usuario y Comportamiento del Programa

```plaintext
Seleccione una opción: 1

   Ingrese cantidad de alumnos: 5
   Ingrese las notas de los dos exámenes del alumno N°1: 10 9
   Ingrese las notas de los dos exámenes del alumno N°2: 7 8
   Ingrese las notas de los dos exámenes del alumno N°3: 2 10
   Ingrese las notas de los dos exámenes del alumno N°4: 9 8
   Ingrese las notas de los dos exámenes del alumno N°5: 4 8

Seleccione una opción: 2

   Alumno N°1: 9.5
   Alumno N°2: 7.5
   Alumno N°3: 6
   Alumno N°4: 8.5
   Alumno N°5: 6

Seleccione una opción: 3

   Ingrese las notas de los dos exámenes del alumno N°6: 5 4

Seleccione una opción: 2

   Alumno N°1: 9.5
   Alumno N°2: 7.5
   Alumno N°3: 6
   Alumno N°4: 8.5
   Alumno N°5: 6
   Alumno N°6: 4.5

Seleccione una opción: 4

   El promedio de notas obtenidas es: 7

Seleccione una opción: 5

   La menor nota obtenida fue: 4.5

Seleccione una opción: 6

   La cantidad de alumnos que obtuvieron notas elevadas es: 3

Seleccione una opción: 7

   Primer alumno eliminado correctamente.

Seleccione una opción: 2

   Alumno N°1: 7.5
   Alumno N°2: 6
   Alumno N°3: 8.5
   Alumno N°4: 6
   Alumno N°5: 4.5

Seleccione una opción: 8

Punto agregado correctamente.

Seleccione una opción: 2

   Alumno N°1: 7.5
   Alumno N°2: 7
   Alumno N°3: 8.5
   Alumno N°4: 7
   Alumno N°5: 4.5

Seleccione una opción: 0

   Fin del Programa.
```
