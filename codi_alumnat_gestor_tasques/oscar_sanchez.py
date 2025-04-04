def eliminar_tasca():
    """Permet eliminar una tasca per ID."""
    id = input("Quina tasca vols eliminar? ")

    try:
        cursor.execute("DELETE FROM gestor_tasques WHERE id = %s", (id,))
        conn.commit()
        print("Tasca eliminada correctament.")
    except Exception as e:
        print(f"Error en eliminar la tasca: {e}")

def modificar_tasques():
    """Modifica el nom i/o la descripció d'una tasca."""
    id = input("Quina tasca vols modificar? ")
    nou_nom = input("Introdueix el nou nom de la tasca: ")
    nova_desc = input("Introdueix la nova descripció de la tasca: ")

    try:
        cursor.execute(
            "UPDATE gestor_tasques SET nom = %s, descripcio = %s WHERE id = %s",
            (nou_nom, nova_desc, id)
        )
        conn.commit()
        print("Tasca modificada correctament.")
    except Exception as e:
        print(f"Error en modificar la tasca: {e}")

def canviar_estat_tasca():
    """Canvia l'estat d'una tasca (pendent/completada)."""
    id = input("Quina tasca vols canviar d'estat? ")
    nou_estat = input("Introdueix el nou estat (pendent/completada): ")

    if nou_estat not in ["pendent", "completada"]:
        print("Valor incorrecte! Només pots triar 'pendent' o 'completada'.")
        return

    try:
        cursor.execute("UPDATE gestor_tasques SET estat = %s WHERE id = %s", (nou_estat, id))
        conn.commit()
        print("Estat de la tasca actualitzat correctament.")
    except Exception as e:
        print(f"Error en modificar l'estat: {e}")

# ────────────────────────────────
# Menú principal
# ────────────────────────────────
def menu():
    while True:
        print("\n💼 GESTOR DE TASQUES")
        print("1. Mostrar tasques")
        print("2. Eliminar tasca")
        print("3. Modificar tasca")
        print("4. Canviar estat tasca")
        print("5. Sortir")
        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            mostrar_tasca()
        elif opcio == "2":
            eliminar_tasca()
        elif opcio == "3":
            modificar_tasques()
        elif opcio == "4":
            canviar_estat_tasca()
        elif opcio == "5":
            print("Sortint del programa...")
            break
        else:
            print("Valor incorrecte, tria una opció vàlida!")

# ────────────────────────────────
# Executar el menú
# ────────────────────────────────
menu()

# Tancar la connexió
cursor.close()
conn.close()