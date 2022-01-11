import requests
import datetime

from tabulate import tabulate

def getDespesas(filtro = False,type = False, args = False, args2 = False):

    if filtro == False:

        req = requests.get('http://localhost:8000/despesa/listar')
        list = []


        for x in req.json():
                if x != []:
                        list.append([x['id'],x['valor'],x['dataPagamento'],x['dataPagamentoEsperado'],x['tipoDespesa'],x['conta']])

        print(tabulate(list, headers=['ID','Valor','Data de Pagamento','Data de Pagamento Esperado','Tipo de Despesa','Conta']))
    
    else:
            if type == '1':
                dataI = args.split("-")
                dataF = args2.split("-")

                dataIM = datetime.datetime(int(dataI[0]), int(dataI[1]), int(dataI[2]))
                dataFM = datetime.datetime(int(dataF[0]), int(dataF[1]), int(dataF[2]))

                req = requests.get('http://localhost:8000/despesa/listar')
                list = []

                for x in req.json():
                        if x != []:
                                DataA = str(x['dataPagamento']).split('-')
                                DataAtual = datetime.datetime(int(DataA[0]), int(DataA[1]), int(DataA[2]))

                                if  DataAtual >= dataIM and DataAtual <= dataFM:
                                        list.append([x['id'],x['valor'],x['dataPagamento'],x['dataPagamentoEsperado'],x['tipoDespesa'],x['conta']])

                print(tabulate(list, headers=['ID','Valor','Data de Pagamento','Data de Pagamento Esperado','Tipo de Despesa','Conta']))

            elif type == '2':
                req = requests.get('http://localhost:8000/despesa/listar')
                list = []

                for x in req.json():
                        if x != []:
                                if x['tipoDespesa'] == args:
                                        list.append([x['id'],x['valor'],x['dataPagamento'],x['dataPagamentoEsperado'],x['tipoDespesa'],x['conta']])

                print(tabulate(list, headers=['ID','Valor','Data de Pagamento','Data de Pagamento Esperado','Tipo de Despesa','Conta']))


def postDespesa(data):
        req = requests.post('http://localhost:8000/despesa/cadastrar', json=data)

def putDespesa(data):
        req = requests.put('http://localhost:8000/despesa/editar', json=data)

def delDespesa(data):
        req = requests.delete('http://localhost:8000/despesa/deletar', json=data)





