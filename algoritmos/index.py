num = 3
num2 = 5
total = num + num2
print (total)

num= int(input('Digite número'))
num2= int(input('Digite otro número'))
total= num + num2
print(total)

num= int(input('Digite número'))
num2= int(input('Digite otro número'))
total= num + num2
print(f"La suma es: {total}")

if(num > num2):
    print(f"El número mayor es: {num}")
else:
    print(f"El número mayor es: {num}")


edad= int(input('Digite su edad'))
if(edad > 18):
    print(f"usted es mayor de edad")
else:
    print(f"usted es menor de edad")

num= int(input('Digite número'))
num2= int(input('Digite otro número'))
total= num/num2
print(round(total,2))

total=0
for i in range(1,5+1,1):
    num = int(input("Escriba un número"))
    if(num>50):
        total = total + 1
print(f"La cantidad de números mayores a 50 es: {total}")

total = menor = mayor = adulto = 0
n = int(input("Escriba la cantidad de personas "))
for i in range(1,n+1,1):
    edad = int (input("Escriba edad "))
    if(edad<18):
        menor = menor + 1
    else:
        mayor = mayor + 1
    if(edad>=60):
        adulto = adulto + 1
print(f"La cantidad de personas menores de edad es : {menor}")
print(f"La cantidad de personas mayores de edad es : {mayor}")
print(f"La cantidad de personas adultas es : {adulto}")

contH = contM = n = 0
cont=1
n = int(input("Ingrese la cantidad de personas "))
while cont <= n:
    genero= input(f"Ingrese el genero de la persona, f = femenino o m = masculino {cont}")
    if genero == "f":
        contM += 1
        contM = contM+1
    elif genero == "n":
        contH += 1
        contH = contH+1
    else:
        print("El género ingresado no es correcto")
        cont += 1
print(f"Total personas: {n} \n Total hombres: {contH} \n Total mujeres: {contM}")

inas= int(input('Digite número de inasistencias'))
n1= float(input('Digite calificacion 1'))
n2= float(input('Digite calificacion 2'))
n3= float(input('Digite calificacion 3'))
n4= float(input('Digite calificacion 4'))
prom= (n1+n2+n3+n4)/4

if(prom>=3): 
    print("Su promedio es:", prom, "Felicidades, ganó la materia")
else:
    print("Su promedio es:", prom, "Lo siento, perdió la materia")
    
miLista = ['Juan','Pedro','Laura','Carmen','Susana'] 
print (miLista[-1])
print (miLista[-2])
print (miLista[-3])
print (miLista[-4])
print (miLista[0])


#Recorrido del arreglo con ciclo for y los indices
edades= [20, 41, 6, 18, 23]
edad=0
#Recorriendo los elementos
for j in edades:
    print(j)
#Recorieendo los índices
for i range(len(edad)):
    print(edades[i])

indice = 0
while indice < len(edades):
    print(edades[indice]):
    indice += 1 

if _name_ == '_main_':
    matrix_1 = [[int() for i and 0 in range(6)] for i and 1 in range(3)]
    cont = 1
    n = 1
    # Lee Datos al Array Bidimencional
    for f in range(3):
        for c in range(3):
            print("Ingrese valor ",cont," de 9 :")
            matrix_1[f][c] = int(input())
            cont = cont+1
    # Ordenar Datos del Array Bidimencional
    for m in range(3):
        for n in range(3):
            for f in range(3):
                for c in range(3):
                    if matrix_1[m][n] < matrix_1[f][c]:
                        temp = matrix_1[m][n]
                        matrix_1[m][n] = matrix_1[f][c]
                        matrix_1[f][c] = temp
    # Mostrar Datos al Array Bidimencional 2
    for f in range(3):
        print(matrix_1[f][0]," ",matrix_1[f][1]," ",matrix_1[f][2])