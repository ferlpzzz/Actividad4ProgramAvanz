earnings = float(input("Ingrese su ingreso anual: "))
dependent = int(input("Ingrese su número de dependientes: "))
if earnings < 40000 and dependent > 2:
    print("No pagas impuestos")
else:
    deduction = dependent * 1000
    earnings_tax = earnings - deduction
    if earnings_tax < 0:
        earnings_tax = 0
    if earnings_tax <= 30000:
        taxes = earnings_tax * 0.05
    elif earnings_tax <= 60000:
        taxes = 30000 * 0.05 + (earnings_tax - 30000) * 0.10
    elif earnings_tax <= 100000:
        taxes = 30000 * 0.05 + 30000 * 0.10 + (earnings_tax - 60000) * 0.15
    else:
        taxes = 30000 * 0.05 + 30000 * 0.10 + 40000 * 0.15 + (earnings_tax - 100000) * 0.20
    print(f"El ingreso anual es: Q{earnings}")
    print(f"De dependientes: {dependent} y sus deducciones: Q{deduction}")
    print(f"El ingreso sin impuestos es: Q{earnings_tax}")
    print(f"EL impuesto a pagar: Q{taxes}")