import { abrirDb } from './gerarDB.js'

export async function CadastrarDespesaDB(despesa) {
    abrirDb().then(db => {
        db.run(`INSERT INTO Despesas (valor, dataRecebimento, dataRecebimentoEsperado, tipoDespesa, conta) VALUES (?,?,?,?,?)`, [despesa.valor, despesa.dataRecebimento, despesa.dataRecebimentoEsperado, despesa.tipoDespesa, despesa.conta]);
    })
}

export async function EditarDespesaDB(despesa) {
    abrirDb().then(db => {
        db.run(`UPDATE Despesas SET valor = ?, dataRecebimento = ?, dataRecebimentoEsperado = ?, tipoDespesa = ?, conta = ? WHERE id = ?`, [despesa.valor, despesa.dataRecebimento, despesa.dataRecebimentoEsperado, despesa.tipoDespesa, despesa.conta, despesa.id]);
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