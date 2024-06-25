notas_finales = []

while True:
    print("\n*** MENU DE OPCIONES ***")
    print("1. Cargar Notas de Alumnos.")
    print("2. Mostrar Notas de Alumnos.")
    print("3. Agregar Notas de un Alumno.")
    print("4. Visualizar el Promedio.")
    print("5. Ver la Menor Nota.")
    print("6. Ver Cantidad de Notas Mayor o igual a 7.")
    print("7. Eliminar al Primer Alumno Cargado.")
    print("8. Sumar un punto a los alumnos con nota 6.")
    print("0. Salir.")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        cargar_notas(notas_finales)
    elif opcion == 2:
        mostrar_notas(notas_finales)
    elif opcion == 3:
        agregar_nota(notas_finales)
    elif opcion == 4:
        visualizar_promedio(notas_finales)
    elif opcion == 5:
        ver_menor_nota(notas_finales)
    elif opcion == 6:
        ver_cantidad_notas_mayores_o_igual_7(notas_finales)
    elif opcion == 7:
        eliminar_primer_alumno(notas_finales)
    elif opcion == 8:
        sumar_punto_a_notas_seis(notas_finales)
    elif opcion == 0:
        print("Fin del Programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

