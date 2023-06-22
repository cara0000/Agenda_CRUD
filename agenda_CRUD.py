import mysql.connector;

base_datos = mysql.connector.connect(
  host="localhost",
  user="root",
  password="barTT3nd3rNO.04"
)
mi_cursor = base_datos.cursor()

mi_cursor.execute("SHOW DATABASES")
bases_de_datos_existentes = mi_cursor.fetchall()

if ('agenda0000',) not in bases_de_datos_existentes:
    mi_cursor.execute("CREATE DATABASE agenda0000")
    mi_cursor.execute("use agenda0000") 
    print("BD 'agenda0000' creada y designada.")

    mi_cursor.execute("CREATE TABLE contactos (id int primary key auto_increment, nombre VARCHAR(40), apellido VARCHAR(40), telefono int, mail VARCHAR(40), direccion VARCHAR(40))")
    print("Tabla 'contactos' creada.")

    insertar_datos = "INSERT INTO contactos (nombre, apellido, telefono, mail, direccion) VALUES (%s, %s, %s, %s, %s)"
    registros = [
        ('Björk', '', 1123, 'allisfulloflove@gmail.com', 'Pluto 09'),
        ('Tove', 'Lo', 1154, 'dirtfemme@gmail.com', 'Anywhere u go'),
        ('Caroline', 'Polachek', 1124, 'welcometomyisland@gmail.com', 'Minotaur Island'),
        ('Rosalia', '', 1223, 'motomami@gmail.com', 'Los Santos'),
        ('Charli', 'XCX', 1125, 'itscharlibaby@gmail.com', 'Paradise'),
    ]
    mi_cursor.executemany(insertar_datos, registros)
    base_datos.commit()
    print(mi_cursor.rowcount, "registros insertados.")

else:
    print("La BD agenda0000 ya esta creada y se encuentra designada.")
    mi_cursor.execute("use agenda0000")

class Agenda:

    def mostrar_menu(self):
        menu= '''Agenda POO
        1. Crear nuevo contacto
        2. Buscar contacto
        3. Editar contacto
        4. Borrar contacto
        5. Mostrar lista de contactos
        6. Salir
        '''
        print(menu)
    
    def ingresar_opcion(self):
        opc= int(input("Ingrese el número de opción elegida: "))
        return opc

    def registrar_contacto(self):
        insertar_datos = "INSERT INTO contactos (nombre, apellido, telefono, direccion, mail) VALUES (%s, %s, %s, %s, %s)"
        nombre= input("Ingrese el nombre del contacto: ")
        apellido= input("Ingrese el apellido del contacto: ")
        telefono= input("Ingrese el número de teléfono del contacto: ")
        direccion= input("Ingrese la dirección del contacto: ")
        email= input("Ingrese el mail del contacto: ")
        valores = (nombre, apellido, telefono, direccion, email)
        mi_cursor.execute(insertar_datos, valores)
        base_datos.commit()
        print("Contacto registrado.")

    def mostrar_contactos_por_nombre(self):
        print("----------------------------------------------")
        print("CONTACTOS ORDENADOS ALFABETICAMENTE POR NOMBRE: ")
        consulta_mostrar_datos= "SELECT * FROM contactos ORDER BY nombre"
        mi_cursor.execute(consulta_mostrar_datos)
        tabla_contactos = mi_cursor.fetchall()
        for contacto in tabla_contactos:
            self.imprimir_datos_contacto(contacto)

    def mostrar_contactos_por_apellido(self):
        print("------------------------------------------------")
        print("CONTACTOS ORDENADOS ALFABETICAMENTE POR APELLIDO: ")
        consulta_mostrar_datos= "SELECT * FROM contactos ORDER BY apellido"
        mi_cursor.execute(consulta_mostrar_datos)
        tabla_contactos = mi_cursor.fetchall()
        for contacto in tabla_contactos:
            self.imprimir_datos_contacto(contacto)

    def buscar_contacto(self,opc):
        if opc == 1:
            consulta= "SELECT * FROM contactos WHERE nombre = %s"
            nombre= input("Ingresar el nombre del contacto buscado: ")
            print("Resultados para el nombre",nombre+": ")
            print("------------------------------------------------")
            mi_cursor.execute(consulta, (nombre,))
            resultado_nombres = mi_cursor.fetchall()
            if len(resultado_nombres) > 0:
                for contacto in resultado_nombres:
                    self.imprimir_datos_contacto(contacto)
            else:
                print("El nombre buscado no esta registrado en la base de datos.")
        if opc == 2:
            consulta= "SELECT * FROM contactos WHERE apellido = %s"
            apellido= input("Ingresar el apellido del contacto buscado: ")
            print("Resultados para el apellido '"+apellido+"': ")
            print("------------------------------------------------")
            mi_cursor.execute(consulta, (apellido,))
            resultados_apellido = mi_cursor.fetchall()
            if len(resultados_apellido) > 0:
                for contacto in resultados_apellido:
                    self.imprimir_datos_contacto(contacto)
            else:
                print("El apellido buscado no esta registrado en la base de datos.")            
        if opc == 3:
            consulta= "SELECT * FROM contactos WHERE id = %s"
            id= int(input("Ingresar el ID del contacto buscado: "))
            print("Resultados para el ID",str(id)+": ")
            print("------------------------------------------------")
            mi_cursor.execute(consulta, (id,))
            resultados_id = mi_cursor.fetchall()
            if len(resultados_id) > 0:
                for contacto in resultados_id:
                    self.imprimir_datos_contacto(contacto)
            else:
                print("El ID buscado no esta registrado en la base de datos.")

    def editar_contacto(self):
        consulta= "SELECT * FROM contactos WHERE id = %s"
        id_buscado= input("Ingresar el ID del contacto a editar: ")
        print("Resultados para el ID",id_buscado+": ")
        print("------------------------------------------------")
        mi_cursor.execute(consulta, (id_buscado,))
        resultados_id = mi_cursor.fetchall()
        if len(resultados_id) > 0:
            for contacto in resultados_id:
                self.imprimir_datos_contacto(contacto)
            print("DATOS A EDITAR:\n1. Nombre\n2. Apellido\n3. Teléfono\n4. Email\n5. Direccón")
            dato_a_editar= int(input("Ingrese el número de dato que desea editar: "))
            if dato_a_editar == 1:
                nombre= input("Ingrese el nuevo nombre de contacto: ")
                actualizar_datos = "UPDATE contactos SET nombre = %s WHERE id = %s"
                valores = (nombre, id_buscado)
                mi_cursor.execute(actualizar_datos, valores)
                base_datos.commit()
                print("Nombre de contacto editado.")
            if dato_a_editar == 2:
                apellido= input("Ingrese el nuevo apellido de contacto: ")
                actualizar_datos = "UPDATE contactos SET apellido = %s WHERE id = %s"
                valores = (apellido, id_buscado)
                mi_cursor.execute(actualizar_datos, valores)
                base_datos.commit()
                print("Apellido de contacto editado.")
            if dato_a_editar == 3:
                telefono= input("Ingrese el nuevo teléfono de contacto: ")
                actualizar_datos = "UPDATE contactos SET telefono = %s WHERE id = %s"
                valores = (telefono, id_buscado)
                mi_cursor.execute(actualizar_datos, valores)
                base_datos.commit()
                print("Teléfono de contacto editado.")
            if dato_a_editar == 4:
                mail= input("Ingrese el nuevo email de contacto: ")
                actualizar_datos = "UPDATE contactos SET mail = %s WHERE id = %s"
                valores = (mail, id_buscado)
                mi_cursor.execute(actualizar_datos, valores)
                base_datos.commit()
                print("Email de contacto editado.")
            if dato_a_editar == 5:
                direccion= input("Ingrese la nueva dirección de contacto: ")
                actualizar_datos = "UPDATE contactos SET direccion = %s WHERE id = %s"
                valores = (direccion, id_buscado)
                mi_cursor.execute(actualizar_datos, valores)
                base_datos.commit()
                print("Dirección de contacto editado.")
            if dato_a_editar > 5 and dato_a_editar < 1:
                print("Opción inválida.")
        else:
            print("El ID buscado no esta registrado en la base de datos.")

    def borrar_contacto(self):
        consulta= "SELECT * FROM contactos WHERE id = %s"
        id_buscado= input("Ingresar el ID del contacto que desea borrar: ")
        print("Resultados para el ID",id_buscado+": ")
        print("------------------------------------------------")
        mi_cursor.execute(consulta, (id_buscado,))
        resultados_id = mi_cursor.fetchall()
        if len(resultados_id) > 0:
            for contacto in resultados_id:
                self.imprimir_datos_contacto(contacto)
            borrar= input("Delete Forever.wav\ns/n: ")
            if borrar == "s":
                consulta_borrar = "DELETE FROM contactos WHERE id = %s"
                mi_cursor.execute(consulta_borrar, (id_buscado,))
                base_datos.commit()
                print("Registro borrado.")
            else:
                print("Operación cancelada.")
        else:
            print("No existen registros para el ID buscado.")

    def imprimir_datos_contacto(self,i):
        print("ID:",i[0])
        print("Nombre:",i[1])
        print("Apellido:",i[2])
        print("Teléfono:",i[3])
        print("Mail:",i[4])
        print("Dirección:",i[5])
        print("------------------------------------------------")

#main
agenda0000= Agenda()
opc= 1
while opc < 6:
    agenda0000.mostrar_menu()
    opc= agenda0000.ingresar_opcion()
    if opc == 1:
        agenda0000.registrar_contacto()
    if opc == 2:
        opc2= int(input("Buscar contacto por...\n1.Nombre\n2.Apellido\n3.ID\nIngresar número de opción elegida: "))
        agenda0000.buscar_contacto(opc2)
    if opc == 3:
        agenda0000.editar_contacto()
    if opc == 4:
        agenda0000.borrar_contacto()
    if opc == 5:
        opc5= int(input("Mostrar contactos ordenados por:\n1. Nombre\n2. Apellido\nIngresar opción: "))
        print(opc5)
        if opc5 == 1:
            agenda0000.mostrar_contactos_por_nombre()               
        if opc5 == 2:
            agenda0000.mostrar_contactos_por_apellido()
print("¡Gracias por utilizar el software!")