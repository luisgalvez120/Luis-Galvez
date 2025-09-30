def calcular_tarifa():
    # Solicitar la edad del pasajero
    try:
        edad = int(input("Ingrese la edad del pasajero: "))
    except ValueError:
        print("Por favor, ingrese una edad válida.")
        return
    
    # Determinar la tarifa usando if-elif-else
    if edad < 12:
        tarifa = 3.00
        mensaje = "Tarifa infantil"
    elif 12 <= edad <= 59:
        tarifa = 5.00
        mensaje = "Tarifa regular"
    else:
        tarifa = 2.00
        mensaje = "Tarifa especial"
    
    # Mostrar el precio final con un mensaje claro y formateado
    print(f"{mensaje}: S/ {tarifa:.2f}")

# Ejecutar la función
calcular_tarifa()