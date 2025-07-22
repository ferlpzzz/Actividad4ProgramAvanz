print("Primera fecha: ")
d1 = int(input("Día: "))
m1 = int(input("Mes: "))
y1 = int(input("Año: "))
print("Segunda fecha:")
d2 = int(input("Día: "))
m2 = int(input("Mes: "))
y2 = int(input("Año: "))
valid = True
if m1 < 1 or m1 > 12 or m2 < 1 or m2 > 12:
    valid = False
if d1 < 1 or d1 > 31 or d2 < 1 or d2 > 31:
    valid = False
if m1 in [4, 6, 9, 11] and d1 > 30:
    valid = False
if m2 in [4, 6, 9, 11] and d2 > 30:
    valid = False
if m1 == 2 and d1 > 28:
    valid = False
if m2 == 2 and d2 > 28:
    valid = False
if not valid:
    print("Fechas inválidas")
else:
    if y1 > y2:
        print("La primera fecha es mayor")
    elif y2 > y1:
        print("La segunda fecha es mayor")
    else:
        if m1 > m2:
            print("La primera fecha es mayor")
        elif m2 > m1:
            print("La segunda fecha es mayor")
        else:
            if d1 > d2:
                print("La primera fecha es mayor")
            elif d2 > d1:
                print("La segunda fecha es mayor")
            else:
                print("Las fechas son iguales")
    if y1 == y2 and m1 == m2:
        print("Están en el mismo mes y año")
    else:
        print("No están en el mismo mes y año")
    days = abs((y1 - y2) * 365 + (m1 - m2) * 30 + (d1 - d2))
    print(f"Días de diferencia: {days}")