#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:46:02 2021

@author: Marine Girardey
"""
class TreeNode:
    """
    Binary Tree class
    Attributes
    ----------
    data :
        Class to create a binary tree, add or delete nodes.
    """

    def __init__(self: object, data):
        """Class constructor.
        Parameters
        ----------
        data : Any
            The value of the given node.

        Returns
        -------
        None
            A class instance.
        """
        self.data = data
        self.right_child = None
        self.left_child = None

    def add_node(self, added_node):
        """
        Add nodes to the tree at a given position.
        Parameters
        ----------
        add_node : TreeNode
            The new node to be added.
        target_data : Any

        Returns
        -------
        None
        """

        if self.data:
            if added_node < self.data:
                if self.left_child is None:
                    self.left_child = TreeNode(added_node)
                else:
                    self.left_child.add_node(added_node)
            elif added_node > self.data:
                if self.right_child is None:
                    self.right_child = TreeNode(added_node)
                else:
                    self.right_child.add_node(added_node)
        else:
            self.data = added_node

    def delete_node(self, data):
        """
        Delete all node(s) value == data
        Parameters
        ----------
        data : searched data to delete.
        """

        # if self doesn't exist, just return it
        if self is None:
            return self
    	# Find the node in the left subtree	if node_to_delete value is less than self
        if self.data > data:
            self.left_child = root.delete_node(data)
    	# Find the node in right subtree if node_to_delete value is greater than self
        elif self.data < data:
            self.right_child = self.delete_node(data)
    	# Delete the node if self.value == node_to_delete
        else:
    	# If there is no right children delete the node and new root would be self.left
            if not self.right_child:
                temp = self.right_child
                return temp
    	# If there is no left children delete the node and new root would be root.right
            if not self.left_child:
                temp = self.left_child
                return temp
            temp = self.right_child
            min_val = temp.data
            while temp.left_child:
                temp = temp.left_child
                min_val = temp.data
            # Delete the minimum node in right subtree
            self.right_child = self.delete_node(data)
        return self

    def print_tree_node(self):
        """
        Function to print the binary tree.
        Parameters
        ----------
        """
        if self.right_child:
            self.right_child.print_TreeNode()
        print(self.data)
        if self.left_child:
            self.left_child.print_TreeNode()

    def is_leaf(self):
        """
        Return True if leaf and False if None.
        Parameters
        ----------
        """
        return self.right_child is None and self.left_child is None

    def __str__(self):
        if self.is_leaf():
            return str(self.data)
        else:
            return "["+ str(self.left_child) +";"+ str(self.right_child) +"]:"+ str(self.data)

# on insert
# si y'a un fils a droite et a gauche on en ajoute un
# insert : on ajoute un de ses fils ou petit fils si ca existe deja
# delete sur noeud, le noeud droit prend sa position
# bonus: chaine de caractere qui represente l'arbre

class Tree:
    """
    Class to represent binary trees.
    Attributes
    ----------
    root: Tree Node
    """

    def __init__(self: object, root_node):
        self.root_node = root_node

    def traversal_deep(self):
        """
        Print self.root_node.
        Attributes
        ----------
        """
        print(self.root_node)

# def delete_node(self,node_to_delete):
if __name__ == "__main__":
    root = TreeNode('10')
    n1 = TreeNode('15')
    n2 = TreeNode('8')
    root.right_child = n1
    root.left_child = n2

    root.print_tree_node()
    # print(root.add_node('11'))
    # print(root.is_leaf())
    # print(n1.is_leaf())
    # root.add_node('11')

    root.delete_node('10')
    root.print_tree_node()

# n0 = tree_node('NO')
# n1 = tree_node('N1')
# n2 = tree_node('N2')
# n0.right = n1
# n0.left = n2

# n0.print_tree_node()
# n0.print_tree_node()

# n0.is_leaf()
# n1.is_leaf()
