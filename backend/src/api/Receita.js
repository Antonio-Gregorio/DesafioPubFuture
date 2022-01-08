import { CadastrarReceitaDB, DeletarReceitaDB, EditarReceitaDB, ListarReceitaDB } from '../database/ReceitaDB.js';


export async function ListarReceita (req, res) {
    res.json(await ListarReceitaDB())
    console.log("[👍] Receita Listada..")
}

// CADASTRAR RECEITA
export async function CadastrarReceita (req, res) {
    CadastrarReceitaDB(req.body)
    res.json({
        "statusCode": 200
    })
    console.log("[👍] Receita Cadastrada..")
}

// EDITAR RECEITA
export async function EditarReceita (req, res) {
    EditarReceitaDB(req.body)
    res.json({
        "statusCode": 200
    })
    console.log("[👍] Receita Editada..")
}

// DELETAR RECEITA
export async function DeletarReceita (req, res) {
    DeletarReceitaDB(req.body)
    res.json({
        "statusCode": 200
    })
    console.log("[👍] Receita Deletada..")
}