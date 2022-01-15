import requests
import datetime

from tabulate import tabulate

def getContas():


        req = requests.get('http://localhost:8000/conta/listar')
        list = []
        valorTotal = 0


        for x in req.json():
                if x != []:
                        list.append([x['id'],'R${:,.2f}'.format(float(str(x['saldo']).replace(",","."))),x['tipoConta'],x['instituiçaoFinanceira']])
                        valorTotal += float(str(x['saldo']).replace(",","."))

        print(tabulate(list, headers=['ID','Saldo','Tipo de Conta','Instituição Financeira']))
        print('\nValor Total: R${:,.2f}'.format(valorTotal))

    
    


def postConta(data):
        req = requests.post('http://localhost:8000/conta/cadastrar', json=data)

def putConta(data):
        req = requests.put('http://localhost:8000/conta/editar', json=data)

def delConta(data):
        req = requests.delete('http://localhost:8000/conta/deletar', json=data)

def transConta(data):
        req = requests.post('http://localhost:8000/conta/transferir', json=data)

def totalContas():
        req = requests.get('http://localhost:8000/conta/total')
        list = []





