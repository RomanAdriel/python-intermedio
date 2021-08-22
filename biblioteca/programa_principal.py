from biblioteca.login import Login
from config.conector_db import ConectorDB

if __name__ == '__main__':

    ConectorDB().crear_db()
    ConectorDB().rellenar_db()
    email_validado = Login().login()
    Login().menu(email_validado)
