weight = float(input("Peso del paquete en kg: "))
distance = float(input("Distancia en km: "))
urgent = input("¿Es urgente? (sí/no): ").lower() in ["sí", "si"]
size = input("Tamaño del paquete (pequeño/mediano/grande): ").lower()
base_cost = (weight * 15) + (distance * 10)
urgent_cost = 50 if urgent else 0
size_cost = 30 if size == 'grande' else 0
discount = 20 if (not urgent and weight < 5) else 0
total = base_cost + urgent_cost + size_cost - discount
print(f"Costo base: Q{base_cost}")
if urgent_cost > 0:
    print(f"Recargo por urgencia: +Q{urgent_cost}")
if size_cost > 0:
    print(f"Recargo por tamaño grande: +Q{size_cost}")
if discount > 0:
    print(f"Descuento: -Q{discount}")
print(f"TOTAL A PAGAR: Q{total}")
