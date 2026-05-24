from EstruturasSimplificadas import Pilha

def exerc2(nome_arq = 'in2.txt'):
   # Ler as primeiras 50 linhas de uma entrada e então escrevê-las na ordem
   # reversa. Ler as próximas 50 linhas e então escrevê-las em ordem reversa.
   # Fazer isso até que não existam mais linhas a serem lidas, neste ponto as
   # linhas restantes devem ser impressas em ordem reversa.
   # Em outras palavras, sua saída vai começar com a linha de número 50,
   # então a 49, 48 e assim por diante até a primeira linha. Isso será seguido
   # pela linha de número 100, seguida pela 99 98 até a linha 51, e assim por diante.
   # Seu código nunca deverá ter armazenado mais de 50 linhas.

    try:
        arq = open(nome_arq, "r")
    except IOError:
        print("Erro ao abrir arquivo de entrada.")
        return

    # Escreva aqui sua resposta para o exercício 2. Não esqueça de usar a função strip()
    # para remover os espaços em branco no início e no fim da string.
    # ATENÇÃO: não use a função readlines() para ler o arquivo de entrada.
    # Sua saída deve ser escrita usando a função print().
    # IMPORTANTE: Seu código nunca deverá ter armazenado mais de 50 linhas.
    # Você deve usar a estrutura simplificada Pilha, Fila, Deque, SSet, USet ou FilaPrioridade
    pilha = Pilha()
    j = 0
    for i in arq:
        pilha.push(i.strip())
        j += 1
        if (j % 50) == 0:
            for i in range(50):
                print(pilha.pop())
    
    while pilha.size() > 0:
        print(pilha.pop())

    # Fim da sua resposta para o exercício 2.

    # fechar arquivo de entrada
    arq.close()

if __name__ == "__main__":
    exerc2()
