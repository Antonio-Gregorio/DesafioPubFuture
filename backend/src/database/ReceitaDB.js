import { abrirDb } from './gerarDB.js'

export async function CadastrarReceitaDB(receita) {
    abrirDb().then(db => {
        db.run(`INSERT INTO Receitas (valor, dataRecebimento, dataRecebimentoEsperado, descrição, tipoReceita, conta) VALUES (?,?,?,?,?,?)`, [receita.valor, receita.dataRecebimento, receita.dataRecebimentoEsperado, receita.descrição, receita.tipoReceita, receita.conta]);
    })
}

export async function EditarReceitaDB(receita) {
    abrirDb().then(db => {
        db.run(`UPDATE Receitas SET valor = ?, dataRecebimento = ?, dataRecebimentoEsperado = ?, descrição = ?, tipoReceita = ?, conta = ? WHERE id = ?`, [receita.valor, receita.dataRecebimento, receita.dataRecebimentoEsperado, receita.descrição, receita.tipoReceita, receita.conta, receita.id]);
    })
}

export async function DeletarReceitaDB(receita) {
    abrirDb().then(db => {
        db.run(`DELETE FROM Receitas WHERE id = ?`, [receita.id]);
    })
}

export async function ListarReceitaDB() {
    return abrirDb().then(db => {
        return db.all(`SELECT * FROM Receitas`).then(res => res)
    })
}