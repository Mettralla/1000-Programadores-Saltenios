# Ejercicio 4: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada
# asignatura, y después mostrar por pantalla con el mensaje: "En la 'asignatura' saco 'nota'" donde
# 'asignatura' es la asignatura correspondiente y 'nota' es la nota correspondiente a la asignatura.

asignaturas = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lengua']
notas = []
for asignatura in asignaturas:
    nota = input(f'Ingresar nota de {asignatura}: ')
    notas.append(nota)
for i in range(len(asignaturas)):
    print(f'En {asignaturas[i]} ha sacado: {notas[i]}')
