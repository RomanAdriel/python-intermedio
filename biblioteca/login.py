import re

from config.datos import mensajes, opciones_menu
from config.conector_db import ConectorDB
from biblioteca.operaciones import Operaciones

cursor, conexion = ConectorDB().crear_cursor()


class Login:

    def login(self):
        email = input(mensajes["INGRESAR_CORREO"])
        patron = re.compile(r'\b([a-z0-9._]{0,25})+(@+([a-z.]{1,30})+\.[a-z]{2,8})\b')
        email_validado = "No"
        contador = 0

        while contador < 3 and email_validado == "No":
            if not re.match(patron, email) and contador < 2:
                email = input(mensajes["REINGRESAR_CORREO"])
                contador += 1
            elif not re.match(patron, email) and contador == 2:
                contador += 1
            else:
                email_validado = "Valido"
        return email, email_validado

    def cambiar_cuenta(self):
        cuenta = self.login()
        if cuenta[1] != "Valido":
            cuenta = ('', 'No')
        return cuenta

    def imprimir_menu(self):
        print(mensajes["SEPARADOR_MENU"],
              "{:^10}" "{:^17}".format(mensajes["COLUMNA_OPCION"], mensajes["COLUMNA_DESCRIPCION"]),
              mensajes["SEPARADOR_MENU"], sep="\n")
        for key, value in opciones_menu.items():
            print("{:^10} {:@^5}".format(key, value))

    def validar_ingreso(self):
        salida = 0
        while salida == 0:
            try:
                menu_ingreso = int(input(mensajes["INGRESAR_OPCION"]))
                salida += 1
                return menu_ingreso
            except ValueError:
                print(mensajes["VALUE_ERROR_MENU"])

    def menu(self, email_validez):
        if email_validez[1] != "No":
            email = email_validez[0]
            usuario = email[:email.index("@")]
            print("\n{:#^38}".format(mensajes["TITULO_MENU"]), mensajes["BIENVENIDA_MENU"] + usuario + ".", sep="\n")
            self.imprimir_menu()
            opcion_ingresada = self.validar_ingreso()
            menu_var = 0
            while menu_var == 0:
                if opcion_ingresada in opciones_menu.keys():
                    if opcion_ingresada == 1:
                        Operaciones().ingresar_libro(cursor, conexion, email)

                    elif opcion_ingresada == 2:
                        Operaciones().eliminar_libro(cursor, conexion)

                    elif opcion_ingresada == 3:
                        Operaciones().modificar_libro(email, cursor, conexion)

                    elif opcion_ingresada == 4:
                        Operaciones().consultar_libro(cursor)

                    elif opcion_ingresada == 5:
                        cambio_email = self.cambiar_cuenta()
                        if cambio_email[1] != "No":
                            email = cambio_email[0]
                            usuario = email[:email.index("@")]

                    elif opcion_ingresada == 6:
                        print(mensajes["DESPEDIDA_MENU"], usuario)
                        menu_var = 1

                    opcion_ingresada = 0
                else:
                    self.imprimir_menu()
                    opcion_ingresada = self.validar_ingreso()

        else:
            print(mensajes["CORREO_INVALIDO"])
