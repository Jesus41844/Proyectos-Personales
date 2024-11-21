hora = int(input("Dime la hora en formato militar y te la dire en formato 12hr: "))

while hora > 0 and hora <= 24:
    newHora = hora - 12
    if hora > 12 and hora < 24:
        print("La hora es {0} p.m.".format(newHora))
    elif hora == 12:
        print("La hora es {0} p.m.".format(hora))
    elif hora == 24:
        print("La hora es {0} a.m.".format(hora))
    else :
        print("La hora es {0} a.m.".format(hora))
    
    hora = -1