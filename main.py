import sqlite3
import os
import time
from pathlib import Path

ROOT_DIR = Path(__file__).parent
PATHDB = 'Lista.sqlite3'
PATHFILE = ROOT_DIR/PATHDB

## A conexão sql
conn = sqlite3.connect(PATHFILE)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS tarefas(
                id integer primary key autoincrement,
                nome text,
                data text
            )""")

# Uma classe para passar os dados de tarefa
class Tafera():
    def __init__(self,nome, data):
        self.nome = nome
        self.data = data
    
def inserirdados(conn,nome,data):
    newTarefa = Tafera(nome,data)

    cur = conn.cursor()
    cur.execute("Insert into tarefas(nome,data) values(?,?)",(newTarefa.nome, newTarefa.data))
    conn.commit()
    cur.close()

def showtarefa(conn):# 
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
        
        showtarefa(conn)
    except (KeyboardInterrupt,TypeError,ValueError):
        print("Uses os numeros do indice")
        removatarefa(conn)
    
def mainpage ():
    loop = True
    while loop:
        showtarefa(conn)

        print("--------------------------")    

        print("1) Criar tarefa ")
        print("2) Removaer tarefa ")
        print("3) Sair ")
    
        try:
            choice = int(input("escolha uma das opções\n"))
        except (ValueError,KeyboardInterrupt,EOFError):
            os.system('clear')
            print("\n\nAlgo deu errado ... reiniciando..")
            time.sleep(5)
            os.system('clear')
            mainpage()

        if choice == 1 :
            os.system('clear')
            
            nome = input("Qual será a nova tarefa\n")

            data = input("Qual será a data de prazo\n")
            
            if data == None or data == "": data == "N/A"
 
            newTarefa = Tafera(nome, data)
            inserirdados(conn, newTarefa.nome,newTarefa.data)

            os.system("clear")
            print("Dados inserido com sucesso!")
            time.sleep(5)
            mainpage()

        elif choice == 2:
            removatarefa(conn)
        elif choice == 3:
            loop = False
            os.system('clear')
            print("Desligando...")
            time.sleep(3)
            os.system('clear')
            

mainpage()