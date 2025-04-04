import mysql.connector

def canviar_estat_tasques():

    id = input("Quina tasca vols actualitzar? ")
    query_select_tasks = "SELECT * FROM tasklist WHERE ID = " + id

    # Executa una consulta SQl
    cursor.execute(query_select_tasks)

    # Obtenir els resultats
    resultats = cursor.fetchall()
    for fila in resultats:
        tascaToString(fila)

        query_update_task = "UPDATE tasklist " \
    "SET titol = '" + titol + "', descripcio = '" + descripcio + "', " \
    "data_creacio = '" + creacio + "', data_venciment = '" + venciment + "', " \
    "prioritat = '" + prioritat + "' " \
    "WHERE id = " + id

    cursor.execute(query_update_task)
    conn.commit()
    
    titol = input("Títol: ")
    descripcio = input("Descripció: ")
    creacio = input("Data inici (YYYY-MM-DD): ")
    venciment = input("Data tancament (YYYY-MM-DD): ")
    prioritat = input("Prioritat: ")



def afegir_tasques():
    titol = input("Títol: ")
    descripcio = input("Descripció: ")
    creacio = input("Data inici (YYYY-MM-DD): ")
    venciment = input("Data tancament (YYYY-MM-DD): ")
    estat = input("Estat: ")
    prioritat = input("Prioritat: ")
    
    x = "INSERT INTO tasques (titol, descripcio, data_creacio, data_venciment, estat, prioritat) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (titol, descripcio, creacio, venciment, estat, prioritat)


    cursor.execute(x, values)
    conn.commit() # Important per desar els canvis

    


def eliminar_tasques():
    # demanar id de tasca a eliminar
    eliminar = input("Quina tasca vols eliminar? ")
    # Executar una consulta SQL
    cursor.execute("DELETE FROM tasques where id = " + eliminar)
    conn.commit()

def mostrar_tasques():
    # Executar una consulta SQL
    print("")
    cursor.execute("SELECT * FROM tasques")

    # Obtenir els resultats
    resultats = cursor.fetchall()

    for fila in resultats:
        print("ID: " + str(fila[0]))
        print("titol: " + str(fila[1]))
        print("descripsio: ", str(fila[2]))
        print("data_cracio: ", str(fila[3]))
        print("estat: ", str(fila[4]))
        print("prioritat: ", str(fila[5]))

def menu():
    while True:
        print("\nMENU GESTOR")
        print("1. mostrar tasques")
        print("2. eliminar tasques")
        print("3. afegir tasques")
        print("4. canviar estat tasques")
        print("5. sortir tasca")
        opcio = input("Que vols crack? ")

        if opcio == "1":
            print("mostrar tasques")
            mostrar_tasques()
        elif opcio == "2":
            print("eliminar tasques")
            eliminar_tasques()
        elif opcio == "3":
            print("afegir tasques")
            afegir_tasques()
        elif opcio == "4":
            print("4. canviar estat tasques")
            canviar_estat_tasques()
        elif opcio == "5":
            print("5. sortir app")
            break
        else:
            print("valor incorrecta tonto")
            

# Connexió a la base de dades
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    port = "3306",	
    # password="contrasenya",
    database="tasques"
)

cursor = conn.cursor()

menu()

# Tancar la connexió
cursor.close()
conn.close()