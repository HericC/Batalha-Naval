import random
cores = {"restart": '\033[m',
         "default": '\033[1;7;30m',
         "azul": '\033[1;7;34m',
         "ciano": '\033[1;7;36m',
         "vermelho": '\033[1;7;31m',
         "verde": '\033[1;7;32m'}


def validar_int(numero):
    try:
        numero = int(numero)
        return entrada_scop(numero)
    except ValueError:
        return validar_int(input('\033[31mNúmero Invalido!\n'
                                 'Permitido apenas números inteiros.\033[0m\n'
                                 'Informe Novamente: '))


def entrada_scop(numero):
    if numero < 1 or numero > 9:
        return validar_int(input('\033[31mNúmero Invalido!\n'
                                 'Permitido apenas entre 1 e 9.\033[0m\n'
                                 'Informe Novamente: '))
    else:
        return numero


def mapa():
    lista = []
    for l in range(9):
        lista.append([])
        for c in range(9):
            lista[l].append(f'{cores["azul"]}   ')

    for i in range(4, 0, -1):
        for p in range(5, i, -1):
            if random.randint(False, True):
                while True:
                    posisao = random.randint(0, 8)
                    lis = random.randint(0, 8)
                    while lis + i >= 9:
                        lis = random.randint(0, 8)
                    ok = True
                    for j in range(i):
                        if lista[lis + j][posisao] != f'{cores["azul"]}   ':
                            ok = False
                            break
                    if ok:
                        break
                for r in range(i):
                    lista[lis + r][posisao] = f'{cores["azul"]} x '
            else:
                while True:
                    posisao = random.randint(0, 8)
                    lis = random.randint(0, 8)
                    while posisao + i >= 9:
                        posisao = random.randint(0, 8)
                    ok = True
                    for j in range(i):
                        if lista[lis][posisao + j] != f'{cores["azul"]}   ':
                            ok = False
                            break
                    if ok:
                        break
                for f in range(i):
                    lista[lis][posisao + f] = f'{cores["azul"]} x '
    return lista


def bomba(m1, m2, m3, lista1, lista2, m0=True):
    if m0:
        entrada = validar_entrada(m1, m2, m3, lista1, lista2, m0)
        lista1.append(entrada)

        if m2[entrada[0]-1][entrada[1]-1] == f'{cores["azul"]}   ':
            m3[entrada[0]-1][entrada[1]-1] = f'{cores["ciano"]}   '
            return bomba(m1, m2, m3, lista1, lista2, False)
        else:
            m3[entrada[0]-1][entrada[1]-1] = f'{cores["vermelho"]} x '
            printar(m1, m3)
            contador = 0
            for i in m3:
                contador += i.count(f'{cores["vermelho"]} x ')
            if contador == 20:
                print(f'{cores["restart"]}\n{cores["verde"]}Parabêns, Você Ganhou!{cores["restart"]}')
                return True
            print(' Você acertou, Ganhou uma jogada!')
            bomba(m1, m2, m3, lista1, lista2)

    else:
        entrada = validar_entrada(m1, m2, m3, lista1, lista2, m0)
        lista2.append(entrada)
        if m1[entrada[0] - 1][entrada[1] - 1] == f'{cores["azul"]}   ':
            m1[entrada[0] - 1][entrada[1] - 1] = f'{cores["ciano"]}   '
            printar(m1, m3)
            return False
        else:
            m1[entrada[0] - 1][entrada[1] - 1] = f'{cores["vermelho"]} x '
            contador = 0
            for i in m1:
                contador += i.count(f'{cores["vermelho"]} x ')
            if contador == 20:
                printar(m1, m3)
                print(f'{cores["restart"]}\n{cores["vermelho"]}Você Perdeu!{cores["restart"]}')
                return True
            bomba(m1, m2, m3, lista1, lista2, False)


def validar_entrada(m1, m2, m3, lista1, lista2, m0):
    if m0:
        entrada = [validar_int(input(f'{cores["restart"]}\nInforme a Linha: ')),
                   validar_int(input('Informe a Coluna: '))]
        if entrada in lista1:
            print('Posição já utilizada, escolha outra.')
            return validar_entrada(m1, m2, m3, lista1, lista2, m0)
        else:
            return entrada
    else:
        entrada = [random.randint(1, 9), random.randint(1, 9)]
        if entrada in lista2:
            return validar_entrada(m1, m2, m3, lista1, lista2, m0)
        else:
            return entrada


def printar(m1, m3):
    print(f'{cores["default"]}   ', end='')
    for m in range(1, 10):
        print(f'  {m} ', end='')
    print(end='                ')
    for m in range(1, 10):
        print(f'  {m} ', end='')
    print('')

    for i in range(9):
        print(end='    ')
        print('- ' * 18, end='                ')
        print('- ' * 18)
        print('', i+1, end=' ')
        for p in m1[i]:
            print(f'|{p}', end=f'{cores["default"]}')
        print(end='|             ')
        print(i+1, end=' ')
        for p in m3[i]:
            print(f'|{p}', end=f'{cores["default"]}')
        print('|')
    print(end='    ')
    print('- ' * 18, end='                ')
    print('- ' * 18)


def main():
    lista_entradas = []
    lista_auto = []

    m1 = mapa()
    m2 = mapa()
    m3 = []
    for l in range(9):
        m3.append([])
        for c in range(9):
            m3[l].append(f'{cores["azul"]}   ')

    while True:
        n = input('''\nOpções: 
    1 - Jogar
    2 - Encerrar
    Informe o Número da Opção: ''')

        if n == '1':
            printar(m1, m3)
            bomba(m1, m2, m3, lista_entradas, lista_auto)
            while True:
                n1 = input(f'''{cores["restart"]}Opções:
    1 - Continuar
    2 - Desistir
    Informe: ''')
                if n1 == '1':
                    if bomba(m1, m2, m3, lista_entradas, lista_auto):
                        break
                elif n1 == '2':
                    break
                else:
                    print('Código Incorreto.\n')
            break
        elif n == '2':
            break
        else:
            print('Código Incorreto.')
    print('\nJogo Finalizado!!!')


main()
