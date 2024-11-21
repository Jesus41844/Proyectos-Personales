def registrar_ventas(producto,precio,cantidad,descuento=0,impuesto=0, **kwargs):
    totalBruto = cantidad * precio
    mDescuento = totalBruto * (descuento / 100)
    totalCDescuento = totalBruto - mDescuento
    mImpuesto = totalCDescuento * (impuesto / 100)
    totalNeto = totalCDescuento + mImpuesto

    mensaje = f"Producto: {producto}\n"
    mensaje += f"Precio por unidad: {precio}\n"
    mensaje += f"Cantidad: {cantidad}\n"
    mensaje += f"Descuento: {descuento}\n"
    mensaje += f"Impuesto: {impuesto}\n"
    mensaje += f"Total a pagar: {totalNeto}\n"

    for clave, valor in kwargs.items():
        mensaje += f"{clave.capitalize()}: {valor}\n"
    
    print(mensaje)

def CalMediaVentas(*ventas):
    if not ventas:
        return 0
    return sum(ventas) / len(ventas)

registrar_ventas("Laptop", 1000, 2, descuento=10, impuesto=18, cliente="Juan Pérez", fecha="2024-11-20")
media = CalMediaVentas(100, 200, 300, 1020)
print(f"La cantidad media de las ventas es de: {media}")