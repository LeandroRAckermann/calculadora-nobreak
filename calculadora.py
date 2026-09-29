valor1 = float(input("Digite um valor qualquer: "))
operacao = input("Digite o símbolo da operação que deseja realizar (+, -, *, /): ")
valor2 = float(input("Digite um valor qualquer: "))

if operacao == "+":
    resultado = valor1 + valor2

elif operacao == "-":
    resultado = valor1 - valor2

elif operacao == "*":
    resultado = valor1 * valor2

elif operacao == "/":
    resultado = valor1 / valor2

else:
    resultado = "Operação inválida"

print("O resultado da operação é:", resultado)