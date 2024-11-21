name = input("Dime tu nombre: ")
newName = name.capitalize()

saludo = input("Hola, eres un nuevo cliente? (si/no): ").strip().lower() == "si"

if saludo:
    print(f"Hola {newName}, como nuevo cliente tienes un 15% de descuento disponible")
    descuento = float(0.15)
else:
    print(f"Hola {newName} como viejo cliente tienes un 10% de descuento disponible")
    descuento = float(0.10)

monto = float(input(f"Dime el monto de tu compra: "))

cDescuento = input("Cuenta con algun descuento disponible? ").strip().lower() == "si"
if cDescuento:
    monto -= monto * descuento

mFinal = print("El monto de su compra es: {0}".format(monto))