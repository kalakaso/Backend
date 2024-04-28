


entrada="""3
3 5 4
3
2 1
9 3
1 2"""
def tiempo_minimo(entrada):
    arr_entrada=entrada.split('\n')
    N=0
    M=0
    arr_N=[]
    arr_M=[]
    for i in range(len(arr_entrada)):
        arr_int=list(map(int,arr_entrada[i].split(' ')))
        if len(arr_int)==1 and i == 0:
            N=arr_int[0]
        
        if len(arr_int)>1 and i == 1:
            arr_N=arr_int
        
        if len(arr_int)==1 and i == 2:
            M=arr_int[0]
        
        if len(arr_int)>1 and i > 2:
            arr_M.append(arr_int)

    ratones=len(arr_N)
    slots=0
    for e in arr_M:
        slots+=e[1]
    if slots < ratones:
        return -1
    else:
        """# Ejemplo de uso con parámetros arr_N y arr_M
        distancia_cercana = lista_distancia(arr_N, arr_M)
        lista_modificada = procesar_lista_recursiva(distancia_cercana ,None, 1)
        #print("Lista modificada:", lista_modificada)
        flag=0
        print(lista_modificada)
        for e in lista_modificada:
            flag=max(e[1][1],flag)
        print(flag)
        """
        arr_N.sort() 
        arr_N.reverse()
        print(arr_N)
        print(lista_distancia( arr_N, arr_M))
        print( lista_seleccion(lista_distancia( arr_N, arr_M)))
       
def lista_distancia( arr_N:list, arr_M : list):
    distancia_cercana=[]
    for raton in arr_N:
        arr_distancias=[]
        for madrigera in arr_M:
             distancia = abs(raton - madrigera[0])
             arr_distancias.append([madrigera[0],distancia])
        lista_ordenada = sorted(arr_distancias, key=lambda x: x[1])
        
        distancia_cercana.append([raton,lista_ordenada])
    return distancia_cercana
     
def lista_seleccion(distancia_cercana):    
    nuevo_arr=[]    
    for conjunto in distancia_cercana: # conjunto[0]-[1] dos arreglos 
        minimo = min(sublista[1] for sublista in conjunto[1])
        print(conjunto[1], minimo)
        for raton_madrigera in conjunto[1]:
            # madrigeras[0] = RATON madrigeras [1] = conjunto de madrigeras
            if minimo == raton_madrigera[1]:
                
               nuevo_arr.append([conjunto[0],raton_madrigera])
    return nuevo_arr

def procesar_lista_recursiva(distancia_cercana, lista=None, idx=1):
  
    if lista is None:
        lista = lista_seleccion(distancia_cercana)
   
    
    if idx >= len(lista):
        return lista
    
    elemento_actual = lista[idx][1]
    elemento_anterior = lista[idx - 1][1]
    
    if elemento_actual[0] == elemento_anterior[0]:
        bandera=elemento_anterior[2]
        
        if elemento_actual[1] > elemento_anterior[1] and bandera > 0:
            for sublista_externa in distancia_cercana:
                print(distancia_cercana)
                for sublista_interna in sublista_externa[1]:
                    if sublista_interna == elemento_anterior:
                        sublista_externa[1].remove(sublista_interna)
                        lista=None

    return procesar_lista_recursiva(distancia_cercana, lista, idx + 1)




tiempo_minimo(entrada)
