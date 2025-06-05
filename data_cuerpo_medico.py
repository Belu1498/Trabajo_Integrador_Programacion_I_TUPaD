# Lista

lista_especialistas = ["Neurologo", "Pediatra", "Traumatologo", "Cardiologo", "Clinico", "Dermatologa", "Kinesiologo", "Obstetra", "Urologo", "Cirujano"]


# Nombres de doctores con su espcialidad utilizando diccionario

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