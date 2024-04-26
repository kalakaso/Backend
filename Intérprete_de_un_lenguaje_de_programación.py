
"""Escribe un programa que implemente un intérprete para un lenguaje de programación secuencial que consta de las siguientes instrucciones:

VAR nombre declara una variable con valor inicial 0. Es un error mencionar un nombre que ya fue usado en una declaración anterior.
REF nombre variable declara un nombre alternativo para una variable. Es un error mencionar un nombre que ya fue usado en una declaración anterior o mencionar una variable que no haya sido declarada anteriormente.
INC nombre incrementa el valor de la variable. Es un error mencionar una variable que no haya sido declarada anteriormente.
PRINT nombre imprime el valor de la variable. Es un error mencionar una variable que no haya sido declarada anteriormente."""


def interprete(entrada:str):
    """interpreta una entrada de texto parseguir las instrucciones
    
    Keyword arguments:
    entrada -- entrada de texto que contiene los comandos a analizar
    Return: salida de texto que imprime los erroes o valores de la lineas
    """
    
    entrada = entrada.split('\n')
    variables={}
    referencias={}
    salida=""
    for i in range(len(entrada)): # For normal para llevar el numero de las lineas de codigo
        elemento=entrada[i]
        comando_en_str = elemento.split() #Se para los comandos por clave y valores
        if comando_en_str.__len__() == 2: #Si el comando tiene solo clave y un valor
            clave , valor = comando_en_str

            #print(clave,valor)
            if clave=='PRINT':
                if valor in variables:
                    if  valor in referencias.values():#Busca si existe la referencia en variables o la misma variable
                        clave1=encontrar_clave_recursiva(valor, referencias, variables) 
                        salida+=str(variables[clave1])+"\n" 
                    else:
                        salida+=str(variables[valor])+"\n"
                else:
                    salida+="ERROR L"+str(i+1)+"\n"
            if clave== 'INC':
                if valor in variables:
                    if  valor in referencias.values(): #Busca si existe la referencia en variables o la misma variable
                        clave1=encontrar_clave_recursiva(valor, referencias, variables)
                        variables[clave1]+=1
                    else:                        
                        variables[valor]+=1
                        #salida+="INC "+" "+str(valor)+"\n"      
                    
                else:
                    salida+="ERROR L"+str(i+1)+"\n"
           
            if clave=='VAR':
                if  valor in variables:
                    salida+="ERROR L"+str(i+1)+"\n"
                else:
                    variables[valor]=0
                    
                
        if comando_en_str.__len__() == 3: #Si el comando tiene  clave y dos valores
            clave , valor,valor2 = comando_en_str

            if clave=='REF':
                if valor2 in variables:
                    if valor in variables:
                        salida+="ERROR L"+str(i+1)+"\n"
                    else:
                        referencias[valor2]=valor
                        variables[valor]=variables[valor2]
                else:
                        salida+="ERROR L"+str(i+1)+"\n"
            #print(clave,valor,valor2)
    
    print(salida) 
        
def encontrar_clave_recursiva(valor, referencias, variables):
    """busca el valor en el diccionario de referencias
       y las referencias en el de variables
    
    Keyword arguments:
    valor -- la clave a buscar
    referencias -- diccionario de referencias
    variables -- diccionario de variables
    Return: regresa la clave a la que se hace referencia
    """
    
    for clave, valor_encontrar in referencias.items():
        if valor_encontrar == valor:
            if clave in referencias.values():
                return encontrar_clave_recursiva(clave, referencias, variables)
            else:
                return clave
    return None
    
entrada="""PRINT A
INC A
VAR A
VAR A
PRINT A
INC A
PRINT A
REF B C
REF B A
INC A
PRINT A
PRINT B
INC B
PRINT A
PRINT B
REF C B
INC C
PRINT A"""
interprete(entrada)

