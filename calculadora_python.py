print('**********Calculadora Python**********\n')

print('''Tabela de operações: 
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Módulo
6 - Potenciação\n''')


def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def modulo(x, y):
    impar_par = x % y
    if impar_par == 0:
        return (f'{impar_par} = Par')
    else:
        return (f'{impar_par} = ímpar')


def potenciacao(x, y):
    return x ** y


sair = 1

while sair == 1:

    tipoOperacao = int(
        input('Qual operação deseja fazer? Digite o número da operação: '))
    print('')

    if tipoOperacao == 1:
        print('Operação escolhida: SOMA')
        soma1 = int(input('Digite o primeiro número: '))
        soma2 = int(input('Digite o segundo número: '))
        print('')
        print(f'{soma1} + {soma2} = {soma(soma1, soma2)}\n')

    elif tipoOperacao == 2:
        print('Operação escolhida: SUBTRAÇÃO')
        sub1 = int(input('Digite o primeiro número: '))
        sub2 = int(input('Digite o segundo número: '))
        print('')
        print(f'{sub1} - {sub2} = {subtracao(sub1,sub2)}\n')

    elif tipoOperacao == 3:
        print('Operação escolhida: MULTIPLICAÇÃO')
        mult1 = int(input('Digite o primeiro número: '))
        mult2 = int(input('Digite o segundo número: '))
        print('')
        print(f'{mult1} * {mult2} = {multiply(mult1, mult2)}\n')

    elif tipoOperacao == 4:
        print('Operação escolhida: DIVISÃO')
        div1 = int(input('Digite o primeiro número: '))
        div2 = int(input('Digite o segundo número: '))
        print('')
        print(f'{div1} / {div2} = {divide(div1, div2)}\n')

    elif tipoOperacao == 5:
        print('Operação escolhida: MÓDULO')
        mod1 = int(input('Digite o primeiro número: '))
        mod2 = int(input('Digite o segundo número: '))
        print('')
        print(f'{mod1} % {mod2} = {modulo(mod1, mod2)}\n')

    elif tipoOperacao == 6:
        print('Operação escolhida: POTENCIAÇÃO')
        pot1 = int(input('Digite o primeiro número: '))
        pot2 = int(input('Digite o segundo número: '))
        print('')
        print(f'{pot1} ** {pot2} = {potenciacao(pot1, pot2)}\n')

    else:
        print('Opcão inválida!')

    sair = int(
        input('Deseja fazer uma nova operação? Digite 1 para SIM e 0 para NÃO: '))
    print('')

else:
    print('''******Obrigado por usar a minha caluculadora!******
         Código escrito por Osiel Meireles''')
