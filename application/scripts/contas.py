import os
from api.api_contas import *


def criarConta():
    os.system('cls' if os.name == 'nt' else 'clear')
    valor = input('Digite o saldo: ')
    tipoConta = 0
    while tipoConta != '1' and tipoConta != '2' and tipoConta != '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1.Carteira\n2.Conta Corrente\n3.Conta Poupança')
        tipoConta = str(input('Escolha o tipo de receita: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    instituiçaoFinanceira = input('Digite o nome da instituição financeira: ')

    if tipoConta == '1':
        tipoConta = "Carteira"
    elif tipoConta == '2':
        tipoConta = "Conta Corrente"
    elif tipoConta == '3':
        tipoConta = "Conta Poupança"

    data = {}
    data['saldo'] = valor
    data['tipoConta'] = tipoConta
    data['instituiçaoFinanceira'] = instituiçaoFinanceira

    postConta(data)

def editarConta():
    os.system('cls' if os.name == 'nt' else 'clear')
    id = input('Digite o id: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    valor = input('Digite o saldo: ')
    tipoConta = 0
    while tipoConta != '1' and tipoConta != '2' and tipoConta != '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1.Carteira\n2.Conta Corrente\n3.Conta Poupança')
        tipoConta = str(input('Escolha o tipo de receita: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    instituiçaoFinanceira = input('Digite o nome da instituição financeira: ')

    if tipoConta == '1':
        tipoConta = "Carteira"
    elif tipoConta == '2':
        tipoConta = "Conta Corrente"
    elif tipoConta == '3':
        tipoConta = "Conta Poupança"

    data = {}
    data['id'] = id
    data['saldo'] = valor
    data['tipoConta'] = tipoConta
    data['instituiçaoFinanceira'] = instituiçaoFinanceira

    putConta(data)
    

def deletarConta():
    os.system('cls' if os.name == 'nt' else 'clear')
    id = input('Digite o id da conta para deleta-la: ')
    data = {}
    data['id'] = id
    delConta(data)

def transferirConta():
    os.system('cls' if os.name == 'nt' else 'clear')
    id1 = input('Digite o id da conta que vai enviar o dinheiro: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    valor = input('Digite o valor: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    id2 = input('Digite o id da conta que vai receber o dinheiro: ')
    data = {}
    data['id1'] = id1
    data['id2'] = id2
    data['valor'] = valor
    
    transConta(data)