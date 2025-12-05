print("=== CALCULADORA SIMPLES ===")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nOperações disponíveis:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = input("\nEscolha a operação: ")

if op == "1":
    resultado = num1 + num2
elif op == "2":
    resultado = num1 - num2
elif op == "3":
    resultado = num1 * num2
elif op == "4":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero."
else:
    resultado = "Operação inválida."

print("\nResultado:", resultado)
