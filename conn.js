const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database('./mydb.sqlite');

db.run(`
    CREATE TABLE IF NOT EXISTS tarefas(
        id integer primary key autoincrement,                
        nome text,

    )
    `)

db.close()



const insertValues = document.getElementById('taskvalue')

insertValues.addEventListener('click', function(){
    let nametask = document.getElementById('nametask').values
    
    db.run(`INSERT into tarefas(nome)values(?)`,[nametask])
})

const showTask = document.getElementById('showtask')
showTask.addEventListener(function(){
    for(let i = 0; i == db.run(`Select * FROM tarefas`); i++){
        document.createElement('li').innerHTML = i
    }
})