import sqlite3

class Grad():

    def __init__(self,id,naziv):
        self.id=id
        self.naziv=naziv

    def addToDatabase(self):
        conn = sqlite3.connect('mini-info-sistem.db')
        c = conn.cursor()
        c.executemany('''
        INSERT INTO gradovi VALUES (?,?);
        ''',[(self.id,self.naziv)])
        conn.commit()
        conn.close()

class Smjer():

    def __init__(self,id,naziv,fakultet_id):
        self.id=id
        self.naziv=naziv
        self.fakultet_id=fakultet_id

    def addToDatabase(self):
        conn = sqlite3.connect('mini-info-sistem.db')
        c = conn.cursor()
        c.executemany('''
        INSERT INTO Smjer VALUES (?,?,?);
        ''',[(self.id,self.naziv,self.fakultet_id)])
        conn.commit()
        conn.close()


class Fakultet():

    def __init__(self, id, naziv, grad_id):
        self.id = id
        self.naziv = naziv
        self.grad_id = grad_id

    def addToDatabase(self):
        conn = sqlite3.connect('mini-info-sistem.db')
        c = conn.cursor()
        c.executemany('''
        INSERT INTO Fakulteti VALUES (?,?,?);
        ''',[(self.id,self.naziv,self.grad_id)])
        conn.commit()
        conn.close()

class Profesori():

    def __init__(self, jmbg, ime, zvanje_id):
        self.jmbg = jmbg
        self.ime = ime
        self.zvanje_id = zvanje_id

    def addToDatabase(self):
        conn = sqlite3.connect('mini-info-sistem.db')
        c = conn.cursor()
        c.executemany('''
        INSERT INTO Profesori VALUES (?,?,?);
        ''',[(self.jmbg,self.ime,self.zvanje_id)])
        conn.commit()
        conn.close()

class Predmeti():

    def __init__(self, id, naziv, smjer_id, saradnik_jmbg, profesor_jmbg):
        self.id = id
        self.naziv = naziv
        self.smjer_id = smjer_id
        self.saradnik_jmbg=saradnik_jmbg
        self.profesor_jmbg=profesor_jmbg

    def addToDatabase(self):
        conn = sqlite3.connect('mini-info-sistem.db')
        c = conn.cursor()
        c.executemany('''
        INSERT INTO Predmeti VALUES (?,?,?,?,?);
        ''',[(self.id,self.naziv,self.smjer_id,self.saradnik_jmbg,self.profesor_jmbg)])
        conn.commit()
        conn.close()


class Saradnici():

    def __init__(self, jmbg, ime):
        self.jmbg = jmbg
        self.ime = ime

    def addToDatabase(self):
        conn = sqlite3.connect('mini-info-sistem.db')
        c = conn.cursor()
        c.executemany('''
        INSERT INTO Saradnici VALUES (?,?);
        ''',[(self.jmbg,self.ime)])
        conn.commit()
        conn.close()

class Zvanje():

    def __init__(self,id,naziv):
        self.id=id
        self.naziv=naziv

    def addToDatabase(self):
        conn = sqlite3.connect('mini-info-sistem.db')
        c = conn.cursor()
        c.executemany('''
        INSERT INTO zvanje VALUES (?,?);
        ''',[(self.id,self.naziv)])
        conn.commit()
        conn.close()


class Studenti():

    def __init__(self, jmbg, ime, br_index):
        self.jmbg = jmbg
        self.ime = ime
        self.br_index = br_index

    def addToDatabase(self):
        conn = sqlite3.connect('mini-info-sistem.db')
        c = conn.cursor()
        c.executemany('''
        INSERT INTO Studenti VALUES (?,?,?);
        ''',[(self.jmbg,self.ime,self.br_index)])
        conn.commit()
        conn.close()


