import sqlite3
from pathlib import Path
import os

ROOT_DIR = Path(__file__).parent
PATHDB = 'Lista.sqlite3'
PATHFILE = ROOT_DIR/PATHDB



class Tafera():
    def __init__(self,nome, data):
        self.nome = nome
        self.data = data

    def inserirdados(self,conn):
        cur = conn.cursor()
        cur.execute("Insert into tarefas(nome,data) values(?,?)",(self.nome, self.data))
        conn.commit()
        cur.close()

def showtarefa(conn):
    cur = conn.cursor()
    rows = cur.execute("Select * FROM tarefas")
    for row in rows:
        print(f"{row[0]}) {row[1]} - {row[2]}")

def removatarefa(conn):
    cur = conn.cursor()
    os.system('clear')
    showtarefa(conn)
    try:
        choice = int(input('Qual tarefa você quer remover (escolha pelo seu indice)'))
        cur.execute("DELETE from tarefas where id = ?",(choice,))
        conn.commit()
        taskname = cur.execute("Select nome from tarefas where id = ? ",(choice,))

        showtarefa(conn)
    except (KeyboardInterrupt,TypeError,ValueError):
        print("Uses os numeros do indice")
        removatarefa(conn)
    

conn = sqlite3.connect(PATHFILE)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS tarefas(
                id integer primary key autoincrement,
                nome text,
                data text
            )""")
