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
    if (tryuser == user1 and trypass == password1) or (tryuser == user2 and trypass == password2) or (tryuser == user3 and trypass == password3):
        successful_entry = True
    else:
        print("Las credenciales son incorrectas.")
        trys -= 1
if not successful_entry:
    print("Acceso bloqueado.")
else:
    print("1. Ver perfil")
    print("2. Cambiar contraseña")
    print("3. Cerrar sesión")