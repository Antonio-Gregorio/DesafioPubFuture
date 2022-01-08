import { Router } from 'express';
import { CadastrarConta, DeletarConta, EditarConta, ListarConta, TotalConta, TransferirConta } from '../api/Conta.js';
import { CadastrarDespesa, DeletarDespesa, EditarDespesa, ListarDespesa } from '../api/Despesa.js';
import { CadastrarReceita, DeletarReceita, EditarReceita, ListarReceita } from '../api/Receita.js';

export const rota = Router();


// LISTAR RECEITA
rota.get('/receita/listar', ListarReceita)
// CADASTRAR RECEITA
rota.post('/receita/cadastrar', CadastrarReceita)
// EDITAR RECEITA
rota.put('/receita/editar', EditarReceita)
// DELETAR RECEITA
rota.delete('/receita/deletar', DeletarReceita)


// LISTAR DESPESA
rota.get('/despesa/listar', ListarDespesa)
// CADASTRAR DESPESA
rota.post('/despesa/cadastrar', CadastrarDespesa)
// EDITAR DESPESA
rota.put('/despesa/editar', EditarDespesa)
// DELETAR DESPESA
rota.delete('/despesa/deletar', DeletarDespesa)


// LISTAR CONTA
rota.get('/conta/listar', ListarConta)
// CADASTRAR CONTA
rota.post('/conta/cadastrar', CadastrarConta)
// EDITAR CONTA
rota.put('/conta/editar', EditarConta)
// DELETAR CONTA
rota.delete('/conta/deletar', DeletarConta)
// TRANSFERIR CONTA
rota.post('/conta/transferir', TransferirConta)
// TOTAL CONTA
rota.get('/conta/total', TotalConta)