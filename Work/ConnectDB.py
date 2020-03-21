import sqlite3

class ConnectDB:
    def __init__(self,root,tip):
        con = sqlite3.connect('connect.db')
        c = con.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS td_list(start,end)''')
        c.execute("INSERT INTO td_list VALUES(?,?)",[root,tip])
        con.commit()
        con.close()
