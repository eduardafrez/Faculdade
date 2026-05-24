'''
An array-based list implementation with O(1+min{i,n-i}) amortized update time.

Stores the list in an array, a, so that the i'th list item is stored
at a[(j+i)%len(a)].

Uses a doubling strategy for resizing a when it becomes full or too empty.
'''
from .utils import new_array
from .base import BaseList

class ArrayDeque(BaseList):
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.a = new_array(1)
        self.j = 0
        self.n = 0

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.a[(i+self.j)%len(self.a)]

    def set(self, i, x):
        if i < 0 or i >= self.n: raise IndexError()
        y = self.a[(i+self.j)%len(self.a)]
        self.a[(i+self.j)%len(self.a)] = x
        return y

    def add(self, i, x): 
        if i < 0 or i > self.n: raise IndexError()
        if self.n == len(self.a): self._resize()
        if i < self.n/2:
            self.j = (self.j-1) % len(self.a)
            for k in range(i):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k+1)%len(self.a)]
        else:
            for k in range(self.n, i, -1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k-1)%len(self.a)]
        self.a[(self.j+i)%len(self.a)] = x
        self.n += 1

    def remove(self, i): 
        if i < 0 or i >= self.n: raise IndexError()
        x = self.a[(self.j+i)%len(self.a)]
        if i < self.n / 2:
            for k in range(i, 0, -1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k-1)%len(self.a)]
            self.j = (self.j+1) % len(self.a)
        else:
            for k in range(i, self.n-1): 
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k+1)%len(self.a)]
        self.n -= 1
        if len(self.a) >= 3*self.n: self._resize()
        return x
  
    def _resize(self):
        b = new_array(max(1, 2*self.n))
        for k in range(self.n):
            b[k] = self.a[(self.j+k)%len(self.a)]
        self.a = b
        self.j = 0
    
    def rotate (self, r):
        if r == 0 or self.n == 0:  #caso numero de elementos do arrey ou o numero de rotações for 0, nada será alterado
            return
        r = r % self.n    #tira modulo para que o numero de rotações não ultrapasse o numero de elementos

        if self.n == len(self.a):           #caso o numero de elementos seja igual ao tamanho do array, define um novo j
            self.j = (self.j - r) % len(self.a)       
            return
 
        if r > (self.n // 2):      #caso o nº de rotações seja maior que metade de n, copia (n-r) elementos do inicio da lista, para o fim da lista.
            for i in range (self.n - r):     
                self.a[(self.j + self.n + i) % len(self.a)] = self.a[(self.j+ i) % len(self.a)] 
            
            self.j = (self.j + self.n - r) % len(self.a)   #novo j é definido para o primeiro elemento que não foi copiado, para que externamente o array seja acessado com a rotação
            return
        else:                               #caso o nº de rotações seja menor ou igual a metade de n, copia r elementos do fim da lista, para inicio da lista.
            for i in range(r):  
                i += 1
                self.a[(self.j-i) % len(self.a)] = self.a[(self.j + self.n - i) % len(self.a)]
            
            self.j = (self.j - r) % len(self.a)     #novo j é definido para o ultimo elemento copiado
