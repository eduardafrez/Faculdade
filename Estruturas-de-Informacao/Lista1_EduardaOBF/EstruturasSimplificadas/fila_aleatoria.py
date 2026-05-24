from EstruturasSimplificadas import Fila
from random import randrange

class FilaAleatoria(Fila):
    # escreva o método remove que remove um elemento aleatório da fila
    # fique atento, pois se você remover diretamente um elemento aleatório
    # sua implementação será O(n), onde n é o tamanho da fila.
    # Você deve implementar este método de forma que ele seja O(1).
    def remove(self, i = 0):
        if self.size() == 0:
            raise

        x = randrange(self.size())
        self.fila[x], self.fila[-1] = self.fila[-1], self.fila[x]
        return self.fila.pop()
        
        # e escreva sua resposta
        # CUIDADO: o pass da linha acima faz o programa de teste entrar 
        # em loop infinito. Por quê?
        
        
