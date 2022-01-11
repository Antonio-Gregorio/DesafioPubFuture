import os
from api.api_despesas import *


def criarDespesa():
    os.system('cls' if os.name == 'nt' else 'clear')
    valor = input('Digite o valor: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    dataPagamento = input('Digite a data de pagamento, exemplo:(2022-12-30) : ')
    os.system('cls' if os.name == 'nt' else 'clear')
    dataPagamentoEsperado = input('Digite a data de pagamento, exemplo:(2022-12-30) : ')
    tipoDespesa = 0
    while tipoDespesa != '1' and tipoDespesa != '2' and tipoDespesa != '3' and tipoDespesa != '4' and tipoDespesa != '5' and tipoDespesa != '6' and tipoDespesa != '7' and tipoDespesa != '8':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1.Alimentação\n2.Educação\n3.Lazer\n4.Moradia\n5.Roupa\n6.Saúde\n7.Transporte\n8.Outros')
        tipoDespesa = str(input('Escolha o tipo de despesa: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    conta = input('Digite o id da conta: ')

    if tipoDespesa == '1':
        tipoDespesa = "Alimentação"
    elif tipoDespesa == '2':
        tipoDespesa = "Educação"
    elif tipoDespesa == '3':
        tipoDespesa = "Lazer"
    elif tipoDespesa == '4':
        tipoDespesa = "Moradia"
    elif tipoDespesa == '5':
        tipoDespesa = "Roupa"
    elif tipoDespesa == '6':
        tipoDespesa = "Saúde"
    elif tipoDespesa == '7':
        tipoDespesa = "Transporte"
    elif tipoDespesa == '8':
        tipoDespesa = "Outros"

    data = {}
    data['valor'] = valor
    data['dataPagamento'] = dataPagamento
    data['dataPagamentoEsperado'] = dataPagamentoEsperado
    data['tipoDespesa'] = tipoDespesa
    data['conta'] = conta

    postDespesa(data)

def editarDespesa():
    os.system('cls' if os.name == 'nt' else 'clear')
    id = input('Digite o id: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    valor = input('Digite o valor: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    dataPagamento = input('Digite a data de pagamento, exemplo:(2022-12-30) : ')
    os.system('cls' if os.name == 'nt' else 'clear')
    dataPagamentoEsperado = input('Digite a data de pagamento, exemplo:(2022-12-30) : ')
    tipoDespesa = 0
    while tipoDespesa != '1' and tipoDespesa != '2' and tipoDespesa != '3' and tipoDespesa != '4' and tipoDespesa != '5' and tipoDespesa != '6' and tipoDespesa != '7' and tipoDespesa != '8':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1.Alimentação\n2.Educação\n3.Lazer\n4.Moradia\n5.Roupa\n6.Saúde\n7.Transporte\n8.Outros')
        tipoDespesa = str(input('Escolha o tipo de despesa: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    conta = input('Digite o id da conta: ')

    if tipoDespesa == '1':
        tipoDespesa = "Alimentação"
    elif tipoDespesa == '2':
        tipoDespesa = "Educação"
    elif tipoDespesa == '3':
        tipoDespesa = "Lazer"
    elif tipoDespesa == '4':
        tipoDespesa = "Moradia"
    elif tipoDespesa == '5':
        tipoDespesa = "Roupa"
    elif tipoDespesa == '6':
        tipoDespesa = "Saúde"
    elif tipoDespesa == '7':
        tipoDespesa = "Transporte"
    elif tipoDespesa == '8':
        tipoDespesa = "Outros"

    data = {}
    data['id'] = id
    data['valor'] = valor
    data['dataPagamento'] = dataPagamento
    data['dataPagamentoEsperado'] = dataPagamentoEsperado
    data['tipoDespesa'] = tipoDespesa
    data['conta'] = conta

    putDespesa(data)
    

def deletarDespesa():
    os.system('cls' if os.name == 'nt' else 'clear')
    id = input('Digite o id da despesa para deleta-la: ')
    data = {}
    data['id'] = id
    delDespesa(data)

def filtrarDespesa():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('1.Filtrar por Ano\n2.Filtrar por Tipo de Tipo de Despesa\n')
    tipoFiltro = input('Escolha o filtro: ')
    os.system('cls' if os.name == 'nt' else 'clear')

    if tipoFiltro == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        DataInicial = input('Digite a data inicial, exemplo (2000-12-30): ')
        os.system('cls' if os.name == 'nt' else 'clear')
        DataFinal = input('Digite a data final, exemplo (2000-12-30): ')
        os.system('cls' if os.name == 'nt' else 'clear')
        getDespesas(True, '1', DataInicial, DataFinal)
        input()


    elif tipoFiltro == '2':
        tipoDespesa = 0
        while tipoDespesa != '1' and tipoDespesa != '2' and tipoDespesa != '3' and tipoDespesa != '4' and tipoDespesa != '5' and tipoDespesa != '6' and tipoDespesa != '7' and tipoDespesa != '8':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('1.Alimentação\n2.Educação\n3.Lazer\n4.Moradia\n5.Roupa\n6.Saúde\n7.Transporte\n8.Outros')
            tipoDespesa = str(input('Escolha o tipo de despesa: '))
        os.system('cls' if os.name == 'nt' else 'clear')

        if tipoDespesa == '1':
            getDespesas(True, '2', "Alimentação")
            input()
        elif tipoDespesa == '2':
            getDespesas(True, '2', "Educação")
            input()
        elif tipoDespesa == '3':
            getDespesas(True, '2', "Lazer")
            input()
        elif tipoDespesa == '4':
            getDespesas(True, '2', "Moradia")
            input()
        elif tipoDespesa == '5':
            getDespesas(True, '2', "Roupa")
            input()
        elif tipoDespesa == '6':
            getDespesas(True, '2', "Saúde")
            input()
        elif tipoDespesa == '7':
            getDespesas(True, '2', "Transporte")
            input()
        elif tipoDespesa == '8':
            getDespesas(True, '2', "Outros")
            input()
