def gestor():
    import mysql.connector
            # Connexió a la base de dades
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        port = "3306",	
        # password="contrasenya",
        database="gestordb"
    )

    cursor = conn.cursor()

    def mostrarTasques():
        
        cursor.execute("SELECT * FROM taula")

        resultats = cursor.fetchall()
        for fila in resultats:
            print("\n *************** Tasca", fila[0], "**************")
            print("ID: ", fila[0])
            print("Títol: ", fila[1])
            print("Descripció: ", fila[2])
            print("Data creació: ", fila[3])
            print("Data venciment: ", fila[4])
            print("Estat: ", fila[5])
            print("Prioritat: ", fila[6])
            

        gestor()
    
    def afegirTasques():

        a = input("títol: ")
        b = input("descripció: ")
        c = input("data de creació (YYYY/MM/DD): ")
        d = input("data de venciment(YYYY/MM/DD): ")
        e = input ("estat: ")
        f = input("prioritat: ")

        tasca = "INSERT INTO taula (titol, descripcio, data_creacio, data_venciment, estat, prioritat) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (a, b, c, d, e, f)

        cursor.execute(tasca, values)
        conn.commit()
        

        gestor()

    def eliminarTasques():

        a = input("ID a eliminar: ")
        cursor.execute("DELETE FROM taula where ID = "+ a)
        
        conn.commit()
        

        gestor()

    def modificarTasques():
        
        id = input("ID de la tasca que vols modificar: ")
        titol = input("Títol: ")
        descripcio = input("Descripció: ")
        data_creacio = input("Data inici (YYYY-MM-DD): ")
        data_venciment = input("Data tancament (YYYY-MM-DD): ")
        estat = input("Estat: ")
        prioritat = input("Prioritat: ")

        modificar_tasca = "UPDATE taula SET titol = '" + titol + "', descripcio = '" + descripcio + "', " "data_creacio ='" + data_creacio + "', data_venciment = '" + data_venciment + "', estat ='" + estat + "', prioritat = '" + prioritat + "' ""WHERE id =" + id

        cursor.execute(modificar_tasca)
        conn.commit()

    print("- - - - - - - - - - - - - - - - - - - -")
    print("Menú gestor")
    print("Mostrar tasques: 1" )
    print("Afegir tasques: 2")
    print("Eliminar tasques: 3")
    print("Modificar tasques: 4")
    print("Sortir: 5")

    n = input("Que vols fer?")
    
    opcions = ["1","2","3","4","5"]
    
    if n not in opcions:
        print("digues una resposta vàlida")
        
        gestor()
    
    elif int(n) == 1:
        mostrarTasques()
        

    elif int(n) == 2:
        afegirTasques()

    elif int(n) == 3:
        eliminarTasques()

    elif int(n) == 4:
        modificarTasques()

    elif int(n) == 5:
        cursor.close()
        conn.close()
        return

gestor()
