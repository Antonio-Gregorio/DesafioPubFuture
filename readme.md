
# Finanças Pessoais (Desafio Pub Future)

Foi desenvolvido um software de finanças com um backend e conexão por api.
<br>
<br>
<br>
<br>
## Aplicação Java 
<br>

Para Iniciar a aplicação, você deve possuir o Java instalado em seu computador, logo em seguida entre na pasta Java-Application e inicie o programa executavel DesafioPubFuture.jar
<br>
<br>
O Código da aplicação Java se encontra em https://github.com/Antonio-Gregorio/Java-DesafioPubFuture


![RECEITAS](/README/java-receitas.png "Receita")

Aqui temos a Tela de Receitas, com um sistema de Cadastrar, Editar, Deletar e Filtrar os dados recebidos na tabela.

![DESPESAS](/README/java-despesas.png "Despesa")

Aqui temos a Tela de Despesas, com um sistema de Cadastrar, Editar, Deletar e Filtrar os dados recebidos na tabela.

![Contas](/README/java-contas.png "Conta")

Aqui temos a Tela de Contas, com um sistema de Cadastrar, Editar, Deletar e Transferir valor entre as contas, os dados recebidos na tabela.
<br>
<br>
<br>
<br>


## Aplicação Python

Dentro da pasta do projeto, abra a pasta Python-Application e inicie o programa client.py

![PYTHON](/README/python.png "Python")

Aqui temos a Tela de Menu, apartir da mesma é possivel acessar as páginas de receitas, despesas e contas, no qual nelas é possivel cadastrar,editar,deletar,filtrar e transferir valores.

<br>
<br>
<br>
<br>

## Iniciando a API

Abra o terminal na pasta backend e rode os seguintes comandos.

Caso utilize o NODE:
```
npm install
npm start
```
Caso utilize o YARN:
```
yarn
yarn start
```

### Receitas
Cadastrar: [POST] http://localhost:8000/receita/cadastrar<br>
Editar: [PUT] http://localhost:8000/receita/editar<br>
Deletar: [DELETE] http://localhost:8000/receita/deletar<br>
Listar: [GET] http://localhost:8000/receita/listar<br>
<br>
<br>

### Despesas
Cadastrar: [POST] http://localhost:8000/despesa/cadastrar<br>
Editar: [PUT] http://localhost:8000/despesa/editar<br>
Deletar: [DELETE] http://localhost:8000/despesa/deletar<br>
Listar: [GET] http://localhost:8000/despesa/listar<br>
<br>
<br>

### Contas
Cadastrar: [POST] http://localhost:8000/conta/cadastrar<br>
Editar: [PUT] http://localhost:8000/conta/editar<br>
Deletar: [DELETE] http://localhost:8000/conta/deletar<br>
Listar: [GET] http://localhost:8000/conta/listar<br>
Transferir: [POST] http://localhost:8000/conta/transferir<br>
<br>
<br>


# Softwares

| Software | Download |
| ------ | ------ |
| Java | https://java.com/pt-BR/download/ |
| Python | https://www.python.org/downloads/ |
| Yarn | https://classic.yarnpkg.com/lang/en/docs/install |
| Npm | https://nodejs.org/en/download/ |

