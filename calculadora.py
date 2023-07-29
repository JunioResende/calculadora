from colorama import Fore, Style, Back

operacao = input('Qual a operacao desejada? ')

if operacao != '+' and operacao != '-' and operacao != '*' and operacao != '/' and operacao != '**':
    print (f'{Fore.RED}Operador ({operacao}) inexistente nessa calculadora. Nao sera possivel calcular!{Style.RESET_ALL}')


A = float(input('Digite o primeiro numero da operacao: '))
B = float(input('Digite o segundo numero da operacao: '))

if operacao == '+':
    print(f'A soma ({operacao}) desses 2 numeros e igual a {Fore.GREEN}{A+B}{Style.RESET_ALL}')
elif operacao == '-':
    print(f'A subtracao ({operacao}) desses 2 numeros e igual a {Fore.RED}{A-B}{Style.RESET_ALL}')
elif operacao == '*':
    print(f'A multiplicacao ({operacao}) desses 2 numeros e igual a {Fore.BLUE}{A*B}{Style.RESET_ALL}')
elif operacao == '/':
    print(f'A divisao ({operacao}) desses 2 numeros e igual a {Fore.YELLOW}{A/B}{Style.RESET_ALL}')
elif operacao == '**':
    print(f'A potenciacao ({operacao}) desses 2 numeros e igual a {Fore.CYAN}{A**B}{Style.RESET_ALL}')
