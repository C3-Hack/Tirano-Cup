import sqlite3
#========================================
#テストデータ
projectname = "MTKirara"
person = ['Akata','Naga','GAN']
todo = "make"
count = 1
#========================================

con = sqlite3.connect('td.db')
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS td_list(ProjectName,TODO_ID,member)''')

#todo_ID = lambda c: chr(c+64)
#todo_ID(count)
todo_ID = "A"
member = ','.join(person)    

c.execute("INSERT INTO td_list VALUES(?,?,?)",[projectname,todo_ID,member])
con.commit()
con.close()