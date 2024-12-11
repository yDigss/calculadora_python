while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Por favor, insira números válidos.")
        continue

    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero!"
    else:
        resultado = "Operação inválida!"

    print(f"O resultado é: {resultado}")

    continuar = input("Deseja fazer outra operação? (s/n): ")
    if continuar.lower() != "s":
        print("Até logo!")
        break
