from api.api_receitas import getReceitas
from scripts.receitas import criarReceita, deletarReceita, editarReceita, filtrarReceita
import os

class Interface:

    # init
    def __init__(self):
        self.instance = 1
        self.menu_iniciar()

    # Menu inicial
    def menu_iniciar(self):
        while self.instance == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('===============\nFinanças Pessoais\n===============\n')
            print('1.Receitas\n2.Despesas\n3.Contas\n4.Sair\n')
            op = int(input('Digite uma opção: '))

            if op == 1:
                self.instance = 2
                self.menu_receitas()
            elif op == 4:
                self.instance = 0

    # Menu de Receitas
    def menu_receitas(self):
        while self.instance == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(getReceitas())
            print('\n1.Criar\n2.Editar\n3.Deletar\n4.Filtrar\n5.Voltar\n')
            op = input('Digite uma opção: ')

            if op == '1':
                criarReceita()

            if op == '2':
                editarReceita()
            
            if op == '3':
                deletarReceita()

            if op == '4':
                filtrarReceita()

            if op == '5':
                self.instance = 1

    


        
        