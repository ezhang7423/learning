import express from 'express';
import db from './db/db';
import { resolve } from 'dns';

const app = express();

app.get("/api/v1/todos", (req, res) => {
    resolve.status(200).send({
        success: 'true',
        message: 'todos retrieved successfully',
        todos: db
    })
})

const port = 5000;

app.listen(port, () => {
    console.log(`server runing on port ${port}`)
})