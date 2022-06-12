"""
Created on Tues Jun 2022
@author: Vicgar21
"""
print("Se muestran los ejemplos y forma de programar los temas basicos para la acreditacion PCEP")
def conceptos():
    opciones = input("Ingresa el concepto que quieres ver: "
                     "\na) Variable"
                     "\nb) Asignacion de un nombre a un valor"
                     "\nc) Nombre de variable"
                     "\nd) Indexacion"
                     "\ne) Rebanada o Debanado"
                     "\nf) Rebanada a saltos"
                     "\ng) Mezclar e Intercalar palabras"
                     "\nr) Regresar al menu principal"
                     "\ns) Salir"
                     "\nEleccion: ")
    if opciones.lower() == "a":
        print()
        return "Variable es asignar un espacio en memoria a un valor"
    elif opciones.lower() == "b":
        print()
        return "Aqui se le asigna el nombre num al valor 5, num = 5"
    elif opciones.lower() == "c":
        print()
        return "Los nombres de variables deben empezar con letra o con un guion bajo: _dato = 21"
    elif opciones.lower() == "d":
        print()
        print("Indexacion es la forma en que podemos obtener el valor del indice y se comienza a contar en 0")
        nombre = "Fatima"
        return "La indexacion de la i en el nombre 'Fatima' es: nombre[3],", nombre[3]
    elif opciones.lower() == "e":
        print()
        rebanada = "palabra"
        print("La rebanada de alab sacada de la palabra 'palabra' es: rabanada[1:5],", rebanada[1:5])
        return "El valor 5 no se toma por que ahi se detiene"
    elif opciones.lower() == "f":
        print()
        rebanoasaltos = "SHROGRHCAHNAATHA"
        return "El rebanado con saltos sirve para esto 'SHROGRHCAHNAATHA': rabanoasaltos[1: :2] ", rebanoasaltos[1:0:2]
    elif opciones.lower() == "g":
        def mezclador(string_a, string_b):
            # aquí debes escribir el código de tu programa
            return string_a[0: 2] + string_b[-2:]

        ver = mezclador("HOJLA", "hssdisdu")
        print(ver)

        def intercalar(stringa, stringb):
            return stringb.join(list(stringa)) + stringb

        mou = intercalar("PASO", "R")
        print(mou)

    elif opciones.lower() == "r":
        print()
        print("Regresaste al menu principal")
        menu_principal()
    elif opciones.lower() == "s":
        print("Has pulsado salir, gracias por tu visita")
        return exit()
    else:
        print()
        print("Elegir de nuevo el concepto que quieres ver")
        return conceptos()

def metodos():  #Se trabajan con cadenas de caracteres
    opciones = input("Elige cual metodo quieres ver: \na) Capitalize"
                     "\nb) Lower"
                     "\nc) Upper"
                     "\nd) Title"
                     "\ne) Center"
                     "\nr) Regresar al menu principal"
                     "\ns) Salir"
                     "\nEleccion: ")
    if opciones.lower() == "a":
        print()
        palabra = "fatima"
        return "Se utiliza el metodo capitalize la palabra es 'fatima' con capitalize es: ", palabra.capitalize()
    elif opciones.lower() == "b":
        print()
        palabra = "PYTHON"
        return "Se utiliza el metodo lower la palabra es 'PYTHON' con lower es: ", palabra.lower()
    elif opciones.lower() == "c":
        print()
        palabra = "victor"
        return "Se utiliza el metodo upper la palabra es 'victor' con upper es: ", palabra.upper()
    elif opciones.lower() == "d":
        print()
        palabra = "bIenvenidoS TODOS"
        return "Se utiliza el metodo title la palabra es 'bIenvenidoS TODOS' con title es: ", palabra.title()
    elif opciones.lower() == "e":
        print()
        palabra = "Hola Fatima"
        return "Se utiliza el metodo center la palabra es 'Hola Fatima' con center es: ", palabra.center(50, "=")
    elif opciones.lower() == "r":
        print()
        print("Regresaste al menu principal")
        menu_principal()
    elif opciones.lower() == "s":
        print("Has pulsado salir, gracias por tu visita")
        return exit()
    else:
        print()
        print("Elegir de nuevo el metodo que deseas ver")
        return metodos()

def listas():
    try:
        elige = int(input("Ingresa el metodo que quieres ver: "
                      "\n1.- Append"
                      "\n2.- Insert"
                      "\n3.- Remove"
                      "\n4.- Index"
                      "\n5.- In"
                      "\n6.- Regresar al menu principal"
                      "\n7.- Salir"
                      "\nEleccion: "))

        if elige == 1:
            print()
            lista1 = [1, 2, 3]
            print(
                "Para agregar un elemento al final de la lista se utiliza append: lista1 = [1, 2, 3]-> lista1.append(4)",
                end=" ")
            lista1.append(4)
            return print(lista1)
        elif elige == 2:
            print()
            lista2 = [1, 2, 3]
            print(
                "Para agregar un elemento en un lugar especifico de la lista se utiliza insert: lista2 = [1, 2, 3]-> lista2.insert(1, 4)",
                end=" ")
            lista2.insert(1, 4)  # La primera posicion es el indice y la segunda el valor
            return print(lista2)
        elif elige == 3:
            print()
            lista3 = [1, 2, 3, 4, 2]
            print("Para eliminar un elemento de una lista se usa remove: lista3 = [1, 2, 3, 4, 2]-> lista3.remove(2)",
                  end=" ")
            lista3.remove(2)  # remove elimina el primer elemento que aparece con el valor que le especificamos
            return print(lista3)
        elif elige == 4:
            print()
            lista4 = [1, 2, 3, 4, 5]
            print(
                "Para saber el indice de un valor en la lista se utiliza index: lista4 = [1, 2, 3, 4, 5] -> lista4.index(3)",
                end=" ")
            return print(lista4.index(3))
        elif elige == 5:
            print()
            num = [2, 3, 4]
            print("El operador in sirve para saber si existe un elemento en la lista: num = [2, 3, 4]-> 3 in num")
            print(3 in num)
            return 3 in num
        elif elige == 6:
            print()
            print("Regresaste al menu principal")
            menu_principal()
        elif elige == 7:
            print("Has pulsado salir, gracias por tu visita")
            return exit()
        else:
            print()
            print("Elegir de nuevo el metodo que quieres ver")
            return listas()
    except ValueError:
        print()
        print("Elegiste una letra en lugar de un numero, vuelve a elegir!")
        return listas()


def diccionarios():
    opciones = input("Ingresa que accion quieres ver en el diccionario: "
                     "\na) Agregar una nueva clave, valor"
                     "\nb) Eliminar una clave, valor"
                     "\nc) Cambiar el valor de una clave"
                     "\nd) Revisar si un elemento esta en el diccionario"
                     "\nr) Regresar al menu principal"
                     "\ns) Salir"
                     "\nElegir: ")
    print()
    traducciones = {"Pink": "Rosa", "Blue": "Azul"}
    print(traducciones)
    if opciones.lower() == "a":
        print("Para agregar elementos al diccionario se realiza de la siguiente manera: traducciones['Purple'] = 'Morado'")
        traducciones["Purple"]= "Morado"
        print(traducciones)
    elif opciones.lower() == "b":
        print("Para eliminar un elemento por clave: del traducciones['Pink'] ", end=" ")
        del traducciones["Pink"]
        print(traducciones)
    elif opciones.lower() == "c":
        print("Para cambiar el valor de una clave: traducciones['Pink'] = 'Rosado' ", end=" ")
        traducciones["Pink"] = "Rosado"
        print(traducciones)
    elif opciones.lower() == "d":
        print("Para ver si alguna clave se encuentra en el diccionario se utiliza: 'Blue' in traducciones ", end=" ")
        print("Blue" in traducciones)
    elif opciones.lower() == "r":
        print()
        print("Regresaste al menu principal")
        menu_principal()
    elif opciones.lower() == "s":
        print("Has pulsado salir, gracias por tu visita")
        return exit()
    else:
        print()
        print("Elegir de nuevo la accion que deseas ver")
        return metodos()


def funciones():
    opciones = input("Ingresa cual concepto de funcion quieres ver: "
                     "\na) Uso de Scope global y local"
                     "\nb) Recursion"
                     "\nr) Regresar al menu principal"
                     "\ns) Salir"
                     "\nElegir: ")
    print()
    if opciones.lower() == "a":
        scope_global = 23
        print("EL scope global se puede utilizar fuera de la funcion si es definida fuera")
        print("En este caso se definio scope_global = 23 fuera de la funcion")
        def scope_local(x): #Se pude utilizar solo dentro de la funcion definida
            print("Ahora estamos dentro de la funcion y aqui solo se puede utiliza el scope local que es: scope_local(x)")
            print("Se utiliza el scope global y se suma con la local que es 12 para dar el resultado: ", end=" ")
            sumar = (scope_global + x)
            return sumar
        print(scope_local(12))
    elif opciones.lower() == "b":
        print("La funcion recursiva es una funcion que se llama a sí misma")
        print("Estas se dividen en 2 partes una es el caso base y la segunda el caso recursivo")
        print("El caso base hace que la funcion se detenga.")
        print("El caso recursivo es el que se encarga de descomponer un problema en una version mas pequeña de ese mismo")
        print("Este es un ejemplo de una funcion recursiva: "
              "\ndef fibonacci(n):"
              "\n     if n == 0 or n == 1:"
              "\n         return n"
              "\n     else: Este es el caso recursivo ya que es donde se llama de nuevo a la funcion"
              "\n         return fibonacci(n-1) + fibonacci(n-2)")
        def fibonacci(n):
            if n == 0 or n == 1:
                return n
            else:
                return fibonacci(n-1) + fibonacci(n-2)
        print("El resultado de fibonacci(3) es: ", fibonacci(3))
    elif opciones.lower() == "r":
        print()
        print("Regresaste al menu principal")
        menu_principal()
    elif opciones.lower() == "s":
        print("Has pulsado salir, gracias por tu visita")
        return exit()
    else:
        print()
        print("Elegir de nuevo la accion que deseas ver")
        return metodos()


def operadores():
    print("La prioridad de las operaciones son (), **, *, / // %, +, -")
    print("La prioridad en booleanos es not, and y al final or")

def ciclos():
    opciones = int(input("Ingresar el ciclo que quieres ver: "))
    if opciones == 1:
        x = int(input("Ingresar el tamaño de la piramide: "))
        def piramide(x):
            contador = x
            contadort = 1
            for espacios in range(x):
                espacios = " "
                triangulo = "*"
                print(espacios * contador, triangulo * contadort)
                contador -= 1
                contadort += 2
        piramide(x)
    elif opciones == 2:
        y = int(input("Ingresa el tamaño del Diamante: "))
        z = y
        def diamante(y):
            contador = y
            contadort = 1
            for espacios in range(y):
                espacios = " "
                triangulo = "*"
                print(espacios * contador, triangulo * contadort)
                contador -= 1
                contadort += 2

            contadord = 1
            contadortd = contadort - 2
            for espaciosinv in range(z):
                espaciosinv = " "
                triangulos = "*"
                print(espaciosinv * contadord, triangulos * contadortd)
                contadord += 1
                contadortd -= 2
        diamante(y)

def menu_principal():
    eleccion = input("Ingresa de cual tema quieres aprender: \na) Conceptos \n"
                     "b) Metodos \n"
                     "c) Listas \n"
                     "d) Diccionarios \n"
                     "e) Funciones \n"
                     "f) Ciclos \n"
                     "g) Operadores \n"
                     "s) Salir \n"
                     "Eleccion: ")
    if eleccion.lower() == "a":
        print()
        print(conceptos())
    elif eleccion.lower() == "b":
        print()
        print(metodos())
    elif eleccion.lower() == "c":
        print()
        listas()
    elif eleccion.lower() == "d":
        print()
        diccionarios()
    elif eleccion.lower() == "e":
        print()
        funciones()
    elif eleccion.lower() == "f":
        print()
        ciclos()
    elif eleccion.lower() == "g":
        operadores()
    elif eleccion.lower() == "s":
        print("Has pulsado salir, gracias por tu visita")
        return exit()
    else:
        print()
        print("Elegir de nuevo el tema que deseas ver")
        return menu_principal()
menu_principal()