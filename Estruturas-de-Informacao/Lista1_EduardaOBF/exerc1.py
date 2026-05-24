from EstruturasSimplificadas import Pilha

def exerc1(nome_arq = "in1.txt"):
    # Leia a entrada de uma linha de cada vez e, em seguida, escreva as 
    # linhas em ordem inversa, de modo que a última linha de entrada 
    # seja impressa primeiro, depois a segunda última linha de entrada, 
    # e assim por diante.

    try :
        arq_in = open(nome_arq, "r")
    except IOError:
        print("Erro ao abrir arquivo de entrada.")
        return
    
    # Escreva aqui sua resposta para o exercício 1. Não esqueça de usar a função strip() 
    # para remover os espaços em branco no início e no fim da string.
    # ATENÇÃO: não use a função readlines() para ler o arquivo de entrada.
    # Você deve usar a estrutura simplificada Pilha, Fila, Deque, Sset, Uset ou FilaPrioridade
    pilha = Pilha()

    for i in arq_in:
        pilha.push(i.strip())
    
    while pilha.size() >0:
        print(pilha.pop())

    # Fim da sua resposta para o exercício 1.
    # fechar arquivo de entrada
    arq_in.close()

if __name__ == "__main__":
    exerc1()
