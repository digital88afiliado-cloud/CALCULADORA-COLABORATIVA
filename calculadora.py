# Funções que serão implementadas pela equipe
def soma(a, b):
# TODO: Pessoa 2 deve implementar esta função
    return a + b    
pass
def subtracao(a, b):
# TODO: Pessoa 3 deve implementar esta função
pass
def multiplicacao(a, b):
# TODO: Pessoa 4 deve implementar esta função
pass
def divisao(a, b):
# TODO: Pessoa 5 deve implementar esta função
  if b == 0:
    return "Erro: divisão por zero não é permitida."
  return a / b
# -- Fim da área de implementação das funções --
# Menu principal da calculadora (Responsabilidade do Líder)
def main():
print("Bem-vindo à Calculadora Colaborativa!")
while True:
print("\nSelecione a operação:")
print("1: Soma")
print("2: Subtração")
print("3: Multiplicação")
print("4: Divisão")
print("0: Sair")
escolha = input("Digite o número da sua escolha: ")
if escolha == '0':
print("Até a próxima!")
break
if escolha not in ['1', '2', '3', '4']:
print("Opção inválida, tente novamente.")
continue
try:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
except ValueError:
print("Entrada inválida. Por favor, digite apenas números.")
continue
if escolha == '1':
resultado = soma(num1, num2)
print(f"O resultado de {num1} + {num2} é: {resultado}")
elif escolha == '2':
resultado = subtracao(num1, num2)
print(f"O resultado de {num1} - {num2} é: {resultado}")
elif escolha == '3':
resultado = multiplicacao(num1, num2)
print(f"O resultado de {num1} * {num2} é: {resultado}")
elif escolha == '4':
resultado = divisao(num1, num2)
print(f"O resultado de {num1} / {num2} é: {resultado}")
# Executa o programa
if __name_