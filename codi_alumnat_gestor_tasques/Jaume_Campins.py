import mysql.connector

# Connexió a la base de dades
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    port = "3307",	
    # password="contrasenya",
    database="gestor_de_tasques"
)

cursor = conn.cursor()


def mostrar_tasques():
    # Executar una consulta SQL
    cursor.execute("SELECT * FROM tasques")

    # Obtenir els resultats
    resultats = cursor.fetchall()
    for fila in resultats:
        print(f"ID: {fila[0]}")
        print(f"Titol: {fila[1]}")
        print(f"Descripcio: {fila[2]}")
        print(f"inici: {fila[3]}")
        print(f"fI: {fila[4]}")
        print(f"Estat: {fila[5]}")
        print(f"Prioritat: {fila[6]}")
        print("**********************")


def eliminar_tasques(id_tasques):
    cursor.execute("DELETE FROM tasques where id=" + id_tasques)

    conn.commit()



def modificar_tasques(id_tasques):
    titol = input("Nou titol: ")
    descripcio = input("nova descripcio: ")
    inici = input("nou inici: ")
    fi = input("nou fi: ")
    estat = input("nou estat: ")
    prioritat = input("nova prioritat: ")
    modificar = "UPDATE tasques Set titol = '" + titol + "',descripcio = '" + descripcio + "',data_creacio = '" + inici + "' ,data_venciment ='" + fi + "' ,estat  = '" + estat + "', prioritat ='" + prioritat + "' WHERE id = " +id_tasques
    
    cursor.execute(modificar)
    conn.commit()





def menu_principal ():
    while True:
        print("**********MENU PRINCIPAL**********")
        print("1. mostrar tasques")
        print("2. modificar tasques")
        print("3. eliminar tasques")
        print("4. sortir")

        opcio = input("Quina opcio vols? ")

        if opcio == "1":
            print("mostrant tasques....")
            mostrar_tasques()
        elif opcio == "2":
            print("quina tasca vols modificar?")
            id_tasques = input("")
            modificar_tasques(id_tasques)
        elif opcio == "3":
            print("quina tasca vols eliminar?")
            id_tasques = input("")
            eliminar_tasques(id_tasques)
        elif opcio == "5":
            break

menu_principal()    


            
        

# Tancar la connexió
cursor.close()
conn.close()