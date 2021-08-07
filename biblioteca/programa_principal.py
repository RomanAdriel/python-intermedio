from biblioteca.login import login, menu
from config.conector_db import crear_db, rellenar_db


def main():

    crear_db()
    rellenar_db()
    email_validado = login()
    menu(email_validado)


__init__: main()
