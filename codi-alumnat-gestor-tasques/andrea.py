import mysql.connector

def connectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        port="3306",
        database="gestor_tasques"
    )
    
def tancar_connexio(cursor, conn):
    # Tancar la connexió
    cursor.close()
    conn.close()

def tascaToString(tasca):
    print()
    print(f"########## TASCA ID: {tasca[0]} ##########")
    print(f"Titol: {tasca[1]}")
    print(f"Descripcio: {tasca[2]}")
    print(f"Data creacio: {tasca[3]}")
    print(f"Data venciment: {tasca[4]}")
    print(f"Estat: {tasca[5]}")
    print(f"Prioritat: {tasca[6]}")
    print(f"#################################")
    print()

def mostar_tasques():
    # Executar una consulta SQL
    cursor.execute("SELECT * FROM tasques")

    # Obtenir els resultats
    resultats = cursor.fetchall()
    for fila in resultats:
            print("******************************")
            print("ID: ", fila[0])
            print("Titol: ", fila[1])
            print("Descripcio: ", fila[2])
            print("Data inici: ", fila[3])
            print("Data fi: ", fila[4])
            print("Estat: ", fila[5])
            print("Prioritat: ", fila[6])
            print("******************************")

def eliminar_tasca():
    id = input("ID de la tasca a eliminar: ")
    cursor.execute("DELETE FROM tasques WHERE ID = " + id)
    conn.commit()

def modificar_tasca():
    id = input("Quina tasca vols actualitzar? (Insereix l'ID corresponent)")

    query_select_tasks = "SELECT * FROM tasques list WHERE ID = " + id

    # Executa una consulta SQl
    cursor.execute(query_select_tasks)

    # Obtenir els resultats
    resultats = cursor.fetchall()
    for fila in resultats:
        tascaToString(fila)

    titol = input("Títol: ")
    descripcio = input("Descripció: ")
    creacio = input("Data inici (YYYY-MM-DD): ")
    venciment = input("Data tancament (YYYY-MM-DD): ")
    prioritat = input("Prioritat: ")

    query_update_task = "UPDATE tasklist " \
    "SET titol = '" + titol + "', descripcio = '" + descripcio + "', " \
    "data_creacio = '" + creacio + "', data_venciment = '" + venciment + "', " \
    "prioritat = '" + prioritat + "' " \
    "WHERE id = " + id

    cursor.execute(query_update_task)
    conn.commit()

def canviar_estat():
    id = input("ID de la tasca per canviar l'estat: ")

    cursor.execute("SELECT * FROM tasques WHERE ID = " + id)
    tasca = cursor.fetchone()
    if not tasca:
        print("No s'ha trobat la tasca.")
        return
    
    tascaToString(tasca)
    estat = input("Nou estat: ")

    query_update_task = f"UPDATE tasques SET estat = '{estat}' WHERE ID = {id}"
    
    cursor.execute(query_update_task)
    conn.commit()

def menu():
    conn = connectar_db()
    cursor = conn.cursor()

    while True:
        print("******* MENU GESTIO DE TASQUES *******")
        print("1. Mostrar tasques")
        print("2. Eliminar tasques")
        print("3. Modificar tasques")
        print("4. Canviar Estat tasca")
        print("5. Sortir")
        opció = input("")

        if opció == "1":
            print("Mostrant les tasques.......")
            mostar_tasques()
        elif opció == "2":
            print("Eliminant la tasca.......")
            eliminar_tasca()
        elif opció == "3":
            print("Modificant la tasca.......")
            modificar_tasca()
        elif opció == "4":
            print("Canviant estat de la tasca.......")
            canviar_estat()
        elif opció == "5":
            print("Has triat la opció 5. Gràcies per utilitzar l'aplicació")
            break

        else:
            print("L'opció que has triat no és vàlida. Per favor, introdueix una opció vàlida.")

# Connexió a la base de dades
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    port = "3306",	
    # password="contrasenya",
    database="gestor_tasques")

cursor = conn.cursor()

menu()

# Tancar la connexió
cursor.close()
conn.close()