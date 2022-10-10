print('**********Calculadora Python**********\n')

print('''Tabela de operações: 
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão\n''')

sair = 1

while sair == 1:

    tipoOperacao = int(
        input('Qual operação deseja fazer? Digite o número da operação: '))

    if tipoOperacao == 1:
        print('Operação escolhida: SOMA')
        soma1 = int(input('Digite o primeiro número: '))
        soma2 = int(input('Digite o segundo número: '))
        resultadoSoma = soma1 + soma2
        print(f'{soma1} + {soma2} = {resultadoSoma}')

    elif tipoOperacao == 2:
        print('Operação escolhida: SUBTRAÇÃO')
        sub1 = int(input('Digite o primeiro número: '))
        sub2 = int(input('Digite o segundo número: '))
        resultadoSub = sub1 - sub2
        print(f'{sub1} - {sub2} = {resultadoSub}')

    elif tipoOperacao == 3:
        print('Operação escolhida: MULTIPLICAÇÃO')
        mult1 = int(input('Digite o primeiro número: '))
        mult2 = int(input('Digite o segundo número: '))
        resultadoMult = mult1 * mult2
        print(f'{mult1} * {mult2} = {resultadoMult}')

    elif tipoOperacao == 4:
        print('Operação escolhida: DIVISÃO')
        div1 = int(input('Digite o primeiro número: '))
        div2 = int(input('Digite o segundo número: '))
        resultadoDiv = div1 / div2
        print(f'{div1} / {div2} = {resultadoDiv}')

    sair = int(
        input('Deseja fazer uma nova operação? Digite 1 para SIM e 0 para NÃO: '))
else:
    print('''******Obrigado por usar a minha caluculadora!******
    Código escrito por Osiel Meireles''')
