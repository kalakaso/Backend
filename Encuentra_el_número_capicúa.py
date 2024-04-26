""" Un número N, con dígitos (d1 d2 .. dn),se considera capicúa (o palíndromo) si es igual
a su reverso, denotado como (dn dn-1 . .d1)  Un procedimiento que puede generar un número capicúa 
 a partir de un número N es el siguiente:
 Si N ya es capicúa, entonces terminamos.
Si N no es capicúa, entonces a N le sumamos su reverso.
El proceso anterior se repite hasta que N se considere capicúa.
Toma en cuenta que aún no se sabe si siempre es posible generar un número capicúa, por lo cual, si N
 no es capicua pero ya es mayor a 10^9, entonces debes detenerte e imprimir.
"""



def identificar_capicua(numero:int):
    """Valida si es un numero capicua
    
    Keyword arguments:
    numero -- numero entero
    Return: regresa verdadero o falso segun sea el caso
    """
    
    lista_numero=list(str(numero))
    return lista_numero == lista_numero[::-1] # verifica si el numero se lee igual de izquierda a derecha
    
def generar_capicua(numero:int):
    """Genera un numero capicua segun sea el caso
    
    Keyword arguments:
    numero -- numero entero
    Return: un numero entero capicua o -1 segun sea el caso
    """
    
    while(numero)< (10 ** 9): # bucle hasta 10^9
        
        lista_numero = list(str(numero))
        if identificar_capicua(numero): # Valida si es o no capicua
            return(numero)# Si si regresa el numero
        else:                           # Si no agrega el inverso al numero
            Lista_reverso = lista_numero[::-1]
            reverso="".join(Lista_reverso)
           # print(lista_numero,Lista_reverso,numero)
            numero=numero+int(reverso)  # se suma el inverso del numero al numero 
            
    
    return -1 # Si es mayor a 10^9 regresa -1

print(generar_capicua(57)) 
