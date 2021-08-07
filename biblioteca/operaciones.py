import mysql.connector

from config.datos import mensajes, queries
import csv


def modificar_libro(email, cursor, conexion):
    continuar = "s"

    while continuar == "s":
        nueva_columna = input(mensajes["INGRESAR_COLUMNA"])
        nuevo_valor = input(mensajes["INGRESAR_VALOR_COLUMNA"])
        columna_condicion = input(mensajes["INGRESAR_CONDICION"])
        valor_condicion = input(mensajes["INGRESAR_VALOR_CONDICION"])
        datos = (nueva_columna, nuevo_valor, email, columna_condicion, valor_condicion)

        try:

            cursor.execute(
                queries["MODIFICAR_LIBRO"].format(columna_nueva=datos[0], valor_nuevo=datos[1], email=datos[2],
                                                  columna_condicion=datos[3], valor_condicion=datos[4]))
            conexion.commit()

            print(mensajes["REGISTROS_AFECTADOS"], cursor.rowcount)
            continuar = input(mensajes["CONTINUAR_OPERACION"])

        except mysql.connector.Error as error:
            print(mensajes["SEPARADOR_MENU"], "Se ha encontrado un error en la ejecución de la query: " + str(error),
                  "Error Code: " + str(error.errno), "SQLSTATE: " + error.sqlstate, "Message: " + error.msg,
                  mensajes["SEPARADOR_MENU"], sep="\n")

            continuar = input(mensajes["CONTINUAR_OPERACION"])

        except mysql.connector.errors.DataError as error:
            print(mensajes["SEPARADOR_MENU"], mensajes["ERROR_QUERY"] + str(error),
                  "Error Code: " + str(error.errno), "SQLSTATE: " + error.sqlstate, "Message: " + error.msg,
                  mensajes["SEPARADOR_MENU"], sep="\n")
            continuar = input(mensajes["CONTINUAR_OPERACION"])


def eliminar_libro(cursor, conexion):
    continuar = "s"

    while continuar == "s":
        columna_condicion = input(mensajes["INGRESAR_CONDICION"])
        valor_condicion = input(mensajes["INGRESAR_VALOR_CONDICION"])
        datos = (columna_condicion, valor_condicion)

        try:

            cursor.execute(queries["BORRAR_LIBRO"].format(columna=datos[0], valor=datos[1]))
            conexion.commit()

            print(mensajes["REGISTROS_AFECTADOS"], cursor.rowcount)
            continuar = input(mensajes["CONTINUAR_OPERACION"])

        except mysql.connector.Error as error:
            print(mensajes["SEPARADOR_MENU"], "Se ha encontrado un error en la ejecución de la query: " + str(error),
                  "Error Code: " + str(error.errno), "SQLSTATE: " + error.sqlstate, "Message: " + error.msg,
                  mensajes["SEPARADOR_MENU"], sep="\n")

            continuar = input(mensajes["CONTINUAR_OPERACION"])


def ingresar_libro(cursor, conexion, email):
    continuar = "s"

    while continuar == "s":
        columnas = ["isbn", "titulo", "autor", "ano_publicacion", "editorial", "idioma", "formato", "stock"]
        valores = []

        for columna in columnas:
            valores.append(input(mensajes["INGRESO_INSERT"].format(columna=columna)))

        try:

            datos = (
                valores[0], valores[1], valores[2], int(valores[3]), valores[4], valores[5], valores[6],
                int(valores[7]), email, email)

            cursor.execute(queries["INSERTAR_LIBRO"], datos)

            conexion.commit()

            print(mensajes["REGISTROS_AFECTADOS"], cursor.rowcount)
            continuar = input(mensajes["CONTINUAR_OPERACION"])

        except ValueError:
            print(mensajes["ERROR_INSERT"])
            continuar = input(mensajes["CONTINUAR_OPERACION"])

        except mysql.connector.errors.DataError as error:
            print(mensajes["SEPARADOR_MENU"], mensajes["ERROR_QUERY"] + str(error),
                  "Error Code: " + str(error.errno), "SQLSTATE: " + error.sqlstate, "Message: " + error.msg,
                  mensajes["SEPARADOR_MENU"], sep="\n")
            continuar = input(mensajes["CONTINUAR_OPERACION"])


def consultar_libro(cursor):
    continuar = "s"

    while continuar == "s":
        columna_condicion = input(mensajes["INGRESAR_CONDICION"])
        valor_condicion = input(mensajes["INGRESAR_VALOR_CONDICION"])
        datos = (columna_condicion, valor_condicion)

        try:
            cursor.execute(
                queries["CONSULTAR_LIBRO"].format(columna=datos[0], valor=datos[1]))
            resultado = cursor.fetchall()
            columnas = cursor.column_names

            if len(resultado) > 0:

                for columna in columnas:
                    print("{:^8}".format(columna), end=" • ")
                print("\n")

                for fila in resultado:
                    for columna in fila:
                        print(columna, end=" • ")
                    print("\n")

                guardar_resultado = input(mensajes["EXPORTAR_RESULTADOS"])

                if guardar_resultado == "s":
                    with open('../archivos/resultados.csv', 'w', newline='',
                              encoding='ISO-8859-1') as exportar_resultados:
                        escritura = csv.writer(exportar_resultados)

                        escritura.writerow(columnas)
                        escritura.writerows(resultado)
            else:
                print(mensajes["SIN_RESULTADOS"])

            continuar = input(mensajes["CONTINUAR_OPERACION"])

        except mysql.connector.Error as error:
            print(mensajes["SEPARADOR_MENU"], mensajes["ERROR_QUERY"] + str(error),
                  "Error Code: " + str(error.errno), "SQLSTATE: " + error.sqlstate, "Message: " + error.msg,
                  mensajes["SEPARADOR_MENU"], sep="\n")

            continuar = input(mensajes["CONTINUAR_OPERACION"])
