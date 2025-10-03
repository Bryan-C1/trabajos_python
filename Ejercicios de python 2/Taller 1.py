#ejercicio 1

#lado = 20
#area = lado * lado
#print("El area del cuadrado es: ", area)


#ejercicio 2

#diametro = 20
#radio = diametro / 2
#area = radio ** 2 * 3.1416
#print("el area del circulo es:",area)


#ejercicio 3

#salario = int(input("inserte su salario: "))
#salud = salario * 0.04
#print("debe pagar por salud:", salud)


#ejercicio 4

#diametro = float(input("digite el diametro del cono: "))
#altura = float(input("digita la altura del cono: "))
#radio = diametro / 2
#area = radio ** 2 * 3.1416
#volumen = area * altura / 3
#print("el volumen del cono es:", volumen)


#ejercicio 5

#base = float(input("digite la base del triangulo: "))
#altura = float(input("digite la altura del triangulo: "))
#area = base * altura / 2
#print("el area del triangulo es: ", area)

#ejercicio 6

#hipotenusa=10     
#adyacente=5 
#opuesto=3

#sin=opuesto/hipotenusa
#cos=adyacente/hipotenusa
#tan=adyacente/opuesto

#print(f"el seno es {sin}")
#print("el seno es",cos)
#print("el seno es",tan)


#ejercicio 7

# texto = "BRYAN"
# minuscula = texto.lower()
# print(minuscula)


#ejercicio 8 

#texto = "cordoba"
#mayuscula = texto.upper()
#print(mayuscula)


#ejercicio 9 

#nombre = input("digite un nombre: ")
#nombre_cap = nombre.title()
#print(nombre_cap)


#ejercicio 10

# frase = input("escribe una frase: ")
# letra = input("digite la letra que quieres contar: ")
# cantidad = frase.count(letra)
# print("el numero de letra es: ", cantidad)


#ejercicio 11

palabra = input("digite la palabra: ")
letra = input("digite la letra: ")

posicion = palabra.find(letra)
cantidad = palabra.count(letra)

if posicion != -1:
    print(f"la letra aparece por primera vez en la posicion {posicion} y hay {cantidad} en total")
else: 
    print(f"la letra {letra} no se encontro en la palabra")


#ejercicio 11

#frase = "Los campistas necesitan practicar mucho con python!, por eso, harán bastantes ejercicios!"
#cantidad = frase.count(" ")
#print(f"en la frase hay {cantidad} espacios en blanco")


 #ejercicio 12

#frase = "Los campistas necesitan practicar mucho con python!, por eso, harán bastantes ejercicios!"
#separado = frase.split()
#print(separado)}


#ejercicio 13

#frase = "Los campistas necesitan practicar mucho con python!, por eso, harán bastantes ejercicios!"
#separado = frase.split(",")
#print(separado)


#ejercicio 14

#edad = int(input("digite su edad: "))

#if edad >= 18:
    #print("eres mayor de edad en colombia")
#else:
    #print("no eres mayor de edad")


#ejercicio 15

#edad = int(input("digite su edad: "))

#if edad >= 21:
    #print("eres mayor de edad en el resto del mundo")
#elif edad >= 18:
    #print("eres mayor de edad en colombia")    
#else:
    #print("no eres mayor de edad")


#ejercicio 16

#nombre = input("didgite su nombre: ") .lower() .strip()

#nombres_validos = ["bon jovi","Bon Jovi Ernesto"]

#if nombre in nombres_validos:
    #print("eres Bon Jovi Ernesto")
#else:
    #print("no eres Bon Jovi Ernesto ")


#ejercicio 17

#numero1 = int(input("digite el primer numero: "))
#numero2 = int(input("digite el segundo numero: "))

#if numero1 > numero2: 
    #print(f"el numero {numero1} es mayor que el numero {numero2}")
#elif numero1 < numero2:
    #print(f"el numero {numero2} es mayor que el numero {numero1}")
#else:
    #print("los dos numeros son iguales")


#ejercicio 18

#nombre = input("digite su nombre: ").strip()
#genero = input("digite su genero: ").strip() .lower()

#generos_validosf = ["f", "femenino"]
#generos_validosm = ["m", "masculino"]


#if genero in generos_validosm:
    #print(f"hola {nombre} bienvenido")
#elif genero in generos_validosf:
    #print(f"hola {nombre} bienvenida")
#else:
    #print("genero no permitido")


#ejercicio 19

#SMV =  1300000
#salario = int(input("ingresa tu salario: "))

#prestacional = SMV * 0.30
#salarioint = SMV * 10 + prestacional

#if salario >= salarioint:
    #print("tu salario es integral")
#else:
    #faltante = salarioint - salario
    #print("tu salario no es integral")
    #print("salario faltante para se integral ", faltante)


#ejercicio 20

#peso = float(input("digite su peso: "))
#ltura = float(input("digite su altura "))

#imc = peso / altura ** 2

#if imc < 18.5:
    #print("Bajo peso")
#elif 18.5 <= imc < 25:
    #print("Normal")
#elif 25 <= imc < 30:
    #print("Sobrepeso")
#else:
    #print("Obesidad")


#ejercicio 21

#numero1 = int(input("digite el primer numero: "))
#numero2 = int(input("digite el segundo numero: "))
#numero3 = int(input("digite el tercer numero: "))

#numeros = [numero1, numero2, numero3]

#numeros.sort()

#print(f"El número menor es: {numeros[0]}")
#print(f"El número del medio es: {numeros[1]}")
#print(f"El número mayor es: {numeros[2]}")


#ejercicio 22

#def calcular_bono(salario, estrato):
    #match estrato:
        #case 1:
            #bono = salario * 0.35
        #case 2:
            #bono = salario * 0.30
        #case 3:
            #bono = salario * 0.25
        #case 4:
            #bono = salario * 0.20
        #case 5 | 6:  
            #bono = salario * 0.10
        #ase _:      
            #bono = 0
    #return bono


#salario = float(input("Ingrese su salario: "))
#strato = int(input("Ingrese su estrato (1-6): "))

#bono = calcular_bono(salario, estrato)
#salariototal = salario + bono

#print(f"Su pago es de {salariototal} y su bono equivale {calcular_bono(salario, estrato)}")



    






