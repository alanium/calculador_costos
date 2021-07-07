import sqlite3

db = sqlite3.connect("costos.db")
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS articulos (id INTEGER PRIMARY KEY,nombre VARCHAR(100) NOT NULL, valor INTEGER NOT NULL)')




def en_desarrollo():

    class Art():

        def __init__(self, nombre, valor, id):
            self.nombre = nombre
            self.valor = valor
            self.id = id
            print(f'se añadio {self.nombre} al catalogo')

        def __str__(self):
            return f'[{self.id}] {self.nombre} {self.valor}'


    class Panel():

        arts = []

        def __init__(self, arts=[]):
            self.arts = arts
        
        def agregar(self, v):
            self.arts.append(v)

        def mostrar(self):
            for v in self.arts:
                print(v)

    # --------------------------------------


def calcular():
    print('--------')
    print('Calcular')
    print('--------')
    print('[1] Ver')
    print('[2] Seleccionar')
    qry_3 = int(input('\n> '))

    while True:
        if qry_3 !=1 and qry_3 !=2:
            qry_3 = int(input('intente nuevamente: '))
        else:
            break
    
    if qry_3 == 1:      # Ver
        cursor.execute('SELECT * FROM articulos')
        usuarios = cursor.fetchall()

        for u in usuarios:
            print(u)
        
        print('\n[1] volver')
        print('[2] salir')
        volver_1 = int(input('> '))
        while True:
            if volver_1 != 1 and volver_1 != 2:
                volver_1 = int(input('intente nuevamente: '))
            else:
                break
        if volver_1 == 1:
            calcular()
        else:
            menu()

    if qry_3 == 2:      # Seleccionar
        lista_0 = []
        
        cursor.execute('SELECT id, nombre FROM articulos')
        ids = cursor.fetchall()
        for v in ids:
            print(v)

        print('ingrese las id de los articulos que desea adquirir, para salir ingrese 0\n')
        a_1 = int(input('> '))
        lista_0.append(a_1)
        while True:
            if a_1 != 0:
                a_1 = int(input('Ingrese otro id o 0 para salir: '))
                if a_1 == 0:
                    break
                else:
                    lista_0.append(a_1)
            else:
                break
        if lista_0 in ids:
            print('estan en la lista')
        else:
            print('no estan')


def panel():
    print('----------------')
    print('Panel de control')
    print('----------------')
    print('[1] Agregar')
    print('[2] Borrar')
    print('[3] Ver')
    print('[4] Volver')
    qry_2 = int(input('\n> '))

    while True:
        if qry_2 !=1 and qry_2 !=2 and qry_2 !=3 and qry_2 !=4:
            qry_2 = int(input('intente nuevamente: '))
        else:
            break
    
    if qry_2 == 1:  # Agregar

        p_1 = input('Nombre del articulo: ')
        p_2 = int(input('Valor: '))
        
        lista_1 = [(p_1, p_2)]

        cursor.executemany('INSERT INTO articulos (nombre, valor) VALUES(?, ?)', lista_1)
        db.commit()
        print(f'Se ha agregado el articulo {p_1}')
        panel()

    elif qry_2 == 2:    # Borrar
        print('Ingrese id que desea borrar')
        id_borrar = input('> ')
        borrar = ("DELETE FROM articulos WHERE id='"+str(id_borrar)+"'")
        cursor.execute(borrar)
        db.commit()
        print(f'Se ha borrado el articulo')
        panel()

    elif qry_2 ==3:     # Ver
        cursor.execute('SELECT * FROM articulos')
        usuarios = cursor.fetchall()

        for u in usuarios:
            print(u)
        
        print('\n[1] volver')
        print('[2] salir')
        volver_1 = int(input('> '))
        while True:
            if volver_1 != 1 and volver_1 != 2:
                volver_1 = int(input('intente nuevamente: '))
            else:
                break
        if volver_1 == 1:
            panel()
        else:
            menu()

    else:
        menu()

def menu():
    print('--------------------')
    print('Calculador de costos ')
    print('--------------------')
    print('[1] Calcular')
    print('[2] Panel de control')
    print('[3] Salir')
    qry = int(input('\n> '))

    while True:
        if qry !=1 and qry !=2 and qry !=3:
            qry = int(input('intente nuevamente: '))
        else:
            break
    
    if qry == 1:
        calcular()
    elif qry == 2:
        panel()

menu()

db.close()


