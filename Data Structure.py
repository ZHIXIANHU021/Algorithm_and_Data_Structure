from collections import deque
"""
Stack
可应用与括号配对检测
"""
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack):
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0

def brace_match(s):
    match = {'}':'{',']':'[',')':'('}
    stack = Stack()
    for i in s:
        if i in {'(','[','{'}:
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top() == match[i]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False

"""
Queue
"""
class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0
        self.front = 0

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear+1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front

def tail(file_name, n):
    with open(file_name, 'r') as f:
        q = deque(f, n)
        return q

"""
Application of Stack and Queue
Maze problem
"""
maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
dirs = [
    lambda x,y: (x+1,y),
    lambda x,y: (x-1,y),
    lambda x,y: (x,y+1),
    lambda x,y: (x,y-1)
]
def maze_path(x1,y1,x2,y2):
    """
    DFS using stack
    """
    stack = []
    stack.append((x1,y1))
    while len(stack) > 0:
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            for i in stack:
                print(i)
            return True

        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2 # 2 means this point already been passed
                # print(stack)
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    return False

def print_r(path):
    curNode = path[-1]
    real_path = []
    while curNode[2] != -1:
        real_path.append(curNode[:2])
        curNode = path[curNode[2]]
    real_path.append(curNode[:2])
    real_path.reverse()
    for node in real_path:
        print(node)

def maze_path_queue(x1,y1,x2,y2):
    """
    BFS using Queue
    """
    queue = deque()
    queue.append((x1,y1,-1))
    path = []
    while len(queue) > 0:
        curNode = queue.pop()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0],nextNode[1],len(path)-1))
                maze[nextNode[0]][nextNode[1]] = 2
    print("No path found.")
    return False

"""
Linked list
"""
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

def ceate_linked_list(ls):
    """
    Insert element from head
    """
    head = Node(ls[0])
    for ele in ls[1:]:
        node = Node(ele)
        node.next = head
        head = node
    return head

def cearte_linked_list_tail(ls):
    """
    Insert element from tail
    """
    head = Node(ls[0])
    tail = head
    for ele in ls[1:]:
        node = Node(ele)
        tail.next = node
        tail = node
    return head

def print_linkedlist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next

"""
Double linked list
"""
class D_Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prior = None

"""
Hash Table
"""
class Linkedlist:

    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkedlistIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = Linkedlist.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
            else:
                return False

    def __iter__(self):
        return self.LinkedlistIterator(self.head)

    def __repr__(self):
        return "<<"+", ".join(map(str, self)) + ">>"

class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.T = [Linkedlist() for _ in range(self.size)]

    def h(self, k):
        return k % self.size

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)

    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print("Duplicated insert.")
        else:
            self.T[i].append(k)

"""
Linux file system tree
"""
class TreeNode:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name

class FileSystemTree:
    def __init__(self):
        self.root = TreeNode("/")
        self.now = self.root

    def mkdir(self, name):
        # Name must be file name and end with "/"
        if name[-1] != "/":
            name += "/"
        node = TreeNode(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name == "..":
            self.now = self.now.parent
            return

        if name[-1] != "/":
            name += "/"

        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError("Invalid dir")

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(root):
    """
    二叉树的前序遍历
    """
    if root:
        print(root.data, end=',')
        pre_order(root.left)
        pre_order(root.right)

def in_order(root):
    """
    二叉树的中序遍历
    """
    if root:
        in_order(root.left)
        print(root.data, end=',')
        in_order(root.right)

def post_order(root):
    """
    二叉树的后序遍历
    """
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end=',')

def level_order(root):
    """
    树的层次遍历（适用于任何树）
    """
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=',')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class BST:
    def __init__(self, ls=None):
        self.root = None
        if ls:
            for val in ls:
                self.insert_no_rec(val)

    def insert(self, node, val):
        if not node:
            node = BSTNode(val)
        elif val < node.data:
            node.left = self.insert(node.left, val)
            node.left.parent = node
        elif val > node.data:
            node.right = self.insert(node.right, val)
            node.right.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BSTNode(val)
            return
        while True:
            if val < p.data:
                if p.left:
                    p = p.left
                else:
                    p.left = BSTNode(val)
                    p.left.parent = p
                    return
            elif val > p.data:
                if p.right:
                    p = p.right
                else:
                    p.right = BSTNode(val)
                    p.right.parent = p
                    return
            else:
                return

    def query(self, node, val):
        if not node:
            return None

        if node.data < val:
            return self.query(node.right, val)
        elif node.data > val:
            return self.query(node.left, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.right
            elif p.data > val:
                p = p.left
            else:
                return p
        return None

    def __remove_node_1(self, node):
        #情况1：node是叶子节点
        if not node.parent:
            self.root = None
        if node == node.parent.left:
            node.parent.left = None
        else:
            node.parent.right = None

    def __remove_node_21(self, node):
        #情况2：node只有一个left child
        if not node.parent:
            self.root = node.left
            node.left.parent = None
        elif node == node.parent.left:
            node.parent.left = node.left
            node.left.parent = node.parent
        else:
            node.parent.right = node.left
            node.left.parent = node.parent

    def __remove_node_22(self, node):
        #情况2：node只有一个right child
        if not node.parent:
            self.root = node.right
            node.right.parent = None
        elif node == node.parent.left:
            node.parent.left = node.right
            node.right.parent = node.parent
        else:
            node.parent.right = node.right
            node.right.parent = node.parent

    def delete(self, val):
        if self.root:
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.left and not node.right:
                self.__remove_node_1(node)
            elif not node.right:
                self.__remove_node_21(node)
            elif not node.left:
                self.__remove_node_22(node)
            else:
                #情况3：两个child都有
                min_node = node.right
                while min_node.left:
                    min_node = min_node.left
                node.data = min_node.data
                #删除min_node
                if min_node.right:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)

    def pre_order(self,root):
        """
        二叉树的前序遍历
        """
        if root:
            print(root.data, end=',')
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root):
        """
        二叉树的中序遍历
        """
        if root:
            self.in_order(root.left)
            print(root.data, end=',')
            self.in_order(root.right)

    def post_order(self, root):
        """
        二叉树的后序遍历
        """
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data, end=',')

    def level_order(self, root):
        """
        树的层次遍历（适用于任何树）
        """
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            print(node.data, end=',')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

class AVLTreeNode(BSTNode):
    def __init__(self, data):
        BSTNode.__init__(self, data)
        self.bf = 0

class AVLTree(BST):
    def __init__(self, ls=None):
        BST.__init__(self, ls)

    def rotate_left(self, p, c):
        s2 = c.left
        p.right = s2
        if s2:
            s2.parent = p

        c.left = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.right
        p.left = s2
        if s2:
            s2.parent = p

        c.right = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):
        # Rotate right
        g = c.left
        s3 = g.right
        c.left = s3
        if s3:
            s3.parent = c
        g.right = c
        c.parent = g

        # Rotate left
        s2 = g.left
        p.right = s2
        if s2:
            s2.parent = p
        g.left = p
        p.parent = g

        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else: # 插入的是g
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def rotate_left_right(self, p, c):
        g = c.right
        s2 = g.left
        c.right = s2
        if s2:
            s2.parent = c
        g.left = c
        c.parent = g

        s3 = g.right
        p.left = s3
        if s3:
            s3.parent = p
        g.right = p
        p.parent = g

        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def insert_no_rec(self, val):
        #和BST一样先插入再调整
        p = self.root
        if not p:
            self.root = AVLTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.left:
                    p = p.left
                else:
                    p.left = AVLTreeNode(val)
                    p.left.parent = p
                    node = p.left
                    break
            elif val > p.data:
                if p.right:
                    p = p.right
                else:
                    p.right = AVLTreeNode(val)
                    p.right.parent = p
                    node = p.right
                    break
            else: # val == p.data
                return

        # 2. update bf
        while node.parent: # node.parent not None
            if node.parent.left == node:# 传递是从左子树来的，左子树更沉了
                # update node.parent's bf -= 1
                if node.parent.bf < 0: # 原来node.parent.bf == -1, 更新后为-2
                    #看node那边沉
                    g = node.parent.parent # 为了连接旋转之后的子树
                    x = node.parent #旋转前子树的根
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # 记得把n和g连起来
                elif node.parent.bf > 0: # 原来node.parent.bf = 1, 更新后为0
                    node.parent.bf = 0
                    break
                else: # 原来的node.parent.bf = 0, 更新后为-1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else: # 传递是从右子树来的，右子树更沉了
                # 更新后的node.parent.bf += 1
                if node.parent.bf > 0: # 原来node.parent.bf = 1, 更新后为2
                    # 看node哪边沉
                    g = node.parent.parent
                    x = node.parent
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                elif node.parent.bf < 0: #原来的node.parent.bf = -1, 更新后为0
                    node.parent.bf = 0
                    break
                else: #原来node.parent.bf = 0, 更新后为1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            #连接旋转后的子树
            n.parent = g
            if g: #g not None
                if x == g.left:
                    g.left = n
                else:
                    g.right = n
                break
            else:
                self.root = n
                break

if __name__ == "__main__":
    # stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # print(stack.pop())
    # print(stack.get_top())
    # print(brace_match('[{()}(){}[]]'))
    # print(brace_match('[{()}'))
    # print(brace_match('{(})'))
    # q = Queue(5)
    # for i in range(4):
    #     q.push(i)
    # print(q.is_filled())
    # print(q.pop())
    # q.push(4)
    # q = deque([1,2,3,4,5], 5)
    # q.append(4) # rear in
    # print(q.popleft()) # front out
    # print(q)
    # q.appendleft(5) # front in
    # print(q.pop()) # rear out
    # print(q)
    # for i in tail('test.txt', 5):
    #     print(i, end='')
    # print(maze_path(1,1,8,8))
    # print(maze_path_queue(1,1,8,8))
    # ls = ceate_linked_list([1,2,3])
    # lk = cearte_linked_list_tail([1,2,3,4,5,6])
    # print_linkedlist(ls)
    # print_linkedlist(lk)
    # lk = Linkedlist([1,2,3,4,5])
    # print(lk)
    # for ele in lk:
    #     print(ele)
    # ht = HashTable()
    # ht.insert(0)
    # ht.insert(1)
    # ht.insert(4)
    # ht.insert(101)
    # # print(','.join(map(str, ht.T)))
    # print(ht.find(7))
    # tree = FileSystemTree()
    # tree.mkdir("var/")
    # tree.mkdir("bin/")
    # tree.mkdir("usr/")
    # tree.cd("bin/")
    # tree.mkdir("python/")
    # tree.cd("..")
    # print(tree.ls())
    # a = BiTreeNode("A")
    # b = BiTreeNode("B")
    # c = BiTreeNode("C")
    # d = BiTreeNode("D")
    # e = BiTreeNode("E")
    # f = BiTreeNode("F")
    # g = BiTreeNode("G")
    # e.left = a
    # e.right = g
    # a.right = c
    # c.left = b
    # c.right = d
    # g.right = f
    # root = e
    # # print(root.left.right.data)
    # pre_order(root)
    # print('\n')
    # in_order(root)
    # print('\n')
    # post_order(root)
    # print('\n')
    # level_order(root)
    import random
    ls = list(range(0, 500, 2))
    random.shuffle(ls)
    avl = AVLTree([9,8,7,6,5,4,3,2,1])
    avl.pre_order(avl.root)
    print('')
    avl.in_order(avl.root)
    # bst = BST([1,4,2,5,3,8,6,9,7])
    # print(bst.root)
    # # bst.pre_order(bst.root)
    # # print('')
    # bst.in_order(bst.root)
    # bst.delete(4)
    # bst.delete(1)
    # bst.delete(8)
    # print('')
    # bst.in_order(bst.root)
    # print(bst.query_no_rec(3).data)
    # bst.pre_order(bst.root)
    # print('')
    # bst.in_order(bst.root)
    # print('')
    # bst.post_order(bst.root)
    # print('')
    # bst.level_order(bst.root)