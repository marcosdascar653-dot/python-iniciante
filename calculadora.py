
while True:
    print("\n=== Calculadora ===")

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    print("""
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
0 - Sair
""")

    op = input("Escolha uma opção: ")

    if op == "0":
        print("Programa encerrado.")
        break
    elif op == "1":
        print("Resultado:", n1 + n2)
    elif op == "2":
        print("Resultado:", n1 - n2)
    elif op == "3":
        print("Resultado:", n1 * n2)
    elif op == "4":
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("Erro: divisão por zero!")
    else:
        print("Opção inválida!")
