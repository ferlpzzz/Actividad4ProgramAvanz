user1 = "masterpro123"
password1 = "mastercontra321"
user2 = "Cosmic Kid"
password2 = "Hola12345"
user3 = "F3rlpzzz"
password3 = "chusito_2025"
trys = 3
successful_entry = False
while trys > 0 and not successful_entry:
    print(f"Te quedan: {trys} intentos")
    tryuser = input("Ingrese su usuario: ")
    trypass = input("Ingrese su contraseña: ")
    if tryuser in user1 or user2 or user3:
        successful_entry = True
