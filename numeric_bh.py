""" Numeric BH: Conversión de bases numéricas """

# Registro de usuario

usuarios_registrados = []


def registro_usuario():
    """ Función para el registro de usuario """
    print()
    print("<<< MENU DE REGISTRO >>")
    correo_usuario = input("Ingrese un correo: ")
    contrasenha_usuario = input("Ingrese una contraseña: ")
    nombre_usuario = input("Ingrese el nombre que desea para su usuario: ")
    usuario = {
        "nombre": nombre_usuario,
        "correo": correo_usuario,
        "contraseña": contrasenha_usuario
    }
    usuarios_registrados.append(usuario)
    print("Registro completado exitosamente!")
    print(f"Nuevo usuario registrado: {usuario['nombre']}")
    return usuario

# Inicio de sesión de usuario


def inicio_sesion_usuario():
    """ Función para el inicio de la sesión del usuario """
    print()
    print("<<< MENU DE INICIO DE SESIÓN >>")
    correo_usuario = input("Ingrese su correo: ")
    contrasenha_usuario = input("Ingrese su contraseña: ")

    for usuario in usuarios_registrados:
        if usuario["correo"] == correo_usuario and usuario["contraseña"] == contrasenha_usuario:
            print(f"Bienvenido, {usuario['nombre']}")
            return usuario

    print("Error: Correo o contraseña incorrectos")

# Decimal a Binario


def decimal_a_binario(num_dec):
    """ Función para la conversión de Decimal a Binario """
    residuos = []
    cociente = None
    while True:
        if cociente != 0:
            cociente = num_dec // 2
            print(f"Cociente: {cociente}")
            residuo = num_dec % 2
            print(f"Residuo: {residuo}")
            print()
            residuos.append(residuo)
            num_dec = cociente
        else:
            print("Se acabo la conversión")
            print(f"El resultado es: {residuos[::-1]}")
            print()
            break

# Binario a Decimal


def binario_a_decimal(num_bin):
    """ Función para la conversión de Binario a Decimal """
    resultado = 0
    for digito in str(num_bin):
        resultado = (resultado * 2) + int(digito)
        print(f"{resultado}")
    print("Se acabo la conversión")
    print(f"El resultado es: {resultado}")
    return resultado

# Decimal a Hexadecimal


def decimal_a_hexadecimal(num_dec):
    """ Función para la conversión de Decimal a Hexadecimal """
    letras = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    residuos = []
    cociente = None

    while True:
        if cociente != 0:
            cociente = num_dec // 16
            print(f"Cociente: {cociente}")
            residuo = num_dec % 16
            print(f"Residuo: {residuo}")
            print()
            if residuo == 10:
                residuo = letras[10]
            elif residuo == 11:
                residuo = letras[11]
            elif residuo == 12:
                residuo = letras[12]
            elif residuo == 13:
                residuo = letras[13]
            elif residuo == 14:
                residuo = letras[14]
            elif residuo == 15:
                residuo = letras[15]
            residuos.append(residuo)
            num_dec = cociente
        else:
            print("Se acabo la conversión")
            print(f"El resultado es: {residuos[::-1]}")
            print()
            break

# Hexadecimal a Decimal


def hexadecimal_a_decimal(num_hexa):
    """ Función para la conversión de Hexadecimal a Decimal """
    letras = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    resultado = 0
    for digito in str(num_hexa).upper():
        if digito == "A":
            digito = letras["A"]
        elif digito == "B":
            digito = letras["B"]
        elif digito == "C":
            digito = letras["C"]
        elif digito == "D":
            digito = letras["D"]
        elif digito == "E":
            digito = letras["E"]
        elif digito == "F":
            digito = letras["F"]
        resultado = (resultado * 16) + int(digito)
        print(f"{resultado}")
    print("Se acabo la conversión")
    print(f"El resultado es: {resultado}")
    return resultado

# Menú Principal


def menu_principal():
    """ Función para el menú principal """
    while True:
        print()
        print("<<< NUMERIC BH >>>")
        print("Bienvenido al sistema de Numeric BH")
        print("1. Registrarse o Iniciar sesión")
        print("2. Conversión de bases numéricas")
        print("3. Ver historial")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            decision = input("¿Desea registrarse(R) o iniciar sesión(I)?: ").upper()
            if decision == "R":
                registro_usuario()
                continue
            if decision == "I":
                inicio_sesion_usuario()
                continue

        if opcion == "2":
            while True:
                print()
                print("Conversión de bases numéricas")
                print("1. Decimal a Binario")
                print("2. Binario a Decimal")
                print("3. Decimal a Hexadecimal")
                print("4. Hexadecimal a Decimal")
                print("5. Salir al menú principal")
                tipo_conversion = input("Ingrese el tipo de conversión que requiere: ")

                if tipo_conversion == "1":
                    numero_decimal = int(input("Ingrese cualquier número de base decimal: "))
                    print()
                    decimal_a_binario(numero_decimal)
                    continue

                if tipo_conversion == "2":
                    numero_binario = int(input("Ingrese cualquier número de base binaria: "))
                    print()
                    binario_a_decimal(numero_binario)
                    continue

                if tipo_conversion == "3":
                    numero_decimal = int(input("Ingrese cualquier número de base decimal: "))
                    print()
                    decimal_a_hexadecimal(numero_decimal)
                    continue

                if tipo_conversion == "4":
                    numero_hexadecimal = str(input("Ingrese cualquier número de base hexadecimal: "))
                    print()
                    hexadecimal_a_decimal(numero_hexadecimal)
                    continue

                if tipo_conversion == "5":
                    print("Volviendo al menú principal...")
                    break

        if opcion == "2":
            return

        if opcion == "3":
            print("Muchas gracias por usar Numeric BH :D")
            print("¡Hasta pronto!")
            print("Saliendo del sistema...")
            break


menu_principal()
