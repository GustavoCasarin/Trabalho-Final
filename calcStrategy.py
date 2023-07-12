# Classe Strategy
class Estrategia:
    def realizar_operacao(self, num1, num2):
        pass

# Implementações concretas das estratégias
class EstrategiaSoma(Estrategia):
    def realizar_operacao(self, num1, num2):
        return num1 + num2

class EstrategiaSubtracao(Estrategia):
    def realizar_operacao(self, num1, num2):
        return num1 - num2

class EstrategiaMultiplicacao(Estrategia):
    def realizar_operacao(self, num1, num2):
        return num1 * num2

# Classe Contexto
class Contexto:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def executar_estrategia(self, num1, num2):
        return self.estrategia.realizar_operacao(num1, num2)

# Exemplo de uso
estrategia_soma = EstrategiaSoma()
contexto = Contexto(estrategia_soma)
resultado = contexto.executar_
