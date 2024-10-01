def obtener_numero_natural():
    """Solicita al usuario un número natural y valida el ingreso."""
    while True:
        try:
            numero = int(input("Ingresa un número natural: "))
            if numero <= 0:
                raise ValueError("El número debe ser mayor a 0.")
            return numero
        except ValueError as e:
            print(f"Entrada no válida: {e}. Intenta de nuevo.")

def calcular_divisores(numero):
    """Calcula y retorna los divisores de un número natural."""
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores

def main():
    numero = obtener_numero_natural()
    divisores = calcular_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")

if __name__ == "__main__":
    main()
