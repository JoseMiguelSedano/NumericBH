""" Numeric BH: Conversión de bases numéricas """

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


# Menú Principal


def menu_principal():
    """ Función para el menú principal """
    while True:
        print()
        print("<<< NUMERIC BH >>>")
        print("Bienvenido al sistema de Numeric BH")
        print("1. Conversión de bases numéricas")
        print("2. Ver historial")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
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


menu_principal()
