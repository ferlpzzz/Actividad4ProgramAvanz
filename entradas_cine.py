age = int(input("Ingresa tu edad: "))
day = input("Ingresa el dia de la semana: ").lower()
is_student = input("Eres estudiante? (si/no): ").lower() == "si"
movie_rating = 15
price = 50
if is_student:
    price = 35
if day == "wednesday":
    price = price / 2
if age < 13 and movie_rating > 15:
    print("Acceso denegado. Los menores de 13 años no pueden ver películas 15+.")
else:
    print(f"El precio a pagar de tus entradas es: Q{price}")