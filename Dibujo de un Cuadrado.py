class Cuadrado:
    def __init__(self, lado: int):
        self.lado = lado

    def dibujar(self):
        for _ in range(self.lado):
            print('*' * self.lado)


if __name__ == "__main__":
    # Ejemplo de uso
    lado = int(input("Ingrese el tamaño del lado del cuadrado: "))

    cuadrado = Cuadrado(lado)
    cuadrado.dibujar()
