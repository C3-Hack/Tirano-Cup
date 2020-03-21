import sqlite3
    
class Create_TODO_Table:
    def __init__(self):
        con = sqlite3.connect('TODO.db')
        c = con.cursor()
        c.execute('create table if not exists TODO(ProjectName,TODO_ID,TODO,member1,member2,member3,member4,member5)')
        con.commit()
        con.close()

class Add_TODO:
    def __init__(self,person1,person2,person3,person4,person5,todo):
        con = sqlite3.connect('TODO.db')
        c = con.cursor()
        TODO_ID = lambda c: chr(c+64)
        c.execute('insert into TODO values (?,?,?,?,?,?,?,?)')
        todojob = (ProjectName,TODO_ID,todo,person1,person2,person3,person4,person5)
        con.commit()
        con.close()

Create_TODO_Table()

ProjectName="MTKirara"
person = ['Akata','Naga','GAN','','']
todo = "Make make make"

Add_TODO(*person,todo)