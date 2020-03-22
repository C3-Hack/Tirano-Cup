import sqlite3

class ConnectDB:
    def __init__(self,root,tip):
        con = sqlite3.connect('../DB/nodes.db')
        c = con.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS nodes(start, end);''')
        c.execute("INSERT INTO nodes VALUES(?,?)",[root,tip])
        con.commit()
        con.close()
