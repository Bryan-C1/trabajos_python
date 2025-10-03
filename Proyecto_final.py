lista=[]
def tareas_dic():               #Se agregan las tareas en la lista anterior mente creado de forma de diccionario
    descripcion=str(input("Ingresa una tarea:\n"))              #agrega una aterea y se guarda en la variable descripcion
    if descripcion:                                             #Utilizamos el if para filtrar si la condicional esta vacia o no (Si esta vacia lo dice mediante ouput)
        tarea={'tarea':descripcion, 'estado':'pendiente'}       #cracion de diccionario mediante {} (Estructura que guarda datos)
        lista.append(tarea)
        print(f"Tu tarea fue agregada: {descripcion}")
    else:
        print("Debes agragar algo a la tarea.")                 #Esta condicion simplemente filtra que agreguemos algo a tarea


def listar_tareas():            #Listar las tareas para saber el orden e identificar cada una
    if not lista:                                               #Operador Logico(not) para comparar variables o una condicion en este caso
        print("No hay tareas.")                                 #si no hay nada en la lista ejecuta el ouput
    else:
        print("\nTAREAS")
        for i,tarea in enumerate(lista):
            print(f"{i}. [{tarea['estado']}] {tarea['tarea']} ")      #hacemos un ouput usando la libreria y   # hacemos que la variable i sea la que avance en la enumeracion de tareas


def marcar_realizado():     #Con base en el listado de arriba se elige una y la coloca como realizada
    if not lista:
        print("No hay tareas para marcar.")
        return
    listar_tareas()  # Mostramos llamando al listado para que elija
    try:
        indice = int(input("Escribe el número de la tarea para marcar como realizada:\n").strip())
        
        lista[indice]['estado'] = 'realizada'
        print(f"Tarea '{lista[indice]['tarea']}' marcada como realizada.")
    except ValueError:   # Si el input no es un número válido
        print("Debes ingresar un número válido.")
    except IndexError:   # Si el número está fuera de rango
        print("Número de tarea inválido.")

def menu():
    while True:
        print("Gestor de Tareas\n1) Agregar tarea\n2) Listar tareas\n3) Marcar tarea como realizada\n4) Salir")

        opcion=int(input("Ingresa una opcion\n"))
        if opcion==1:
            tareas_dic()
        elif opcion==2:
            listar_tareas()
        elif opcion==3:
            marcar_realizado()
        elif opcion==4:
            print("saliendo del programa")
            break
        else:
            print("Opcion invalida, intenta de nuevo")

menu()