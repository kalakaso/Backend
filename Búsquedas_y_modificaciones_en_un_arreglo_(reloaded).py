"""
Dado un arreglo de N
enteros, escribe un programa que procese una secuencia M de 
comandos de los siguientes tipos:
    CUENTA K: Contar la cantidad de veces que aparece el entero K en el arreglo.
    SUMA K: Sumar K a todos los elementos del arreglo.
"""
        
def suma(k:int,arreglo:list):
    """suma el elemento K de tipo entero a cada parte de un arreglo de enteros 
Keyword arguments:
k -- El elemento a sumar
arreglo -- arreglo N de enteros
Return: nuevo arreglo N
"""
    for i in range( len(arreglo)):
        arreglo[i]=arreglo[i]+k
    return arreglo

def cuenta(k:int,arreglo:list):
    """cuenta las veces que se repite el elemento k en el arreglo
    
    Keyword arguments:
    k -- un numero entero
    Return: numero de veces que se encuentra k en el arreglo
    """
    
    return arreglo.count(k)
    
def busqueda_modificacion(cadena:str):
    """
    Extrae los elemenots N  y M [arreglo N elementos] y COMANDOS M de la cadena de texto
    y llama las funciones cuenta() y suma() 
    Keyword arguments:
    cadena:str -- entrada en formato texto que contiene N M segido de un [arreglo N elementos] y COMANDOS M
    Return: Para cada evento del tipo CUENTA, un entero que sea la cantidad de veces que aparece el entero dado..
    """
    
    entrada = cadena.split('\n') # Arreglo del texto se parado por saltos de linea
    str_N_y_M=entrada[0].split() #Primer elemento que tiene N y M
    int_N_y_M= list(map( int, str_N_y_M)) # creamos arreglo de enteros de N  y M
    
    if int_N_y_M.__len__() ==2: # Validamos que sean N y M solamente
        N,M = int_N_y_M
        arreglo=entrada[1].split() # obtenermos el arreglo de numero N
        arreglo=list(map(int,arreglo)) # creamos el arreglo de numero N de enteros
        salida=""   #Se crea una unica salida
        for i in range(2,2+M): # partimos desde el 3 elemento del arreglo principal hasta el numero M para obtener los comandos
            caso,k=entrada[i].split() # Para cada comando se paramos por comando y clave
            k=int(k)
            if("suma"==caso.lower()):
                suma(k,arreglo)  
            if("cuenta"==caso.lower()):
                salida= salida +str(cuenta(k,arreglo)) +"\n"  # Se actualiza la salida
        print(salida) # Se imprime en una unica salida

entrada= """5 7
3 1 4 1 6
CUENTA 4
CUENTA 8
CUENTA 1
SUMA 3
CUENTA 4
CUENTA 8
CUENTA 1"""

busqueda_modificacion(entrada)
