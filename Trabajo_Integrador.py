def quicksort(lista_especialistas):
    if len(lista_especialistas) <= 1: # Si la lista tiene menos de 1 elemento, esta ordenada.
        return lista_especialistas
    pivote = lista_especialistas[0] # Elegimos la primer palabra como pivote (usado como refencia para dividir la lista)

# organiza los elementos menores a un lado y los mayores al otro.

    menor = [x for x in lista_especialistas[1:] if x <= pivote]  # primero los menores
    mayor = [x for x in lista_especialistas[1:] if x > pivote]   # luego los mayores
    return quicksort(menor) + [pivote] + quicksort(mayor) # retornamos la lista con los elementos y el pivote

# Busqueda binaria

def busqueda_binaria(lista, objetivo):

    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Lista


lista_especialistas = ["Neurologo", "Pediatra", "Traumatologo", "Cardiologo", "Clinico", "Dermatologa", "Kinesiologo", "Obstetra", "Urologo", "Cirujano"]

# Lista ordenada

lista_especialistas_ordenada = quicksort(lista_especialistas)

# Nombres de doctores con su especialidad utilizando diccionario

doctores_por_especialidad = {
    'Cardiologo': ['Dr. Hernán Cabrera', 'Dr. Iván Romero', 'Dr. Marcelo Vargas'],
    'Cirujano': ['Dr. Leonardo Ibáñez', 'Dr. Gustavo Soto', 'Dr. Fabián Medina'],
    'Clinico': ['Dr. Ernesto Aguilar', 'Dra. Valeria Peña', 'Dr. Rodrigo Fernández'],
    'Dermatologa': ['Dra. Carolina Fuentes', 'Dra. Patricia Núñez', 'Dra. Daniela Rojas'],
    'Kinesiologo': ['Lic. Nicolás Salas', 'Lic. Andrés Molina', 'Lic. Franco Herrera'],
    'Neurologo': ['Dr. Ricardo Paredes', 'Dr. Sergio Quiroga', 'Dr. Pablo Leiva'],
    'Obstetra': ['Dra. Ana Martínez', 'Dra. Florencia Díaz', 'Dra. Elena Suárez'],
    'Pediatra': ['Dra. Laura Ramírez', 'Dra. Julieta Castro', 'Dra. Cecilia Gómez'],
    'Traumatologo': ['Dr. Diego Sánchez', 'Dr. Tomás Vera', 'Dr. Martín López'],
    'Urologo': ['Dr. Carlos Méndez', 'Dr. Javier Ruiz', 'Dr. Alberto Torres']
}

# Codigos
# Se convierten las espcializades en numeros

especialistas_codigos = {
    "Neurologo": 4,
    "Pediatra": 8,
    "Traumatologo": 9,
    "Cardiologo": 10,
    "Clinico": 7,
    "Dermatologa": 5,
    "Kinesiologo": 6,
    "Obstetra": 1,
    "Urologo": 3,
    "Cirujano": 2
}


numeros = [especialistas_codigos[x] for x in lista_especialistas_ordenada]
# print(numeros) [Numeros desordenados]


# Aplicacion de quicksort y busqueda binaria

nombre = (input("¡Bienvenido/a! Por favor ingrese su nombre y apellido: "))
mail = (input("Por favor ingrese su mail: "))
print("------------------------------")

print(f"Estimado/a paciente {nombre}, a continuación se mostrarán los especialistas médicos disponibles hasta la fecha en orden descendente.")
print("Cada numero quivale a la especializacion disponible en nuestro sistema. Por ejemplo, el número **4** equivaldrá a la cuarta especialidad en la lista de especialistas médicos")
print("Menor a 5: equivale a las especialidades con menor disponibilidad hasta el momento.")
print()
print("===== Disponibilidad =====")

print(quicksort(numeros)) # traemos la lista de numeros utilizando quicksort

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
