import { abrirDb } from './gerarDB.js'

export async function CadastrarContaDB(conta) {
    abrirDb().then(db => {
        db.run(`INSERT INTO Contas (saldo, tipoConta, instituiçaoFinanceira) VALUES (?,?,?)`, [conta.saldo, conta.tipoConta, conta.instituiçaoFinanceira]);
    })
}

export async function EditarContaDB(conta) {
    abrirDb().then(db => {
        db.run(`UPDATE Contas SET saldo = ?, tipoConta = ?, instituiçaoFinanceira = ? WHERE id = ?`, [conta.saldo, conta.tipoConta, conta.instituiçaoFinanceira, conta.id]);
    })
}

export async function DeletarContaDB(conta) {
    abrirDb().then(db => {
        db.run(`DELETE FROM Contas WHERE id = ?`, [conta.id]);
    })
}

export async function ListarContaDB() {
    return abrirDb().then(db => {
        return db.all(`SELECT * FROM Contas`).then(res => res)
    })
}

export async function TransferirContaDB(conta) {
    return abrirDb().then(db => {
        return db.all(`SELECT saldo FROM Contas WHERE id = ?`, [conta.id1]).then(res => {
            if(res[0].saldo >= conta.valor) {
                db.run(`UPDATE Contas SET saldo = ? WHERE id = ?`, [res[0].saldo - conta.valor, conta.id1])
                db.all(`SELECT saldo FROM Contas WHERE id = ?`, [conta.id2]).then(res2 => {
                    db.run(`UPDATE Contas SET saldo = ? WHERE id = ?`, [res2[0].saldo + conta.valor, conta.id2])
                })
            } else {
                return "Valor Insuficiente na primeira conta."
            }
        })
    })
}

export async function TotalContaDB() {
    return abrirDb().then(db => {
        return db.all(`SELECT sum(saldo) from Contas`).then(res => {
            return res[0]
        })
    })
}