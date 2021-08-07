mensajes = {
    "INGRESAR_CORREO": "Ingrese su correo electrónico: ",
    "REINGRESAR_CORREO": "Reingrese su correo electrónico: ",
    "CORREO_INVALIDO": "No fue posible comprobar su correo electrónico. Vuelva a intentarlo más tarde.",
    "INGRESAR_OPCION": "Ingrese una opción para continuar: ",
    "TITULO_MENU": " Biblioteca ",
    "COLUMNA_OPCION": "Opción",
    "COLUMNA_DESCRIPCION": "Descripción",
    "SEPARADOR_MENU": "____________________________",
    "BIENVENIDA_MENU": "Bienvenido/a, ",
    "DESPEDIDA_MENU": "Hasta pronto,",
    "REINGRESAR_OPCION": "Por favor, reingrese una opción: ",
    "INGRESAR_COLUMNA": "Ingrese el nombre de la columna que desea modificar: ",
    "INGRESAR_VALOR_COLUMNA": "Ingrese el nuevo valor: ",
    "INGRESAR_CONDICION": "Ingrese la columna por la que desea filtrar: ",
    "INGRESAR_VALOR_CONDICION": "Ingrese el valor del filtro: ",
    "REGISTROS_AFECTADOS": "Cantidad de registros afectados: ",
    "CONTINUAR_OPERACION": "Desea repetir el tipo de operación? (s/n): ",
    "EXPORTAR_RESULTADOS": "Desea exportar los resultados? (s/n): ",
    "SIN_RESULTADOS": "No se han encontrado resultados.",
    "ERROR_QUERY": "Se ha encontrado un error en la ejecución de la query: ",
    "ERROR_INSERT": "Año y stock no pueden estar vacíos y deben ser números enteros.",
    "INGRESO_INSERT": "Ingrese el valor para {columna}: ",
    "SERVIDOR_APAGADO": "El servidor MySQL se encuentra apagado. Ejecute el servicio y vuelva a intentarlo.",
    "VALUE_ERROR_MENU": "Reintente ingresando un valor numérico."}

opciones_menu = {1: "Ingresar Libro", 2: "Eliminar Libro", 3: "Modificar Libro", 4: "Consultar Libro",
                 5: "Cambiar de Cuenta", 6: "Salir"}

queries = {
    "INSERTAR_LIBRO": "INSERT INTO libros (isbn, titulo, autor, ano_publicacion, editorial, idioma, formato, stock, "
                      "creado_por, hora_creacion, modificado_por, hora_modificacion) "
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, now(), %s, now())",
    "MODIFICAR_LIBRO": "UPDATE libros SET {columna_nueva} = '{valor_nuevo}', modificado_por = '{email}', "
                       "hora_modificacion = NOW() WHERE {columna_condicion} = '{valor_condicion}'",
    "BORRAR_LIBRO": "DELETE FROM libros WHERE {columna} = '{valor}'",
    "CONSULTAR_LIBRO": "SELECT * FROM libros WHERE {columna} = '{valor}'",
    "DROP_BASE": "DROP DATABASE IF EXISTS biblioteca",
    "CREAR_BASE": "CREATE DATABASE biblioteca",
    "USAR_BASE": "USE biblioteca",
    "CREAR_TABLA": "CREATE TABLE libros (idlibros int NOT NULL AUTO_INCREMENT, isbn varchar(45) CHARACTER SET "
                   "utf8mb4 DEFAULT NULL, titulo varchar(250) CHARACTER SET utf8mb4 DEFAULT NULL, autor varchar(250) "
                   "CHARACTER SET utf8mb4 DEFAULT NULL, ano_publicacion int DEFAULT NULL, editorial varchar(45) "
                   "CHARACTER SET utf8mb4 DEFAULT NULL, idioma varchar(45) CHARACTER SET utf8mb4 DEFAULT NULL, "
                   "formato varchar(45) CHARACTER SET utf8mb4 DEFAULT NULL, stock int DEFAULT '1', creado_por "
                   "varchar(250) CHARACTER SET utf8mb4 DEFAULT NULL, hora_creacion timestamp NULL DEFAULT NULL, "
                   "modificado_por varchar(250) CHARACTER SET utf8mb4 DEFAULT NULL, hora_modificacion timestamp NULL "
                   "DEFAULT NULL, PRIMARY KEY (idlibros)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"}
