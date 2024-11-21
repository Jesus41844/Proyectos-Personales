import io

class Clientes:
    def __init__(self, nombre, pedido, pizzas, bebida):
        self.nombre = nombre
        self.pedido = pedido
        self.pizzas = pizzas
        self.bebida = bebida

def Menu():
    with io.open('C:\\Users\\j3sus\\OneDrive\\Documents\\Programacion\\Proyectos Personales\\Python fundamento\\ProyectoHPAPython\\Bienvenida.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

    for linea in data:
        print(linea.strip())


def Pedidos(Cliente):
    with io.open('C:\\Users\\j3sus\\OneDrive\\Documents\\Programacion\\Proyectos Personales\\Python fundamento\\ProyectoHPAPython\\Pedidos.txt', 'a', encoding='utf-8') as file:
        file.write(f"Cliente = {Cliente.nombre}\n")
        file.write(f"Pedido #{Cliente.pedido}\n")
        file.write("Pizzas = " + ", ".join(Cliente.pizzas) + "\n")
        file.write(f"Bebida = {Cliente.bebida}\n")
        file.write("\n")

nombre = input("Bienvenido a McDeallo, cual es su nombre: ")
seguir = True
Contador = 1
while seguir:
    Menu()
    decision = input("Quiere una pizza o una bebida? (P/B): ")
    if decision == "P":
        pizzas = []
        for i in range(4):
            pizza = input(f"Dime el sabor {i+1} de la pizza: ")
            pizzas.append(pizza)
        cliente1 = Clientes(nombre,Contador,pizzas,"No pedido")
        Pedidos(cliente1)
    elif decision == "B":
        bebida = input("Dime la bebida que desea: ")
        cliente1 = Clientes(nombre,Contador,["No pedido"],bebida)
        Pedidos(cliente1)
    else:
        print("Opción no válida. Por favor, elija 'P' para pizza o 'B' para bebida.")
    SoN = input("Desea pedir algo mas? (S/N): ")
    if SoN != "S":
        seguir = False
    Contador += 1

print("Pronto se le entregara su pedido, provecho")