day = int(input("Ingrese el día: "))
month = int(input("Ingrese el año: "))
year = int(input("Ingrese el año: "))
valid_date = True
if month < 1 or month > 12:
    valid_date = False
if valid_date:
    if month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            valid_date = False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day < 1 or day > 29:
                valid_date = False
        else:
            if day < 1 or day > 28:
                valid_date = False
    else:
        if day < 1 or day > 31:
            valid_date = False
if valid_date:
    if month < 3:
        month += 12
        year -= 1
    century = year // 100
    year_on_century = year % 100
    zeller = (day + ((13 * (month + 1)) // 5 + year_on_century + (year_on_century // 4) + (century // 4) + 5 * century) % 7
