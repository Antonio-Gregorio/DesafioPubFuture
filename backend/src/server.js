// Adicionando o .env
import 'dotenv/config'

// Gerando Banco de dados
import { createTables } from './database/createTables.js'

// Importando Rotas
import { rota } from './routes/routes.js'

// Gerando o express
import express, { json } from 'express'
var http = express()
var porta = process.env.PORTA

http.get("/", (req, res) => {
    res.json({"message":"Ok"})
})

http.use(json())
http.use(rota)

createTables()



// Iniciando o serviço
http.listen(porta, () => {
    console.log("[✅] Servidor Ligado !")
})