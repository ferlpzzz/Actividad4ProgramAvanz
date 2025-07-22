origin = input("Coordenada origen (norte/sur/este/oeste): ").lower()
destination= input("Coordenada destino (norte/sur/este/oeste): ").lower()
if origin == destination:
    print(f"Recto hacia el {origin}")
else:
    if origin == "norte":
        if destination == "este":
            print("Dirección: noreste")
        elif destination == "oeste":
            print("Dirección: noroeste")
        elif destination == "sur":
            print("Dirección: recto hacia el sur")

    elif origin == "sur":
        if destination == "este":
            print("Dirección: sureste")
        elif destination == "oeste":
            print("Dirección: suroeste")
        elif destination == "norte":
            print("Dirección: recto hacia el norte")

    elif origin == "este":
        if destination == "norte":
            print("Dirección: noreste")
        elif destination == "sur":
            print("Dirección: sureste")
        elif destination == "oeste":
            print("Dirección: recto hacia el oeste")

    elif origin == "oeste":
        if destination == "norte":
            print("Dirección: noroeste")
        elif destination == "sur":
            print("Dirección: suroeste")
        elif destination == "este":
            print("Dirección: recto hacia el este")

    else:
        print("Coordenadas no válidas")