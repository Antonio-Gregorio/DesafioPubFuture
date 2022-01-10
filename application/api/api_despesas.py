import requests
import json

from tabulate import tabulate

def getDespesas():
    req = requests.get('http://localhost:8000/despesa/listar')
    list = []

    list.append(['ID','Valor','Data de Pagamento','Data de Pagamento Esperado','Tipo de Despesa','Conta'])

    for x in req.json():
        if x != []:
            list.append([x['id'],x['valor'],x['dataPagamento'],x['dataPagamentoEsperado'],x['tipoPagamento'],x['conta']])

    print(tabulate(list))
    

def postDespesas(data):
        req = requests.post('http://localhost:8000/despesa/cadastrar', json=data)

def putDespesas(data):
        req = requests.put('http://localhost:8000/despesa/editar', json=data)

def delDespesas(data):
        req = requests.delete('http://localhost:8000/despesa/deletar', json=data)


