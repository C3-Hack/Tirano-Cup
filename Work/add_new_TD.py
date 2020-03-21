import sqlite3
#========================================
#テストデータ
projectname = "MTKirara"
#person = ['Akata','Naga','GAN','Hage','Gomi']
person = ['','','','','']
print("p1:")
person[0] = input()
todo = "make"
print("Count:")
count = input()
#========================================

con = sqlite3.connect('td.db')
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS td_list(ProjectName,TODO_ID,TODO,member1,member2,member3,member4,member5)''')

todo_ID = lambda c: chr(c+64)
id = todo_ID(int(count))
#todo_ID = "A"

c.execute("INSERT INTO td_list VALUES(?,?,?,?,?,?,?,?)",[projectname,id,todo,person[0],person[1],person[2],person[3],person[4]])
con.commit()
con.close()