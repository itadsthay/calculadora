import math

# Função para realizar divisão com tratamento de erros
def dividir(num1, num2):
    try:
        return f'{num1}/{num2} = {num1 / num2}'
    except ZeroDivisionError:
        return 'O denominador deve ser diferente de zero.'
    except TypeError:
        return 'Insira um valor válido.'

# Exibe o menu principal
def menu_principal():
    print("Calculadora".center(65, '='))
    opcoes()
    print('=' * 65)

# Opções principais do menu
def opcoes():
    print("\t1 - Operações aritméticas")
    print("\t2 - Funções logarítmicas e potência")
    print("\t3 - Funções trigonométricas")
    print("\t4 - Outras opções")
    print("\t5 - Sair")

# Submenu de operações aritméticas
def opcoes_1():
    print("\t1 - Soma")
    print("\t2 - Subtração")
    print("\t3 - Multiplicação")
    print("\t4 - Divisão")
    print("\t5 - Voltar")

# Submenu de logaritmos e potências
def opcoes_2():
    print("\t1 - Quadrado")
    print("\t2 - Cubo")
    print("\t3 - Potência")
    print("\t4 - Log10")
    print("\t5 - Log em base personalizada")
    print("\t6 - Voltar")

# Submenu de trigonometria
def opcoes_3():
    print("\t1 - Seno")
    print("\t2 - Cosseno")
    print("\t3 - Tangente")
    print("\t4 - Voltar")

# Submenu de outras opções
def opcoes_4():
    print("\t1 - Fatorial")
    print("\t2 - Voltar")

# Funções para menu 1 - Aritmética
def menu_1():
    opcao = 0
    while opcao != 5:
        opcao = int(input(">> "))
        if opcao in range(1, 5):
            num1 = float(input("Número 1: "))
            num2 = float(input("Número 2: "))
            if opcao == 1:
                print(f'{num1} + {num2} = {num1 + num2}')
            elif opcao == 2:
                print(f'{num1} - {num2} = {num1 - num2}')
            elif opcao == 3:
                print(f'{num1} x {num2} = {num1 * num2}')
            else:
                print(dividir(num1, num2))
        elif opcao != 5:
            print('Opção inválida.')

# Funções para menu 2 - Potência e logaritmo
def menu_2():
    opcao = 0
    while opcao != 6:
        opcao = int(input(">> "))
        if opcao in range(1, 6):
            if opcao in [1, 2, 4]:
                num1 = float(input('Número: '))
                if opcao == 1:
                    print(f'{num1}² = {num1 ** 2}')
                elif opcao == 2:
                    print(f'{num1}³ = {num1 ** 3}')
                else:
                    print(f'Log10({num1}) = {math.log10(num1)}')
            elif opcao == 3:
                base = float(input("Base da potência: "))
                exp = float(input("Expoente: "))
                print(f'{base}^{exp} = {base ** exp}')
            elif opcao == 5:
                base = float(input("Base do log: "))
                num = float(input("Número: "))
                print(f'Log de {num} na base {base} = {math.log(num, base)}')
        elif opcao != 6:
            print('Opção inválida.')

# Funções para menu 3 - Trigonometria
def menu_3():
    opcao = 0
    while opcao != 4:
        opcao = int(input(">> "))
        if opcao in range(1, 4):
            num = float(input("Número (em radianos): "))
            if opcao == 1:
                print(f"sen({num}) = {math.sin(num)}")
            elif opcao == 2:
                print(f"cos({num}) = {math.cos(num)}")
            else:
                print(f"tan({num}) = {math.tan(num)}")
        elif opcao != 4:
            print('Opção inválida.')

# Funções para menu 4 - Outras
def menu_4():
    opcao = 0
    while opcao != 2:
        opcao = int(input(">> "))
        if opcao == 1:
            num = int(input("Digite o número inteiro: "))
            print(f"{num}! = {math.factorial(num)}")
        elif opcao != 2:
            print('Opção inválida.')

# Função principal que executa o programa
def main():
    escolha = ''
    while escolha != '5':
        menu_principal()
        escolha = input(">> ")
        if escolha == '1':
            opcoes_1()
            menu_1()
        elif escolha == '2':
            opcoes_2()
            menu_2()
        elif escolha == '3':
            opcoes_3()
            menu_3()
        elif escolha == '4':
            opcoes_4()
            menu_4()
        elif escolha == '5':
            print("Fim do programa")
        else:
            print("Opção inválida")

# Executa o programa
if __name__ == '__main__':
    main()
