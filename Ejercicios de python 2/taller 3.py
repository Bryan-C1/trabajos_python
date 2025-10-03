
#Ejercicio 1

# numero=[]
# contador_0=0
# contador_p=0
# contador_n=0
# for i in range(5):
#     Numeros=int(input("digite un numero"))
#     if Numeros==0:
#         contador_0+=1
#     elif Numeros>0:
#         contador_p+=1
#     elif Numeros<0:
#         contador_n+=1
#     numero.append(Numeros)
#     numero.sort()
# print("\nAsi quedaria tu lista\n",numero)
# print(f"Total numeros +,- y 0 es\n+:{contador_p}\n-:{contador_n}\n0:{contador_0}")


#Ejercicio 2

# n = int(input("Ingrese un número: "))

# for i in range(1, n + 1):   
#     cuadrado = i ** 2
#     if cuadrado % 2 == 0:
#         print(f"{i}^2 = {cuadrado} es par")
#     else:
#         print(f"{i}^2 = {cuadrado}")


#Ejercicio 3

# palabra = str(input("Ingresa una palabra o frase: ")) .lower()
# letra = str(input("Ingresa la letra que deseas encontar: ")) .lower()
# contador = 0
# for i in palabra:
#     if i == letra:
#         contador += 1
# if contador > 0:
#     print(f"tu letra aparece {contador} veces")
# else:
#     print("Tu letra no aparece")


#Ejercicio 4

#Dudas


#Ejercicio 5

# contador_a=0
# contador_r=0
# notasagp=[]
# for i in range(1,6):
#     notas=float(input(F"Ingresa la nota #{i}\n"))
#     notasagp.append(notas)
#     if notas>5:
#         print("Nota no valida\nPrograma FINALIZADO")
#         break
#     elif notas>=3:
#         print(f"{notas} Aprobada")
#         contador_a+=1
#     elif notas<3:
#         print(f"{notas} Reprobada")
#         contador_r+=1
# print(f"\nEl total de aprobadas fue: {contador_a}\nEl total de reprobadas fue: {contador_r}")
# print(notasagp)