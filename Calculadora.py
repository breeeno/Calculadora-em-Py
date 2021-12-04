
class Calculadora:
    def __init__(self):
        self.opcoes()

    def opcoes(self):
        print("(1) soma \n"
              "(2) subtração \n"
              "(3) multiplicação \n"
              "(4) divisão \n")
        operacao = int(input("Qual operação deve ser realizada? "))
        operacoes = [1,2,3,4]
        while not operacao in operacoes:
            print("Insira um valor válido.")
            operacao = int(input("Qual operação deve ser realizada? "))

        if operacao == 1:
            primeiro_valor = int(input("Insira o primeiro valor: "))
            segundo_valor = int(input("Insira o segundo valor : "))

            print(self.soma(primeiro_valor, segundo_valor))

        if operacao == 2:
            primeiro_valor = int(input(" Insira o primeiro valor: "))
            segundo_valor =  int(input("Insira o segundo valor : "))

            print(self.subtracao(primeiro_valor, segundo_valor))

        if operacao == 3:
            primeiro_valor = int(input(' Insira o primeiro valor: '))
            segundo_valor = int(input("Insira o segundo valor : "))

            print((self.multiplicacao(primeiro_valor, segundo_valor)))

        if operacao == 4:
            primeiro_valor = int(input(' Insira o primeiro valor: '))
            segundo_valor = int(input("Insira o segundo valor : "))

            print((self.divisao(primeiro_valor, segundo_valor)))

    def soma(self, valor1, valor2):
        self.resultado = valor1 + valor2
        return f'Resultado = {self.resultado} '

    def subtracao(self, valor1, valor2):
        self.resultado = valor1 - valor2
        return f'Resultado = {self.resultado}'

    def multiplicacao(self, valor1, valor2):
        self.resultado = valor1 * valor2
        return f'Resultado = {self.resultado}'

    def divisao(self, valor1, valor2):
        self.resultado = valor1 / valor2
        return f'Resultado = {self.resultado}'


if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.opcoes()
