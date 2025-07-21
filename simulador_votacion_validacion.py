name = input("Ingrese su nombre completo: ")
dpi = input("Ingrese su numero de DPI: ")
department = input("Ingrese su departamento: ")
year_birth = int(input("Ingrese su año de nacimiento: "))
if len(name) < 5:
    print("El nombre no puede tener menos de 5 letras.")
else:
    if len(dpi) != 13 or not dpi.isdigit():
        print("El DPI tiene que tener al menos 13 digitos y ser un numero.")
    else:
        age = 2025 - year_birth
        can_vote = False
        if department in ["Petén", "Alta Verapaz"]:
            if age >= 17:
                can_vote = True
        else:
            if age >= 18:
                can_vote = True
        if can_vote:
            print(f"Bienvenido/a {name}, su centro de votación está en {department}")
        else:
            print("Usted no cumple los requisitos para poder votar")
