class node:
    def __init__(self, v, p = None):
        self.value = v
        self.parent = p
        self.left = None
        self.right = None
        self.height = 1
class avl_tree:
    def __init__(self):
        self.root = None
        self.last = None
    def balanse(self, x): # rotations
        if not x:
            return
        left_h = x.left.height if x.left else 0
        right_h = x.right.height if x.right else 0
        x.height = max(left_h, right_h) + 1
        diff = left_h - right_h
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
                if self.balanse(self.last): # if balance True once - change heights for all nodes!
                    self.last = self.last.parent.parent
                else:
                    self.last = self.last.parent
        else:
            self.root = node(x)
            self.last = None
    def remove_max(self, x): # remove max from left subtree
        if x == None:
            return None
        start = x
        while x:
            last = x
            x = x.right
        if last == start:
            last.parent.left = last.left
        elif last.left:
            last.parent.right = last.left
            last.left.parent = last.parent
        else:
            last.parent.right = None
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
                    if temp:
                        temp.parent = parent
                else:
                    temp = parent.right = self.last.right
                    if temp:
                        temp.parent = parent
            else:
                temp = self.remove_max(self.last.left)
                self.balanse(self.last.left)
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
                self.root = temp
                if self.root:
                    self.root.parent = None
            while temp:# one excess step when root
                if self.balanse(temp):
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