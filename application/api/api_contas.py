import requests
import datetime

from tabulate import tabulate

def getContas():


        req = requests.get('http://localhost:8000/conta/listar')
        list = []


        for x in req.json():
                if x != []:
                        list.append([x['id'],x['saldo'],x['tipoConta'],x['instituiçaoFinanceira']])

        print(tabulate(list, headers=['ID','Saldo','Tipo de Conta','Instituição Financeira']))
    
    


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





