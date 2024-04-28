from collections import deque
sub_sub_arreglo = deque()  # Cola vacía

M={'2':1,'9':3,'1':2}

print(sorted(list(M.keys())))
if M[str(2)] > 0:
    pass
    #M[str(2)]-=1
#print(M[str(2)])

arreglo=[[5, [[2, 3], [9, 4], [1, 4]]], [4, [[2, 2], [1, 3], [9, 5]]], [3, [[2, 1], [1, 2], [9, 6]]]]
sub_arreglo=[5, [[2, 3], [9, 4], [1, 4]]]
for elemento in sub_arreglo[1]:
    sub_sub_arreglo.append(elemento)
# Sacar elementos de la cola (FIFO)
elemento = sub_sub_arreglo.popleft()
posision=elemento[0] 
print(posision)
#print( M[str(posision)])
if M[str(posision)] > 0:
    print("Esta libre")
else:
    print("Esta ocupado")
