#avl_tree with sum support
class node:
    def __init__(self, v, p = None):
        self.value = v
        self.parent = p
        self.left = None
        self.right = None
        self.height = 1
        self.sum = v
class avl_tree:
    def __init__(self):
        self.root = None
        self.last = None
    def _balance(self, x): # rotations
        if not x:
            return
        left_h = x.left.height if x.left else 0
        right_h = x.right.height if x.right else 0
        x.height = max(left_h, right_h) + 1
        diff = left_h - right_h
        x.sum = (x.left.sum if x.left else 0) + (x.right.sum if x.right else 0) + x.value
        if abs(diff) == 2:
            if x == self.root: # create overroot
                temp = node(None)
                temp.left = x
                x.parent = temp
            if diff > 0: # left rotation ####################################################################
                left_h = x.left.left.height if x.left.left else 0
                right_h = x.left.right.height if x.left.right else 0
                if left_h < right_h: # big left
                    if x.parent.left == x:
                        x.parent.left = x.left.right
                        x.left.right.parent = x.parent
                        x.left.right = x.left.right.left
                        if x.left.right:
                            x.left.right.parent = x.left
                        x.parent.left.left = x.left
                        x.left.parent = x.parent.left
                        x.left = x.parent.left.right
                        if x.left:
                            x.left.parent = x
                        x.parent.left.right = x
                        x.parent = x.parent.left
                    else:
                        x.parent.right = x.left.right
                        x.left.right.parent = x.parent
                        x.left.right = x.left.right.left
                        if x.left.right:
                            x.left.right.parent = x.left
                        x.parent.right.left = x.left
                        x.left.parent = x.parent.right
                        x.left = x.parent.right.right
                        if x.left:
                            x.left.parent = x
                        x.parent.right.right = x
                        x.parent = x.parent.right
                    x.height -= 2
                    x.parent.height += 1
                    x.parent.left.height -= 1
                    x.sum = (x.left.sum if x.left else 0) + (x.right.sum if x.right else 0) + x.value
                    y = x.parent.left
                    y.sum = (y.left.sum if y.left else 0) + (y.right.sum if y.right else 0) + y.value
                    x.parent.sum = x.sum + y.sum + x.parent.value
                else: # small left
                    if x.parent.left == x:
                        x.parent.left = x.left
                        x.left.parent = x.parent
                        x.left = x.parent.left.right
                        if x.left:
                            x.left.parent = x
                        x.parent.left.right = x
                        x.parent = x.parent.left
                    else:
                        x.parent.right = x.left
                        x.left.parent = x.parent
                        x.left = x.parent.right.right
                        if x.left:
                            x.left.parent = x
                        x.parent.right.right = x
                        x.parent = x.parent.right
                    x.height -= 2
                    x.sum = (x.left.sum if x.left else 0) + (x.right.sum if x.right else 0) + x.value
                    x.parent.sum = x.sum + x.parent.left.sum + x.parent.value
            else: # right rotation ##########################################################################
                left_h = x.right.left.height if x.right.left else 0
                right_h = x.right.right.height if x.right.right else 0
                if left_h > right_h: # big right
                    if x.parent.left == x:
                        x.parent.left = x.right.left
                        x.right.left.parent = x.parent
                        x.right.left = x.right.left.right
                        if x.right.left:
                            x.right.left.parent = x.right
                        x.parent.left.right = x.right
                        x.right.parent = x.parent.left
                        x.right = x.parent.left.left
                        if x.right:
                            x.right.parent = x
                        x.parent.left.left = x
                        x.parent = x.parent.left
                    else:
                        x.parent.right = x.right.left
                        x.right.left.parent = x.parent
                        x.right.left = x.right.left.right
                        if x.right.left:
                            x.right.left.parent = x.right
                        x.parent.right.right = x.right
                        x.right.parent = x.parent.right
                        x.right = x.parent.right.left
                        if x.right:
                            x.right.parent = x
                        x.parent.right.left = x
                        x.parent = x.parent.right
                    x.height -= 2
                    x.parent.height += 1
                    x.parent.right.height -= 1
                    x.sum = (x.left.sum if x.left else 0) + (x.right.sum if x.right else 0) + x.value
                    y = x.parent.right
                    y.sum = (y.left.sum if y.left else 0) + (y.right.sum if y.right else 0) + y.value
                    x.parent.sum = x.sum + y.sum + x.parent.value
                else: # small right
                    if x.parent.left == x:
                        x.parent.left = x.right
                        x.right.parent = x.parent
                        x.right = x.parent.left.left
                        if x.right:
                            x.right.parent = x
                        x.parent.left.left = x
                        x.parent = x.parent.left
                    else:
                        x.parent.right = x.right
                        x.right.parent = x.parent
                        x.right = x.parent.right.left
                        if x.right:
                            x.right.parent = x
                        x.parent.right.left = x
                        x.parent = x.parent.right
                    x.height -= 2
                    x.sum = (x.left.sum if x.left else 0) + (x.right.sum if x.right else 0) + x.value
                    x.parent.sum = x.sum + x.parent.right.sum + x.parent.value
            if x == self.root: # destroy overroot
                x.parent.parent = None
                self.root = x.parent
            return True
        else:
            return False
    def add(self, x):
        if self.find(x):
            return
        if self.last:
            if x < self.last.value:
                self.last.left = node(x, self.last)
            else:
                self.last.right = node(x, self.last)
            while self.last:
                if self._balance(self.last): # if balance True once - change heights for all nodes in chain!
                    self.last = self.last.parent.parent
                else:
                    self.last = self.last.parent
        else:
            self.root = node(x)
            self.last = None
    def _remove_max(self, x): # remove max from left subtree
        if x == None:
            return None
        start = x
        start_parent = start.parent
        while x:
            last = x
            x = x.right
        if last == start:
            last.parent.left = last.left
        else:
            if last.left:
                last.parent.right = last.left
                last.left.parent = last.parent
            else:
                last.parent.right = None
            temp = last.parent
            while temp != start_parent:
                if self._balance(temp):
                    temp = temp.parent.parent
                else:
                    temp = temp.parent
        return last
    def remove(self, x):
        if not self.find(x):
            return
        if self.last:
            if self.last == self.root: # create overroot
                overroot = node(None)
                overroot.left = self.root
                self.root.parent = overroot
            temp = parent = self.last.parent
            if self.last.left == None:
                if parent.left == self.last:
                    temp = parent.left = self.last.right
                else:
                    temp = parent.right = self.last.right
                if temp:
                    temp.parent = parent
                else:
                    temp = parent
            else:
                temp = self._remove_max(self.last.left)
                temp.left = self.last.left
                if temp.left:
                    temp.left.parent = temp
                temp.right = self.last.right
                if temp.right:
                    temp.right.parent = temp
                if parent.left == self.last:
                    parent.left = temp
                else:
                    parent.right = temp
                temp.parent = parent
            if self.last == self.root:
                if temp.value != None:
                    self.root = temp
                    self.root.parent = None
                else:
                    temp = self.root = None
            while temp:# one excess step when root?
                if self._balance(temp):
                    temp = temp.parent.parent
                else:
                    temp = temp.parent
            self.last = None
    def find(self, x):
        t = self.root
        while t:
            self.last = t
            if x < t.value:
                t = t.left
            elif x > t.value:
                t = t.right
            else:
                return True
        return False
    @property
    def nodes(self): # iterativeInorder
        node = self.root
        nodes, stack = [], []
        while stack or node != None:
            if node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                nodes.append(node)
                node = node.right
        return nodes
    def sum(self, larg, rarg):
        if self.root:
            temp = self.root
            tail = 0
            state1 = True
            state2 = False
            if temp.value < larg:
                tail -= temp.value + (temp.left.sum if temp.left else 0)
                temp = temp.right
            else:
                temp = temp.left
            while temp:
                if temp.value < larg:
                    if state1:
                        tail -= temp.sum
                        state1 = False
                    temp = temp.right
                    state2 = True
                else:
                    if state2:
                        tail += temp.sum
                        state2 = False
                    temp = temp.left
                    state1 = True
            temp = self.root
            state1 = True
            state2 = False
            if temp.value > rarg:
                tail -= temp.value + (temp.right.sum if temp.right else 0)
                temp = temp.left
            else:
                temp = temp.right
            while temp:
                if temp.value > rarg:
                    if state1:
                        tail -= temp.sum
                        state1 = False
                    temp = temp.left
                    state2 = True
                else:
                    if state2:
                        tail += temp.sum
                        state2 = False
                    temp = temp.right
                    state1 = True
            return self.root.sum + tail
        else:
            return 0
