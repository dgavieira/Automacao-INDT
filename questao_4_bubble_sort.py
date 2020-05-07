
entrada = "10 8 2 3 5 1 20 305 030"

#usando apenas funcoes built-in
def string_para_lista(entrada):
    #convertendo a string para lista utilizando o método split
    lista_de_string = entrada.split() #essa lista é uma lista em que os itens são strings, eu preciso que eles sejam do
    # tipo int para o bubble sort funcionar corretamente
    lista_numerica = [] #criando uma lista vazia que receberá os itens em formato inteiro
    for i in range(len(lista_de_string)): #varrendo a lista de strings
       t = int(lista_de_string[i]) #convertendo para tipo inteiro item a item
       lista_numerica.append(t) #acrescentando elemento a elemento
    return lista_numerica

def bubble_sort(lista_numerica):
    n = len(lista_numerica) #determina o tamanho da lista
    for i in range(n-1): #varrendo a lista
        for j in range (0, n-i-1):
            if lista_numerica[j] > lista_numerica[j+1]:
                lista_numerica[j], lista_numerica[j+1] = lista_numerica[j+1], lista_numerica[j]
    return lista_numerica

def lista_para_string(lista):
    #convertendo a lista ordenada para string
    saida = ' '.join(map(str,lista))
    return saida

if __name__ == "__main__":
    lista_numerica = string_para_lista(entrada)
    print(lista_numerica)

    lista_numerica = bubble_sort(lista_numerica)
    print(lista_numerica)

    saida = lista_para_string(lista_numerica)
    print(saida)

