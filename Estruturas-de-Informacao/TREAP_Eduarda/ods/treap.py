import random
from .binarysearchtree import BinarySearchTree

class Treap(BinarySearchTree):
    class Node(BinarySearchTree.Node):
        def __init__(self, x):
            super(Treap.Node, self).__init__(x)
            self.p = random.random()  # Prioridade aleatória
            self.size = 1  # Tamanho da subárvore
            self.x = x  # Chave
            self.left = self.right = self.parent = None

        def __str__(self):
            return "[%r,%f]" % (self.x, self.p)

    def __init__(self, iterable=[]):
        super(Treap, self).__init__(iterable)

    def _new_node(self, x):
        return Treap.Node(x)

    def add(self, x):
        u = self._new_node(x)
        if self.add_node(u):
            self.bubble_up(u)
            return True
        return False

    def bubble_up(self, u):
        while u != self.r and u.parent.p > u.p:
            if u.parent.right == u:
                self.rotate_left(u.parent)
            else:
                self.rotate_right(u.parent)
        if u.parent is None:  # Atualizar raiz
            self.r = u
        self._update_ancestors_size(u)  # Atualizar tamanhos

    def remove(self, x):
        u = self._find_last(x)
        if u is not None and u.x == x:
            self.trickle_down(u)
            self.splice(u)
            self._update_ancestors_size(u.parent)  # Atualizar tamanhos após remoção
            return True
        return False

    def trickle_down(self, u):
        while u.left or u.right:
            if u.left is None:
                self.rotate_left(u)
            elif u.right is None:
                self.rotate_right(u)
            elif u.left.p < u.right.p:
                self.rotate_right(u)
            else:
                self.rotate_left(u)
        if u.parent is None:  # Atualizar raiz
            self.r = None

    def get(self, i):
        if self.r is None or i < 0 or i >= self.size():
            return None
        return self._get(self.r, i)

    def _get(self, node, i):
        if node is None:
            return None
        left_size = node.left.size if node.left else 0

        if i < left_size:  # Índice está na subárvore esquerda
            return self._get(node.left, i)
        elif i == left_size:  # Índice corresponde ao nó atual
            return node.x
        else:  # Índice está na subárvore direita
            return self._get(node.right, i - left_size - 1)

    def _update_size(self, u):
        """Atualiza o tamanho do nó u com base nos tamanhos dos filhos."""
        if u is not None:
            u.size = 1
            if u.left:
                u.size += u.left.size
            if u.right:
                u.size += u.right.size

    def _update_ancestors_size(self, u):
        """Atualiza o tamanho de todos os ancestrais do nó u."""
        while u is not None:
            self._update_size(u)
            u = u.parent

    def rotate_left(self, u):
        super().rotate_left(u)
        self._update_size(u)
        self._update_size(u.parent)

    def rotate_right(self, u):
        super().rotate_right(u)
        self._update_size(u)
        self._update_size(u.parent)