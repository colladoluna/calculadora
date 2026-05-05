def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  ⚠ Por favor, introduce un número válido.\n")

def mostrar_menu():
    print("\n╔══════════════════════════╗")
    print("║       CALCULADORA        ║")
    print("╠══════════════════════════╣")
    print("║  1. Suma                 ║")
    print("║  2. Resta                ║")
    print("║  3. Multiplicación       ║")
    print("║  4. División             ║")
    print("║  0. Salir                ║")
    print("╚══════════════════════════╝")

def main():
    operaciones = {
        "1": ("Suma",           sumar),
        "2": ("Resta",          restar),
        "3": ("Multiplicación", multiplicar),
        "4": ("División",       dividir),
    }

    print("\nBienvenido a la calculadora")

    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ").strip()

        if opcion == "0":
            print("\nHasta luego 👋\n")
            break
        elif opcion in operaciones:
            nombre, funcion = operaciones[opcion]
            print(f"\n── {nombre} ──")
            a = obtener_numero("  Primer número:  ")
            b = obtener_numero("  Segundo número: ")
            resultado = funcion(a, b)
            print(f"\n  Resultado: {a} {'+-*/'['1234'.index(opcion)]} {b} = {resultado}")
        else:
            print("\n  ⚠ Opción no válida. Elige entre 0 y 4.")

if __name__ == "__main__":
    main()