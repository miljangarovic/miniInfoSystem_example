from models import Grad, Fakultet,Profesori,Zvanje
import sqlite3

conn = sqlite3.connect('mini-info-sistem.db')
c = conn.cursor()

grad1 = Grad(1, 'Podgorica')
grad2 = Grad(2, 'Niksic')


fakultet1 = Fakultet(1, 'ETF', grad1.id)
fakultet2 = Fakultet(2, 'Filozovski', grad2.id)

zvanje=Zvanje(1,'Redovni Profesor')
profesor=Profesori(123456,'Marko Markovic',zvanje.naziv)


grad1.addToDatabase()
grad2.addToDatabase()
fakultet2.addToDatabase()
fakultet1.addToDatabase()
zvanje.addToDatabase()
profesor.addToDatabase()

c.execute('SELECT * FROM gradovi')

print(c.fetchone())


conn.commit()
conn.close()
