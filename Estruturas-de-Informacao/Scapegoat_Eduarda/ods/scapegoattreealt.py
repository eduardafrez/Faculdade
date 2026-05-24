# Neste esboço de solução, optei por criar uma nova class e herdar tudo da classe ScapegoatTree.
# A classe ScapegoatTreeAlt é uma versão alternativa da ScapegoatTree que armazena e mantém
# explicitamente os tamanhos da subárvore com raiz em cada nó.
# Os testes dependem do atributo do nõ tam_sub_tree.
import math
from .utils import new_array
from .scapegoattree import ScapegoatTree
from .binarysearchtree import BinarySearchTree

def log32(q):
    return int(math.log(q, 1.5))

class ScapegoatTreeAlt(ScapegoatTree, BinarySearchTree):
    class Node(BinarySearchTree.Node):
        def __init__(self, x):
            super(ScapegoatTreeAlt.Node, self).__init__(x)
            self.tam_sub_tree = 1

        def update_sizeSTree(self):
            self.tam_sub_tree = 1 + (self.left.tam_sub_tree if self.left else 0) + (self.right.tam_sub_tree if self.right else 0)

        def __str__(self):
            return str(self.x) + ":" + str(self.tam_sub_tree)

    def _new_node(self, x):
        u = ScapegoatTreeAlt.Node(x)
        return u

    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x, u.tam_sub_tree
            u = self.next_node(u)

    def rebuild(self, u):
        if u is self.nil:
            return
        ns = self._size(u)
        p = u.parent
        a = new_array(ns)
        self.pack_into_array(u, a, 0)
        if p == self.nil:
            self.r = self.build_balanced(a, 0, ns)
            self.r.parent = self.nil
        elif p.right == u:
            p.right = self.build_balanced(a, 0, ns)
            p.right.parent = p
        else:
            p.left = self.build_balanced(a, 0, ns)
            p.left.parent = p

    def path(self, u): 
        if u is not None:
            self.path(u.left)
            size = 1 + self._size(u.left) + self._size(u.right)
            u.tam_sub_tree = size
            print(f" Height ({u.x}) node: {size} nodes.")
            self.path(u.right)

    def add(self, x):
        (u, d) = self.add_with_depth(x)
        self.path(self.r)
        if d > log32(self.q):
            w = u.parent
            while 3 * self._size(w) <= 2 * self._size(w.parent):
                if w.parent is None:
                    break
                w = w.parent
            if w.parent is not None:
                self.rebuild(w.parent)
        return d >= 0
    
    def remove(self, x):
        if super(ScapegoatTreeAlt, self).remove(x):
            if 2 * self.n < self.q:
                self.rebuild(self.r)
                self.q = self.n
            self.path(self.r)
            return True
        return False
    
    def _update_sizeSTree(self, u):
        while u != self.nil:
            u.update_sizeSTree()
            u = u.parent

    def build_balanced(self, a, i, ns):
        if ns == 0:
            return self.nil
        m = ns // 2        
        a[i+m].left = self.build_balanced(a, i, m)
        if a[i+m].left != self.nil:
            a[i+m].left.parent = a[i+m]
        a[i+m].right = self.build_balanced(a, i+m+1, ns-m-1)
        if a[i+m].right != self.nil:
            a[i+m].right.parent = a[i+m]
        return a[i+m]