# ejercicio 1

# opcion 1

# numeros = [10,40,12,20,4,28,30,14,5,9]

# print("primera posicion: ", numeros[0])
# print("ultima posicion: ", numeros[-1])
# print("posicion cinco: ", numeros[5])

# ordenar = numeros.sort(reverse=True)

#opcion 2

# lista=[]
# for i in range(10):
#     numero=int(input(f"Agrega el numero #{i + 1}"))
#     lista.append(numero)
# print(lista[0],lista[-1],lista[5])
# inverso=lista[::-1]
# print(f"{inverso}")


# ejercicio 2

# frutas = ["manzana", "pera", "banano", "uva"]
# agregar=input("agrega una fruta ")
# frutas.append(agregar)
# agregar2=input("agrega una fruta en la segunda posicion ")
# frutas.insert(1,agregar2)
# frutas.remove("banano")

# print(frutas)


#ejercicio 3

# lista = []

# for i in range (20):
#     lista.append(i+1)

# maximo = max(lista)
# minimo = min(lista)

# print(f"la suma de todos es: {sum(lista)} el numero mas alto es el: {maximo} y el de menor valor es: {minimo}")



#ejercicio 4

# opcion 1

# tupla = ("colombia", "argentina", "brasil", "francia", "rusia")

# # lista.insert("estados unidos")

# lista = list(tupla)
# lista.remove("argentina")
# tupla = tuple(lista)
# print(tupla)

#opcion 2

# tupla=("Rusia", "Venezuela", "Cuba", "China", "Korea sur")

# #tupla.remove("Rusia")

# tupla_lista = []
# for i in tupla:
#     tupla_lista.append(i)
# tupla_lista.remove("Rusia")
# tupla=tuple(tupla_lista)
# print(tupla)


# ejercicio 5

#opcion 1

# lista = [1,2,2,3,4,4,4,5,6,6,6,6]

# for i in set(lista):
#     print(f"el numero {i} aparece {lista.count(i)} veces")

#opcion 2

# numeros=[1,2,2,3,4,4,4,5,6,6,6,6]
# print(numeros.count(1))
# print(numeros.count(2))
# print(numeros.count(3))
# print(numeros.count(4))
# print(numeros.count(5))
# print(numeros.count(6))


# for i in set(numeros):
#     print(f" el numero {i} esta:{numeros.count(i)}")



#ejercicio 6


# persona = {
#    "nombre": "Ana",
#    "edad": 25,
#    "profesion": "Ingeniera"
# }

# persona.update({"cuidad": "medellin"}) 
# persona ["edad"] = 26
# del persona["profesion"]
# print(persona)


#ejercio 7

# info= {
#     "Bryan" : 3007125622,
#     "Juan Jose" : 3219023372,
#     "Alexandra" : 3053123421
# }

# print(info)
# nombre=str(input("Ingresa el nombre que deseas buscar"))
# print(f"El numero de la persona es: {info[nombre]}")
# del info["Bryan"]


#ejercicio 8


# estudiante1 = {
#    "nombre": "Ana",
#    "edad": 25,
#    "nota": 4.5
# }

# estudiante2 = {
#    "nombre": "Luis", 
#    "edad": 20,
#    "nota": 5.0
# }


# estudiante3 = {
#    "nombre": "Maria", 
#    "edad": 22,
#    "nota": 3.8
# }



# promedio = (estudiante1["nota"] + estudiante2["nota"] + estudiante3["nota"]) / 3
# maximo = estudiante1["nota"], estudiante2 ["nota"], estudiante3 ["nota"] 
# nota_max = max(maximo)


# print(f"Nombre: {estudiante1['nombre']}, Edad: {estudiante1['edad']}, Nota: {estudiante1['nota']}")
# print(f"Nombre: {estudiante2['nombre']}, Edad: {estudiante2['edad']}, Nota: {estudiante2['nota']}")
# print(f"Nombre: {estudiante3['nombre']}, Edad: {estudiante3['edad']}, Nota: {estudiante3['nota']}")
# print(f"Promedio de notas: {promedio:.2f}")
# print(f"La nota más alta es {nota_max}")


#ejercicio 9


# hola={
#         "Arroz"   : 2500,
#         "Arepa"   : 5000,
#         "Gaseosa" : 4000,
#         "Aceite"  : 3500,
#         "Mantequilla" : 1500
#     }

# aaa=str(input("Que producto deseas? ")).capitalize()
# if not aaa in hola:
#     print("El producto no esta")
# else:
#     print(hola[aaa])

# total_precio=int(hola["Aceite"]+hola["Arepa"]+hola["Arroz"]+hola["Gaseosa"]+hola["Mantequilla"])
# print(f"Todo vale {total_precio}")
# v=max(hola["Aceite"],hola["Arepa"],hola["Arroz"],hola["Gaseosa"],hola["Mantequilla"])
# print(v)


#EJERCICIO 10 

# matriz=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

# acumulador_diagonal=0
# acumulador_mitad=0
# acumulador_diagonal2=0

# for i in range(3):
#     for j  in range(3):
    
#         if i==j+1:
#             print(f"{matriz[i][j]}")
#             acumulador_diagonal=matriz[i][j]
#         if i==0:
#             acumulador_mitad+=matriz[i][j]
#         if i+j==2:
#             acumulador_diagonal2=matriz[i][j]+acumulador_diagonal2

# print(f"\n{acumulador_diagonal}")
# print("el acomulador de la mitad es:",acumulador_mitad)
# print("el acomulador de la Diagonal es:",acumulador_diagonal2)
# lista=[1,2,3]