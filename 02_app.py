def conversion_moneda():
    # Solicitar al usuario el monto en soles
    monto_pen = float(input("Ingrese el monto en soles (PEN): "))
    
    # Preguntar la tasa de cambio actual
    tasa_cambio = float(input("Ingrese la tasa de cambio actual (1 USD = ? PEN): "))
    
    # Calcular el equivalente en dólares
    equivalente_usd = monto_pen / tasa_cambio
    
    # Mostrar el resultado con dos decimales
    print("\n--- Conversión en Global Change ---")
    print(f"Monto en soles: S/ {monto_pen:.2f}")
    print(f"Tasa de cambio: 1 USD = S/ {tasa_cambio:.2f}")
    print(f"Equivalente en dólares: $ {equivalente_usd:.2f}")

# Ejecutar la función
conversion_moneda()