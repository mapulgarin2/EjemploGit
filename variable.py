# print("Hola Mundo")
# a = 30
# b = "Colombian python"
# c = 3.14
# d= 'a'
# e = True
# f,g,h=4,5,7
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(f)
# print(g)
# print(ah)

# print("Como se llama?")
# nombre =input() 
# print(f"me alegro de conocelo: {nombre}") 

# miComidaFavorita = "Espaguetti"
# print("mi comida favorita es: "+ miComidaFavorita)
# print("mi comida favorita es: ", miComidaFavorita)

# num1= 1
# num2= 2
# resul =num1 + num2

# print("La suma es: ",num1 + num2)
# print("La suma es: ", int(num1) + int(num2))#forzar a traves de un int

# print(f"El numero: {num1} sumado con el numero {num2},da como resultado {resul}")

# num1= 10
# num2= 2

# suma = num1 + num2
# resta = num1 - num2
# multi = num1 * num2
# div = num1 / num2
# residuo = num1 % num2
# exp = num1**num2

# print(f"la suma es {suma}")
# print(f"la resta es {resta}")
# print(f"la multi es {multi}")
# print(f"la div es {div}")
# print(f"el residuo es {residuo}")
# print(f"el exponencial es {exp}")

# peso = input("Cual es tu peso: ")
# estatura = input("Cual es tu estatura")
# imc = round(float(peso)/float(estatura)**2,2)
# print("Tu indice de masa corporal es: " + str(imc))

# var = 5 == 1
# print(var)
# var = 5 >1
# print(var)
# var = 5 < 1
# print(var)
# var = 5 != 1
# print(var)


# x = 1
# y = 2 
# z = 3
# miVar = x + y == z
# print(miVar)

# res = (x < y) or (y > z)
# print(res)
# res = not (y > z)
# print(res)

# a = 5
# a+=5
# print(a)
# a-=5
# print(a)
# a*=5
# print(a)
# a/=5
# print(a)
# a%=5
# print(a)

# horas =float(input("Digite la cantidad de horas trabajadas: ")) 
# costo = float(input("Digite el valor por hora: "))
# salario =horas*costo

# print(f"Tu salario total es: {salario} pesos")


# frutas = int(input("Introduce la cantidad de frutas que desea llevar: "))
# precio = 1.0
# descuento = 0.5
# costo_descuento = precio*frutas*0.5

# print(f"El precio de la fruta sin descuento es {precio} pesos")
# print(f"El descuento de la fruta que no esta fresca es {descuento*100}%")
# print(f"El costo final a pagar es de {costo_descuento} pesos")

# name = input("Cual es su nombre?: ")

# print(name.lower())
# print(name.upper()+ " tiene " + str(len(name))+ " letras")
# print(name.title())

# mapulgarin2
email = input("Introduce una email con el @ al final: ")
print(email[:email.find('@')] + '@coltis.com')
