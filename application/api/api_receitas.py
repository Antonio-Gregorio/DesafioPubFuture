import requests
import datetime

from tabulate import tabulate

def getReceitas(filtro = False,type = False, args = False, args2 = False):

    if filtro == False:

        req = requests.get('http://localhost:8000/receita/listar')
        list = []

        list.append(['ID','Valor','Data de Recebimento','Data de Recebimento Esperado','Descrição','Tipo de Receita','Conta'])

        for x in req.json():
                if x != []:
                        list.append([x['id'],x['valor'],x['dataRecebimento'],x['dataRecebimentoEsperado'],x['descrição'],x['tipoReceita'],x['conta']])

        print(tabulate(list))
    
    else:
            if type == '1':
                dataI = args.split("-")
                dataF = args2.split("-")

                dataIM = datetime.datetime(int(dataI[0]), int(dataI[1]), int(dataI[2]))
                dataFM = datetime.datetime(int(dataF[0]), int(dataF[1]), int(dataF[2]))

                req = requests.get('http://localhost:8000/receita/listar')
                list = []

                list.append(['ID','Valor','Data de Recebimento','Data de Recebimento Esperado','Descrição','Tipo de Receita','Conta'])

                for x in req.json():
                        if x != []:
                                DataA = str(x['dataRecebimento']).split('-')
                                DataAtual = datetime.datetime(int(DataA[0]), int(DataA[1]), int(DataA[2]))

                                if  DataAtual >= dataIM and DataAtual <= dataFM:
                                        list.append([x['id'],x['valor'],x['dataRecebimento'],x['dataRecebimentoEsperado'],x['descrição'],x['tipoReceita'],x['conta']])

                print(tabulate(list))

            elif type == '2':
                req = requests.get('http://localhost:8000/receita/listar')
                list = []

                list.append(['ID','Valor','Data de Recebimento','Data de Recebimento Esperado','Descrição','Tipo de Receita','Conta'])

                for x in req.json():
                        if x != []:
                                if x['tipoReceita'] == args:
                                        list.append([x['id'],x['valor'],x['dataRecebimento'],x['dataRecebimentoEsperado'],x['descrição'],x['tipoReceita'],x['conta']])

                print(tabulate(list))


def postReceitas(data):
        req = requests.post('http://localhost:8000/receita/cadastrar', json=data)

def putReceitas(data):
        req = requests.put('http://localhost:8000/receita/editar', json=data)

def delReceitas(data):
        req = requests.delete('http://localhost:8000/receita/deletar', json=data)


