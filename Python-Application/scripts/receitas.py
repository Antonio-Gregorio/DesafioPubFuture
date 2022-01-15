import os
from api.api_receitas import *


def criarReceita():
    os.system('cls' if os.name == 'nt' else 'clear')
    valor = input('Digite o valor: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    dataRecebimento = input('Digite a data de recebimento, exemplo:(2022-12-30) : ')
    os.system('cls' if os.name == 'nt' else 'clear')
    dataRecebimentoEsperado = input('Digite a data de recebimento, exemplo:(2022-12-30) : ')
    os.system('cls' if os.name == 'nt' else 'clear')
    descrição = input('Digite a descrição: ')
    tipoReceita = 0
    while tipoReceita != '1' and tipoReceita != '2' and tipoReceita != '3' and tipoReceita != '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1.Salário\n2.Prêmio\n3.Presente\n4.Outros')
        tipoReceita = str(input('Escolha o tipo de receita: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    conta = input('Digite o id da conta: ')

    if tipoReceita == '1':
        tipoReceita = "Salário"
    elif tipoReceita == '2':
        tipoReceita = "Prêmio"
    elif tipoReceita == '3':
        tipoReceita = "Presente"
    elif tipoReceita == '4':
        tipoReceita = "Outros"

    data = {}
    data['valor'] = valor
    data['dataRecebimento'] = dataRecebimento
    data['dataRecebimentoEsperado'] = dataRecebimentoEsperado
    data['descrição'] = descrição
    data['tipoReceita'] = tipoReceita
    data['conta'] = conta

    postReceitas(data)

def editarReceita():
    os.system('cls' if os.name == 'nt' else 'clear')
    id = input('Digite o id: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    valor = input('Digite o valor: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    dataRecebimento = input('Digite a data de recebimento, exemplo:(2022-12-30) : ')
    os.system('cls' if os.name == 'nt' else 'clear')
    dataRecebimentoEsperado = input('Digite a data de recebimento, exemplo:(2022-12-30) : ')
    os.system('cls' if os.name == 'nt' else 'clear')
    descrição = input('Digite a descrição: ')
    tipoReceita = 0
    while tipoReceita != '1' and tipoReceita != '2' and tipoReceita != '3' and tipoReceita != '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1.Salário\n2.Prêmio\n3.Presente\n4.Outros')
        tipoReceita = str(input('Escolha o tipo de receita: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    conta = input('Digite o id da conta: ')

    if tipoReceita == '1':
        tipoReceita = "Salário"
    elif tipoReceita == '2':
        tipoReceita = "Prêmio"
    elif tipoReceita == '3':
        tipoReceita = "Presente"
    elif tipoReceita == '4':
        tipoReceita = "Outros"

    data = {}
    data['id'] = id
    data['valor'] = valor
    data['dataRecebimento'] = dataRecebimento
    data['dataRecebimentoEsperado'] = dataRecebimentoEsperado
    data['descrição'] = descrição
    data['tipoReceita'] = tipoReceita
    data['conta'] = conta

    putReceitas(data)
    

def deletarReceita():
    os.system('cls' if os.name == 'nt' else 'clear')
    id = input('Digite o id da receita para deleta-la: ')
    data = {}
    data['id'] = id
    delReceitas(data)

def filtrarReceita():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('1.Filtrar por Ano\n2.Filtrar por Tipo de Tipo de Receita\n')
    tipoFiltro = input('Escolha o filtro: ')
    os.system('cls' if os.name == 'nt' else 'clear')

    if tipoFiltro == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        DataInicial = input('Digite a data inicial, exemplo (2000-12-30): ')
        os.system('cls' if os.name == 'nt' else 'clear')
        DataFinal = input('Digite a data final, exemplo (2000-12-30): ')
        os.system('cls' if os.name == 'nt' else 'clear')
        getReceitas(True, '1', DataInicial, DataFinal)
        input()


    elif tipoFiltro == '2':
        tipoReceita = 0
        while tipoReceita != '1' and tipoReceita != '2' and tipoReceita != '3' and tipoReceita != '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('1.Salário\n2.Prêmio\n3.Presente\n4.Outros')
            tipoReceita = str(input('Escolha o tipo de receita: '))
        os.system('cls' if os.name == 'nt' else 'clear')

        if tipoReceita == '1':
            getReceitas(True, '2', "Salário")
            input()
        elif tipoReceita == '2':
            getReceitas(True, '2', "Prêmio")
            input()
        elif tipoReceita == '3':
            getReceitas(True, '2', "Presente")
            input()
        elif tipoReceita == '4':
            getReceitas(True, '2', "Outros")
            input()
