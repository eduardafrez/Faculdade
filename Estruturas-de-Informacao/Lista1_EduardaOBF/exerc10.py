from EstruturasSimplificadas import Pilha

def exerc10(string):
    # Uma string casada é uma sequência de caracteres {, }, (, ), [, e ] que
    # estejam casados corretamente. Por exemplo, {{()[]}} é uma string
    # casada, porém {{()]} não é, pois o segundo { casa com um ]. Mostre
    # que uma pilha pode ser usada para isso de tal modo que dada uma string
    # de tamanho n, você possa determinar se ela é uma string casada no tempo O(n).
    # Escreva aqui sua resposta para o exercício 10. Sua resposta deve retornar 
    # True ou False de acordo com o resultado do casamento da string.
    pilha = Pilha()
    b = {'[':']','{':'}', '(':')'}

    for i in string:
        if i in b.keys():
            pilha.push(i)
        elif i in b.values():
            a = pilha.pop()
            if b[a] != i:
                print(f"{string} Não é uma string casada")
                return False
    if pilha.size() == 0:
        print(f"{string} É uma string casada")
        return True
    else:
        print(f"{string} Não é uma string casada")
        return False
    
    


    

if __name__ == "__main__":
    exerc10("{{()[]}") # Não é uma string casada
    exerc10("{{()[]}}") # É uma string casada
    exerc10("{{()]}") # Não é uma string casada
    exerc10("{{()[]}}{") # Não é uma string casada
    exerc10("{{()[]}}{}") # É uma string casada
    exerc10("{{()[]}}{}{") # Não é uma string casada
    exerc10("{{()[]}}{}{}") # É uma string casada
    exerc10("{{()[]}}{}{}{") # Não é uma string casada
    exerc10("{{()[]}}{}{}{}") # É uma string casada
    exerc10("{{()[]}}{}{}{}{") # Não é uma string casada
    exerc10("") # É uma string casada
