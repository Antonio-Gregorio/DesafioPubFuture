import { abrirDb } from './gerarDB.js'

export async function createTables(){
    abrirDb().then(db => {
        db.exec('CREATE TABLE IF NOT EXISTS Contas ( id INTEGER PRIMARY KEY , saldo INTEGER , tipoConta TEXT CHECK( tipoConta IN ("Carteira", "Conta Corrente", "Conta Poupança") ), instituiçaoFinanceira TEXT)')
        db.exec('CREATE TABLE IF NOT EXISTS Despesas ( id INTEGER PRIMARY KEY, valor INTEGER , dataPagamento DATE , dataPagamentoEsperado DATE , tipoDespesa TEXT CHECK( tipoDespesa IN ("Alimentação", "Educação", "Lazer", "Moradia", "Roupa", "Saúde", "Transporte", "Outros") ), conta INTEGER, FOREIGN KEY(conta) REFERENCES Contas(id) )')
        db.exec('CREATE TABLE IF NOT EXISTS Receitas ( id INTEGER PRIMARY KEY, valor INTEGER , dataRecebimento DATE , dataRecebimentoEsperado DATE , descrição TEXT , tipoReceita TEXT CHECK( tipoReceita IN ("Salário", "Presente", "Prêmio", "Outros") ), conta INTEGER, FOREIGN KEY(conta) REFERENCES Contas(id) )')
    })
}