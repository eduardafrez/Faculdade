"""A doubly-linked list implementation with O(1+min{i, n-i}) update time"""
from .base import BaseList

class DLList(BaseList):

    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None
            self.prev = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.n = 0
        self.dummy = DLList.Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def get_node(self, i):
        if i < self.n/2:
            p = self.dummy.next
            for _ in range(i):
                p = p.next
        else:
            p = self.dummy
            for _ in range(self.n, i, -1):
                p = p.prev
        return p

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.get_node(i).x

    def set(self, i, x): #@ReservedAssignment
        if i < 0 or i >= self.n: raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def _remove(self, w):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1

    def remove(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        self._remove(self.get_node(i))

    def add_before(self, w, x):
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i, x):
        if i < 0 or i > self.n:    raise IndexError()
        self.add_before(self.get_node(i), x)

    def __iter__(self):
        u = self.dummy.next
        while u != self.dummy:
            yield u.x
            u = u.next

# Implemente o método rotate(r) que “rotaciona” uma DLList de modo que o 
# item i da lista se torne o item (i + r) mod n. Este método deve executar 
# em um tempo O(1 + min{r, n − r}) e não deve modificar nenhum nó na lista. 
# Você deve completá-lo sem alocar novos nós ou arrays temporários. 
# Tudo pode ser feitos apenas manipulando os valores de prev e next dos nós existentes.

    def rotate(self, r):
        if self.n == 0:  # Lista vazia
            return
        
        r = r % self.n  # Ajusta r dentro do intervalo

        if r == 0:  # não rotaciona
            return
            # Salva os ponteiros antigos
        old_dummy_next = self.dummy.next
        old_dummy_prev = self.dummy.prev

        if r <= self.n // 2:            #para r menos que a metade do numero de elementos
                # Atualiza next do dummy  
            self.dummy.next = self.get_node(self.n-r)
                # atualiza o prev do dummy
            self.dummy.prev = self.get_node(self.n-r-1)

                # Atualiza o prev do novo começo para o dummy
            self.get_node(self.n-r).prev = self.dummy
                # Atualiza o next do novo final para o dummy
            self.get_node(self.n-r-1).next = self.dummy
            
        else:                                            #para r maior que metade do numero de elementos
                # atualiza o next do dummy
            self.dummy.next = self.get_node(r)
                # atualiza o prev do dummy
            self.dummy.prev = self.get_node(r-1)

                # Atualiza o prev do novo começo para o dummy
            self.get_node(r).prev = self.dummy
                # Atualiza o next do novo final para o dummy
            self.get_node(r-1).next = self.dummy
        
            # Atualiza os ponteiros do antigo começo e fim
        self.get_node(0).prev = old_dummy_prev
        self.get_node(self.n).next = old_dummy_next
        