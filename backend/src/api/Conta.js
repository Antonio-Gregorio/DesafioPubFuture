import { CadastrarContaDB, DeletarContaDB, EditarContaDB, ListarContaDB, TransferirContaDB } from '../database/ContaDB.js';


export async function ListarConta (req, res) {
    res.json(await ListarContaDB())
    console.log("[👍] Conta Listada..")
}

// CADASTRAR CONTA
export async function CadastrarConta (req, res) {
    CadastrarContaDB(req.body)
    res.json({
        "statusCode": 200
    })
    console.log("[👍] Conta Cadastrada..")
}

// EDITAR CONTA
export async function EditarConta (req, res) {
    EditarContaDB(req.body)
    res.json({
        "statusCode": 200
    })
    console.log("[👍] Conta Editada..")
}

// DELETAR CONTA
export async function DeletarConta (req, res) {
    DeletarContaDB(req.body)
    res.json({
        "statusCode": 200
    })
    console.log("[👍] Conta Deletada..")
}

// TRANSFERIR SALDO CONTA
export async function TransferirConta (req, res) {
    res.json(await TransferirContaDB(req.body))
    console.log("[👍] Conta Transferencia Realizada..")
}