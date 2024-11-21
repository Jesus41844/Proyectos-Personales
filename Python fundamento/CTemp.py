nombre = input("Dime tu nombre: ")
newName = nombre.capitalize()

TCelsius = float(input("Hola {0} dime la temperatura en Celsius para convertirla a grados Kelvin y Fahrenheit: ".format(nombre)))
cKelvin = TCelsius + 273.15
cfahr = (TCelsius * 9/5) + 32

message = "{0} los grados en Kelvin son: {1}, y los grados en Fahrenheit son: {2}".format(nombre, cKelvin, cfahr)
print(message)