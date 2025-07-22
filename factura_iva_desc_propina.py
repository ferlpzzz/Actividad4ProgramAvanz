prices = []
print("Ingrese los precios de los productos, si desea terminar ingrese 0")
while True:
    price = input("Precio del producto: ")
    if price == "0":
        break
    prices.append(float(price))
subtotal = sum(prices)
percent_tip = 0
if input("¿Desea dejar propina? (sí/no): ") in ['sí', 'si']:
    percent_tip = float(input("¿Qué porcentaje de propina?: "))
percent_disc = 0
if input("¿Tiene tarjeta de cliente frecuente? (sí/no): ") in ['sí', 'si']:
    percent_disc = 10
tip = subtotal * (percent_tip/100)
discount = subtotal * (percent_disc/100)
subtotal_w_disc = subtotal - discount
iva = subtotal_w_disc * 0.12
total = subtotal_w_disc + iva + tip
print(f"Subtotal: Q{subtotal}")
if discount > 0:
    print(f"Descuento: Q-{discount}")
print(f"IVA: Q{iva}")
if tip > 0:
    print(f"Propina ({percent_tip}%): Q{tip}")
print(f"TOTAL: Q{total}")