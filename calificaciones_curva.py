students = []
for i in range(5):
    print(f"Estudiante #{i+1}")
    name = input("Nombre: ")
    notes = []
    for h in range(3):
        note = float(input(f"Nota {h+1}: "))
        notes.append(note)
    students.append({"nombre": name, "notas": notes})
curve = True
for student in students:
    average = sum(student["notas"]) / 3
    if average >= 70:
        curve = False
        break
if curve:
    print("Se aplicara una curva de 5 puntos más a todas las notas")
    for student in students:
        for i in range(3):
            student["notas"][i] = min(student["notas"][i] + 5, 100)
print("\nResultados finales:")
for student in students:
    name = student["nombre"]
    notes = student["notas"]
    average = sum(notes) / 3
    print(f"Estudiante: {name}")
    print(f"Notas: {notes[0]}, {notes[1]}, {notes[2]}")
    print(f"Promedio: {average}")