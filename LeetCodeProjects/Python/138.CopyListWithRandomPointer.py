# A linked list of length n is given such that each node contains an
# additional random pointer, which could point to any node in the list, or null.
#
# Construct a deep copy of the list. The deep copy should consist of
# exactly n brand new nodes, where each new node has its value set to
# the value of its corresponding original node. Both the next and random
# pointer of the new nodes should point to new nodes in the copied list
# such that the pointers in the original list and copied list represent
# the same list state. None of the pointers in the new list should
# point to nodes in the original list.
#
# For example, if there are two nodes X and Y in the original list,
# where X.random --> Y, then for the corresponding two nodes x and
# y in the copied list, x.random --> y.
#
# Return the head of the copied linked list.
#
# The linked list is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random
# pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.
#
#
#
# Example 1:
#
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:
#
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:
#
#
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]


# Definition for a Node.
import collections


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        old_to_new_nodes_dict = dict()
        current = result_list = None
        while head:
            node = Node(head.val)
            if not result_list:
                current = result_list = node
            else:
                current.next = node
                current = current.next
            old_to_new_nodes_dict[head] = node
            head = head.next

        for old, new in old_to_new_nodes_dict.items():
            if old.random:
                new.random = old_to_new_nodes_dict[old.random]

        return result_list


if __name__ == '__main__':
    # [[7,null],[13,0],[11,4],[10,2],[1,0]]
    node_5 = Node(1, None, None)
    node_4 = Node(10, node_5, None)
    node_3 = Node(11, node_4, None)
    node_2 = Node(13, node_3, None)
    node_1 = Node(7, node_2, None)
    node_2.random = node_1
    node_5.random = node_1
    node_3.random = node_5
    node_5.random = node_1
    node_4.random = node_3

    head = node_1
    Solution().copyRandomList(head)
