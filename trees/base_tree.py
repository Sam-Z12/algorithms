class Tree:

    class Position:

        def element(self):
            raise NotImplementedError('Must be implemented by subclass')

        def __eq__(self, other) -> bool:
            raise NotImplementedError('Must be implemented by subclass')
        
        def __ne__(self, other) -> bool:
            return not (self == other)

    def root(self):
        raise NotImplementedError('Must be implemened by subclass')
    
    def parent(self):
        raise NotImplementedError('Must be implemented by subclass')

    def num_childen(self):
        raise NotImplementedError('Must be implemented by subclass')

    def children(self):
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('Must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_childen(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
             return 1 + self.depth(self.parent(p))

    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    
    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)

class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('Must be implemented by subclass')
    
    def sibling(self, p):
        parent  = self.parent(p)
        if parent == None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
 
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)