import { CadastrarDespesaDB, DeletarDespesaDB, EditarDespesaDB, ListarDespesaDB } from '../database/DespesasDB.js';


export async function ListarDespesa (req, res) {
    res.json(await ListarDespesaDB())
    console.log("[👍] Despesa Listada..")
}

// CADASTRAR Despesa
export async function CadastrarDespesa (req, res) {
    CadastrarDespesaDB(req.body)
    res.json({
        "statusCode": 200
    })
    console.log("[👍] Despesa Cadastrada..")
}

// EDITAR Despesa
export async function EditarDespesa (req, res) {
    EditarDespesaDB(req.body)
    res.json({
        "statusCode": 200
    })
    console.log("[👍] Despesa Editada..")
}

// DELETAR Despesa
export async function DeletarDespesa (req, res) {
    DeletarDespesaDB(req.body)
    res.json({
        "statusCode": 200
    })
    console.log("[👍] Despesa Deletada..")
}