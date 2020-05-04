def turning_number(lista, tamanho):
    cresce = 1
    decresce = 1

    for i in range(1,tamanho):
        if(lista[i] < lista[i - 1]):
            if cresce == 1:
                decresce = decresce + 1
            else:
                return [-1,0];
        elif(lista[i] > lista[i - 1]):
            if cresce == 1:
                minimo_global = lista[i-1]
                index = i-1
            if decresce >= 2:
                cresce = cresce + 1
            else:
                return [-1, 0];
        elif(lista[i] == lista[i - 1]):
            return [-1, 0];
    if (cresce >= 2 and decresce >= 2):
        return [minimo_global,index];
    else:
        return [-1, 0];


lista = [21,11,10,2,5,9]
tamanho = len(lista)
numero_e_index = turning_number(lista,tamanho)
#numero_e_index = [1,5]
if (numero_e_index[0] == -1):
    print("The input is not an unimodal aray")
else:
    print("The index of the turning number is {}".format(numero_e_index[1]))


