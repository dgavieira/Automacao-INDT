#funcao que identifica o 'turning number'
def turning_number(lista, tamanho):
    #cria uma contagem incremental
    cresce = 1
    #cria uma contagem decremental
    decresce = 1

    #loop para varrer o vetor
    for i in range(1,tamanho):
        #verifica se o número é menor que o anterior
        if(lista[i] < lista[i - 1]):
            #verifica se o vetor está no estágio crescente
            if cresce == 1:
                #diminui a contagem decremental
                decresce = decresce + 1
            else:
                #se houve um número maior que o outro, o vetor não está na parte decrescente
                return [-1,0];
            #verifica se o número é maior que o anterior
        elif(lista[i] > lista[i - 1]):
            #se o valor é 1, o vetor está no estágio crescente
            if cresce == 1:
                #passa o ponto de mínimo do vetor
                minimo_global = lista[i-1]
                #passa o index do vetor
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

if __name__ == "__main__":
    lista = [21,11,10,2,5,9]
    tamanho = len(lista)
    numero_e_index = turning_number(lista,tamanho)
    #numero_e_index = [1,5]
    if (numero_e_index[0] == -1):
        print("The input is not an unimodal array")
    else:
        print("The index of the turning number is {}".format(numero_e_index[1]))


