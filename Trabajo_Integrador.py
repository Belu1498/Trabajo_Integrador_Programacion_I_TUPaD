from quicksort_busqueda_binaria import quicksort, busqueda_binaria
from data_cuerpo_medico import doctores_por_especialidad, lista_especialistas, especialistas_codigos

# Lista ordenada
lista_especialistas_ordenada = quicksort(lista_especialistas)

numeros = [especialistas_codigos[x] for x in lista_especialistas_ordenada]

repetir = True

# Aplicacion de quicksort y busqueda binaria
while repetir:

    nombre = (input("¡Bienvenido/a! Por favor ingrese su nombre y apellido: "))
    mail = (input("Por favor ingrese su mail: "))
    print("------------------------------")

    print(f"Estimado/a paciente {nombre}, a continuación se mostrarán los especialistas médicos disponibles hasta la fecha en orden descendente.")
    print("Cada numero quivale a la especializacion disponible en nuestro sistema. Por ejemplo, el número **4** equivaldrá a la cuarta especialidad en la lista de especialistas médicos")
    print("Menor a 5: equivale a las especialidades con menor disponibilidad hasta el momento.")
    print()
    print("===== Disponibilidad =====")

    print(quicksort(numeros))
# traemos la lista de numeros utilizando quicksort
    print()
    print("===== Especialistas Médicos =====")
    print(quicksort(lista_especialistas_ordenada)) # traemos la lista de especialidades ya ordenada utilizando quicksort


    print()
    busqueda = input("Ingrese la especialidad que desea buscar (ej. Pediatra): ").capitalize()

    # Realizar la búsqueda
    indice = busqueda_binaria(lista_especialistas_ordenada, busqueda)

    # El usuario al escribir la profesion, se marca la posicion dentro de la lista.

    if indice != -1 and busqueda in doctores_por_especialidad:
        print(f"\nEspecialidad encontrada en la posición {indice}.")

    # Mensaje aclarando que si la posición es 5 o mayor saldra un mensaje marcando menor disponibilidad
        if indice >= 5:
            print("Atención: Esta especialidad presenta menor disponibilidad. Se recomienda consultar turnos con anticipación a clinica@medicos.com.")

        print("\nDoctores disponibles:")
        for doctor in doctores_por_especialidad[busqueda]:
            print(f"- {doctor}")
    else:
    # Si no coindice con el contenido de la lista
        print("Especialidad no encontrada.")

    print()
    print(f"Le llegara un boletin informativo una vez asignado el turno a este correo: {mail}. ¡Muchas gracias!")

    nuevo_turno = (input("¿Desea tomar otro turno? Ingrese Si o No: "))
    repetir = True if nuevo_turno.capitalize() == 'Si' else False
