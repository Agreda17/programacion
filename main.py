class PalindromoChecker:
    def __init__(self, palabra):
        self.palabra = palabra.lower().replace(" ", "")

    def es_palindromo(self):
        return self.palabra == self.palabra[::-1]

def obtener_palabra_valida():
    while True:
        palabra = input("Ingrese una palabra: ")
        palabra = palabra.strip()
        if not palabra:
            print(" No Debes ingresar nuemros.")
        elif not palabra.isalpha():
            print(" La palabra debe contener solo letras.")
        else:
            return palabra

def main():
    palabra = obtener_palabra_valida()
    checker = PalindromoChecker(palabra)

    if checker.es_palindromo():
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")

if __name__ == "__main__":
    main()
