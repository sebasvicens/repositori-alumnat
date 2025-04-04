import mysql.connector



def mostrar_tasques():
    # Executar una consulta SQL
    cursor.execute("SELECT * FROM tasques")

    # Obtenir els resultats
    resultats = cursor.fetchall()
    for fila in resultats:
        mostrar_tasca(fila)


def mostrar_tasca(fila):
    print("*******************")
    print("ID:", fila[0])
    print("Titol", fila[1])
    print("Descripcio", fila[2])
    print("Data inici", fila[3])
    print("Data fi", fila[4])
    print("Estat", fila[5])
    print("Prioritat", fila[6])
    print("*******************")


def eliminar_tasques():
    id = input("ID de la tasca a eliminar: ")
    cursor.execute("DELETE FROM tasques where id =", )
    conn.commit()


def modificar_tasques(id_tasques):
    titol = input("Nou titol")
    descripcio = input ("nova descripcio")
    inici = input ("nova data_inici")
    fi = input ("nova data_fi")
    estat = input ("nou estat")
    prioritat = input ("nova prioritat")

    modificar = "UPDATE tasques Set titol = '" + titol + "', descripcio ='" + descripcio + "', Data_creacio = '" + inici + "' , Data_venciment='" + fi + "' ,Estat = '" + estat + "', Prioritat = '" + prioritat + "' WHERE id = " + id_tasques
    
    cursor.execute (modificar)
    conn.commit()



def menu ():
    while True:
        print ("****** MENU GESTIO DE TASQUES *******")
        print ("1. Mostrar Tasques")
        print ("2.Eliminar Tasca")
        print ("3. Modificar Tasca")
        print ("4. Canviar Estat Tasca")
        print ("5. Sortir")
        opcio = input("")

        if opcio == "1":
            print ("Mostrant les tasques ......")
            mostrar_tasques()
        elif opcio == "2":
            print ("Eliminant la tasca ......") 
        elif opcio == "3":
            print ("Modificant la tasca ......")
            id = input("Quina tasca vols modificar? ") 
            modificar_tasques(id)
        elif opcio == "4":
            print ("Canviant estat de la tasca ......")
        elif opcio == "5":
            print ("Sortint .....") 
            break
        else:
            print ("Valor incorrecte, done'm una opcio correcte capdefava!")


# Connexió a la base de dades
conn = mysql.connector.connect(
    host ="localhost",
    user ="root",
    port = "3307",	
    # password="contrasenya",
    database = "gestor_de_tasques"
)

cursor = conn.cursor()

menu ()

# Tancar la connexió
cursor.close()
conn.close()


    



    