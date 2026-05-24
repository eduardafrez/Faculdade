from EstruturasSimplificadas import Pilha
from EstruturasSimplificadas import Fila

def exerc11():
    # Suponha que você tenha uma Pilha, s, que suporta somente as operações
    # push(x) e pop(). Mostre como, usando somente uma fila FIFO, f, você
    # pode reverter a ordem de todos os elementos em s.
    try:
        arq = open('in4.txt', 'r')
    except:
        print('Erro ao abrir arquivo!')
        return 

    s = Pilha()
    f = Fila()

    print('--inicio da Pilha S--')
    for i in arq:
        s.push(i.strip())
        print(i.strip())
    print('--Fim da pilha--\n \n--inicio da Fila F--')

    while True:
        try:
            f.add(s.pop())
        except IndexError:
            break
    
    while f.size()>0:
        print(f.remove())
    print('--Fim da fila--')

   
if __name__ == "__main__":
    exerc11()
