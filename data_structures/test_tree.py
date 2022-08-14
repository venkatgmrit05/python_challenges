# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 23:39:30 2021

@author: umave
"""
import tree



num = 40

node = tree.Node(15)
print('-'*num)

node.insert(5)
node.insert(20)
node.print_tree()
print('-'*num)

node.insert(3)
# node.insert(22)
node.print_tree()
print('-'*num)


node.insert(4)
node.insert(21)
node.print_tree()
print('-'*num)

node.insert(22)
node.print_tree()
print('-'*num)

node.insert(-4)
node.insert(-21)
node.print_tree()
print('-'*num)


node.insert(4.1)
node.insert(21.5)
node.print_tree()
print('-'*num)



a = [1,2,3,4,5]