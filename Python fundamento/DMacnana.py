def defDia(dia, mes, acno):
    if acno >= 2000 and acno <= 2024:
        if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 9 or mes == 12):
            if (dia >=1 and dia < 31):
                dia = dia + 1
            elif (dia == 31 and mes != 12):
                dia = dia + 1
                mes = mes + 1
            elif (dia == 31 and mes == 12):
                dia = dia + 1
                mes = 1
                acno = acno + 1
        elif (mes == 4 or mes == 6 or mes == 10 or mes == 11):
            if (dia >=1 and dia < 30):
                dia = dia + 1
            elif (dia == 30):
                dia = 1
                mes = mes + 1
        elif (mes == 2):
            if (dia < 28):
                dia = dia + 1
            elif (dia == 28):
                dia = 1
                mes = mes + 1
        else:
            print("Datos no validos")
    return dia, mes, acno

print("Dime que dia es hoy y te dire el dia siguiente: ")
dia = int(input("Dime el dia actual: "))
mes = int(input("Dime el mes actual: "))
acno = int(input("Dime el año actual: "))

dia, mes, acno = defDia(dia, mes, acno)

print("Mañana es: {0}/{1}/{2}".format(dia, mes, acno))