def find_divisors(number):
    divisors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)

    divisors.sort()
    return divisors

def get_positive_integer_input():
    while True:
        try:
            number = int(input("Ingrese un número entero positivo: "))
            if number <= 0:
                print("El número debe ser mayor a 0.")
            else:
                return number
        except ValueError:
            print("No se permiten caracteres especiales ni letras. Por favor ingresa un numero entero positivo: ")

if __name__ == "__main__":
    number = get_positive_integer_input()
    result = find_divisors(number)
    print(f"Los divisores de {number} son: {result}")
