""" Numeric BH: Conversión de bases numéricas: Binario y Hexadecimal """

from conexion import guardar_conversion, obtener_historial

# Decimal a Binario


def decimal_a_binario(num_dec):
    """ Función para la conversión de Decimal a Binario """
    residuos = []

    if num_dec == 0:
        return print("Resultado: 0")

    while num_dec > 0:
        cociente = num_dec // 2
        residuo = num_dec % 2
        residuos.append(residuo)
        num_dec = cociente

    resultado = "".join([str(residuo) for residuo in residuos[::-1]])

    return resultado

# Binario a Decimal


def binario_a_decimal(num_bin):
    """ Función para la conversión de Binario a Decimal """
    resultado = 0
    for digito in str(num_bin):
        resultado = (resultado * 2) + int(digito)

    return resultado

# Decimal a Hexadecimal


def decimal_a_hexadecimal(num_dec):
    """ Función para la conversión de Decimal a Hexadecimal """
    letras = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    residuos = []

    if num_dec == 0:
        return print("Resultado: 0")

    while num_dec > 0:
        cociente = num_dec // 16
        residuo = num_dec % 16

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

    resultado = "".join([str(residuo) for residuo in residuos[::-1]])
    return resultado

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

    return resultado

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
                    tipo = "Decimal a Binario"
                    numero = int(input("Ingrese cualquier número de base decimal: "))
                    resultado = decimal_a_binario(numero)

                elif tipo_conversion == "2":
                    tipo = "Binario a Decimal"
                    numero = int(input("Ingrese cualquier número de base binaria: "))
                    resultado = binario_a_decimal(numero)

                elif tipo_conversion == "3":
                    tipo = "Decimal a Hexadecimal"
                    numero = int(input("Ingrese cualquier número de base decimal: "))
                    resultado = decimal_a_hexadecimal(numero)

                elif tipo_conversion == "4":
                    tipo = "Hexadecimal a Decimal"
                    numero = str(input("Ingrese cualquier número de base hexadecimal: "))
                    resultado = hexadecimal_a_decimal(numero)

                elif tipo_conversion == "5":
                    print("Volviendo al menú principal...")
                    break

                else:
                    print("Opción inválida. Intente nuevamente")
                    continue

                print(f"El resultado es: {resultado}")

                if tipo_conversion in ["1", "2", "3", "4"]:
                    guardar_conversion(tipo, str(numero), str(resultado))

        elif opcion == "2":
            registros = obtener_historial()
            for registro in registros:
                print(f"{registro[0]} | {registro[1]} | {registro[2]} | {registro[3]}")
            continue

        elif opcion == "3":
            print("Muchas gracias por usar Numeric BH :D")
            print("¡Hasta pronto!")
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
            print()


menu_principal()
