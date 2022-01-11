import { abrirDb } from './gerarDB.js'

export async function CadastrarDespesaDB(despesa) {
    abrirDb().then(db => {
        db.run(`INSERT INTO Despesas (valor, dataPagamento, dataPagamentoEsperado, tipoDespesa, conta) VALUES (?,?,?,?,?)`, [despesa.valor, despesa.dataPagamento, despesa.dataPagamentoEsperado, despesa.tipoDespesa, despesa.conta]);
    })
}

export async function EditarDespesaDB(despesa) {
    abrirDb().then(db => {
        db.run(`UPDATE Despesas SET valor = ?, dataPagamento = ?, dataPagamentoEsperado = ?, tipoDespesa = ?, conta = ? WHERE id = ?`, [despesa.valor, despesa.dataPagamento, despesa.dataPagamentoEsperado, despesa.tipoDespesa, despesa.conta, despesa.id]);
    })
}

export async function DeletarDespesaDB(despesa) {
    abrirDb().then(db => {
        db.run(`DELETE FROM Despesas WHERE id = ?`, [despesa.id]);
    })
}

export async function ListarDespesaDB() {
    return abrirDb().then(db => {
        return db.all(`SELECT * FROM Despesas`).then(res => res)
    })
}