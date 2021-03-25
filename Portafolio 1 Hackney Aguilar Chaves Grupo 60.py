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
        
        return


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
    if isinstance (num, int) and isinstance (factor, int ):
        if num > 0 and factor > 0:
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
    if isinstance(divisor, int) and isinstance(dividendo, int):
        if (divisor < dividendo):
            return 0
        else:
            return 1 + divisionRecursivo(dividendo-divisor,divisor)
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
   if isinstance (num, float):
      resultado = num * 10
      return print (int (float (resultado)))        
            
        
        

   
    
        
            


