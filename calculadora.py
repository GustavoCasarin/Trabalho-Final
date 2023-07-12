class Calculadora:
    def somar(self, num1, num2):
        return num1 + num2

    def subtrair(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

# Exemplo de uso
calculadora = Calculadora()

resultado = calculadora.somar(5, 3)
print("Resultado da operação de adição:", resultado)

resultado = calculadora.subtrair(5, 3)
print("Resultado da operação de subtração:", resultado)

resultado = calculadora.multiplicar(5, 3)
print("Resultado da operação de multiplicação:", resultado)

