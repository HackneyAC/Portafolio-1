# Portafolio 1 Hackney Aguilar Chaves Grupo 60

"""
Nombre: Divisores

Entradas:
        num: Numero entero positivo

Salidas:
        Imprimir los divisores de un numero de manera descendente.

Restricciones:
        Debe ser un numero entero positivo mayor a cero

"""

def divisores(num):
    if isinstance(num, int): # Es un numero entero
        if (num > 0): # Debe ser un numero mayor a cero
            return divisores_aux(num)
        else:
            print("El valor ingresado no es mayor a cero")
    else:
        print("Error: El valor ingresado no es un numero entero")

def divisores_aux(num):
    if (num==0):
        return 0
    else:
        return 1 + divisores_aux(num % 10)


"""
Nombre: multiploRecursivo

Entradas:
        num: numero entero posivivo mayor a cero
        factor: numero entero positivo mayo a cero

Salidas:
         La multiplicacion de un numero n por un numero m sin utilizar el operador
         de multipliacon

Restriccione:
        El valor de num y factor deben de ser enteros positivos mayo a cero

"""
def multiplicarRecursivo(num, factor):
    if isinstance (num, int) and isinstance (factor, int ):# Es un numero entero
        if num > 0 and factor > 0:#Deben ser mayor a cero
            if factor==0:
                return 0
            elif factor == 1:
                return num
            else:
                return num + multiplicarRecursivo(num, factor- 1)
        else:
            print("Error: Solo se permite valores positivos")
    else:
        print("Error: El valor ingresado no es un número entero")


"""
Nombre:

Entradas:
        divisor: Numero entero positivo mayor a cero
        dividiendo: Numero entero positivo mayor a cero
        
Salidas:
        Resultado de la divicion entera de un numero n por un numero m sin utilizar
        el operador divisor

Restricciones:
            El valor de los operadores debe de ser un numero entero positivos

"""

def divisionRecursivo(divisor, dividendo):
    if isinstance(divisor, int) and isinstance(dividendo, int):# Es un numero entero
        if (divisor < dividendo):#Debe el divisor debe ser mayor al dividendo
            return 0
        else:
            return 1 + divisionRecursivo(dividendo-divisor)
    else:
        print("El valor ingresado no es entero")
        


"""
Nombre: CorrimientoAEntero

Entradas
        num: Es un numero flotante

Salidas:
        Pasar los numero de la parte decimal a entero

Restricciones:
            El numero ingresado debe de ser flotante

"""

def corrimientoAEntero(num):
   if isinstance (num, float):# Es un valor flotante
      resultado = num * 10
      return print (int (float (resultado)))


"""
Nombre:contarDigitosFlotante

Entradas:
        num: Es un numero Flotante
Salidas:
        Contar digitos tipo flotante ya sea negativo o positivo

Restricciones:
            El valor ingresado debe ser Flotante
"""


def contarDigitoFlotante(num):
    if(isinstance(num, float) == False):# Es un valor Flotante
        return print("Error tipo de dato, no es flotante")
    elif (num == 0):
        return 1
    elif (num < 0):
        num*=-1
    else:
        return contarDigitoFlotante_aux(num)

def contarDigitoFlotante_aux(n):
    if(n == 0):
        return 0
    else:
        return 1 +contarDigitoFlotante_aux(n // 10)

"""
Nombre: indiceNumero

Entradas:
        num:Debe de ser un numero entero positivo
        indice: Debe ser un numero mayor o igual a cero
Salidas:
        Devuelve un digito segun su indice

Restricciones:
            Solo numero enteros

"""

def indiceNumero(num, indice):
    if isinstance(num, int) and isinstance(indice, int):# Es un numero entero
        if (num > 0) and (indice <= 0):
            return indiceNumero_aux(num, indice)
        else:
            print ("El numero debe ser mayor a cero")
    else:
        print("Error: el numero no entero")

def indiceNumero_aux(num, indice):
    if (num > 0) and (indice <= 0):
        resulta = (num // indece)% 10
        return resulta + indiceNumero_aux(num, indice%10)
    else:
        print ("Error: Ingrese un valor valido")

"""
Nombre:cortarNumero

Entradas:
        num:Debe de ser un numero entero positivo
        indice: Debe ser un numero mayor o igual a cero
Salidas:
        Devuelve un digito segun su indice

Restricciones:
            Solo numero enteros

"""
def cortarNumero(num, indice):
    if isinstance(num, int) and isinstance(indice, int):# Es un numero entero
        if (num > 0) and (indice <= 0):
            return cortarNumero_aux(num, indice)
        else:
            print ("El numero debe ser mayor a cero")
    else:
        print("Error: el numero no entero")

def cortarNumero_aux(num, indice):
    if (num > 0) and (indice <= 0):
        resulta = (num // indece)% 10*2)
        return resulta + cortarNumero_aux(num, indice%10)
    else:
        print ("Error: Ingrese un valor valido")
            
            
        
            
        
        

   
    
        
            


