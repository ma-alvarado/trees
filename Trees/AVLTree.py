'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files.
'''

from Trees.BinaryTree import BinaryTree, Node
from Trees.BST import BST

class AVLTree(BST):

    def __init__(self, xs=None):


        super().__init__()
        if xs:
            self.insert_list(xs)


    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)


    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):         
        if AVLTree.balance_factor(node) not in [-1,0,1]:
            return False
        if node:
            if node.left and node.right:
                return AVLTree._is_avl_satisfied(node.left) and AVLTree._is_avl_satisfied(node.right)
            if node.left and node.right is None:
                return AVLTree._is_avl_satisfied(node.left)    
            if node.right and node.left is None:
                return AVLTree._is_avl_satisfied(node.right)
        return True
 


    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None or node.right is None:
            return node
        
        nodeone = Node(node.right.value)
        nodeone.right = node.right.right

        leftNode = Node(node.value)
        leftNode.left = node.left
        leftNode.right = node.right.left

        nodeone.left = leftNode

        return nodeone


    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None or node.left is None:
            return node

        node1 = Node(node.left.value)
        node1.left = node.left.left
        
        rightNode = Node(node.value)
        rightNode.right = node.right
        rightNode.left = node.left.right

        node1.right = rightNode

        return node1

    def insert_list(self,xs):
        for item in xs:
            self.insert(item)

    def insert(self, value):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''

        if self.root is None:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(value, self.root)

    @staticmethod
    def updateBalance(node):

        if AVLTree._balance_factor(node) > 1:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
            else:
                return AVLTree._right_rotate(node)
        elif AVLTree._balance_factor(node) < -1:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
            else:
                return AVLTree._left_rotate(node)
        else:
            return node

    @staticmethod
    def _insert(value,node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                AVLTree._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                AVLTree._insert(value, node.right)
        else:
            print("Already in the tree.")

        if AVLTree._is_avl_satisfied(node) == False:
            node.left = AVLTree.updateBalance(node.left)
            node.right = AVLTree.updateBalance(node.right)
            return AVLTree.updateBalance(node)
        else:
            return node





