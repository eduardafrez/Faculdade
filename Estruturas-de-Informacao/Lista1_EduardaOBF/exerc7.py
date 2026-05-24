from EstruturasSimplificadas import FilaPrioridade

def exerc7():
    # Ler uma linha por vez. Então imprimir todas as linhas ordenadas por
    # tamanho, com a linha mais curta em primeiro. No caso em que duas linhas
    # tenham o mesmo tamanho, resolva sua ordem usando a regra de ordenação alfabética. 
    # as linhas duplicadas devem ser impressas o mesmo número de vezes 
    # que aparecem na entrada.
    try:
        arq = open('in7.txt', 'r')
    except:
        print('Erro ao abrir arquivo de entrada!!')
        return

    fila = FilaPrioridade()

    for i in arq:
        fila.add(i.strip())
    
    while fila.size() > 0:
        print(fila.remove())


if __name__ == "__main__":
    exerc7()
