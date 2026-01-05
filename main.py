import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
PATHDB = 'Lista.sqlite3'
PATHFILE = ROOT_DIR/PATHDB


class Tafera():
    def __init__(nome, data, self):
        self.nome = nome
        self.data = data

    def inserirdados(self,conn):
        cur = conn.cursor()
        cur.excute("Insert into tabelas (nome,data) values(?,?)",(self.nome, self.data))
        conn.commit()

def showtarefa(conn):
    cur = conn.cursor()
    rows = cur.execute("Select * FROM tarefas")
    for row in rows:
        print(f"{row[0]}) {row[1]} - {row[2]}")

def removatarefa(conn):
    cur = conn.cursor()
    showtarefa(conn)


conn = sqlite3.connect(PATHFILE)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS tarefas(
                id integer primary key autoincrement,
                nome text,
                data text
            )""")

task = Tafera("oi","2026-01-04")
task.inserirdados()
