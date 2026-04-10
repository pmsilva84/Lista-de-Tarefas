const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./mydb.sqlite');

db.run(`
    CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
);
    `);

db.run(`INSERT into tarefas(nome)values("test")`)

const insertValues = document.getElementById('taskvalue')
    
insertValues.addEventListener('click', function(){
    let nametask = document.getElementById('nametask').values
        
    db.run(`INSERT into tarefas(nome)values(?)`,[nametask])
})
    
    const showTask = document.getElementById('showtask')
    showTask.addEventListener(async function(){
        for(let i = 1; i == db.run(`Select * FROM tarefas`); i++){
            const li = document.createElement('li').innerHTML = i
            
            showTask.appendChild(li)
        }
    })

db.close()