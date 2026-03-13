def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100

    print(precio_base * 1.21 - precio_base)

    print(precio_base * 1.21)

    subtotal = (precio_base * 1.21)

    print(subtotal * 1.10 - subtotal)

    print((precio_base * 1.21) + subtotal * 1.10 - subtotal)
#price()