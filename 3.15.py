# import re
# # s = 'My name is Mike'
# # print(s.split(sep=','))
# #
# #
# # p = re.compile(r'\W+')
# # print(p.split(s))
#
# # p = re.compile('(blue|white|red)')
# # print(p.sub('color', 'blue socks and red shoes'))
# # print(p.sub('color', 'blue socks and red shoes', count=1))
# # print(p.subn('color', 'blue socks and red shoes', count=1))
# #
# #
# #
# # def hexrepl(match):
# #     value = int(match.group())
# #     return hex(value)
# #
# # p = re.compile(r'\d')
# # print(p.sub(hexrepl, '12345 55 11 test test2 '))
#
#
#
#
#
#
# #
# # s = '<html><head><title>Title</title></head></ttml>'
# #
# # print(re.match('<.*>', s))
# # print(re.match('<.*?>', s))
# #
# # s = ('a', 'b', 'c')
# # t = '{}, {}, {}'.format(s)
# # print(t)
# #
# # ('{}, {}, {}'.format('a', 'b' 'c'))
#
#
#
# # print(int(100), hex(100), oct(100), bin(100))
# # print('{0:d}, {0:#x}, {0:#o}, {0:#b}'.format(100))
# #
# # for i in range(20):
# #     for base in 'bdX':
# #         print('{:5{base}}'.format(i, base=base), end=' ')
# #     print()
# #
# #
#
#
# # print('s')
# # print(str('t'))
# # print(repr('t'))
# #
# # import datetime
# # d = datetime.datetime.now()
# # print(d)
# # print(str(d))
# # print(repr(d))
#
#
#
# # print('{!r} {} {!s}'.format('test', 'test1', 'test2'))
#
#
# class Point(object):
#     def __str__(self):
#         return 'Point ####'
#
# p = Point()
#
# print('{0!r} {0} {!0s}'.format(p))



# class Node(object):
#     def __init__(self, value: int) -> None:
#         self.value = value
#         self.right = None
#         self.left = None
#
#
# def insert(node:Node, value: int) -> Node:
#     if node is None:
#         return Node(value)
#
#     if value < node.value:
#         node.left = insert(node.left, value)
#
#     else:
#         node.right = insert(node.right, value)
#     return node
#
#
# if __name__ == '__main__':
#
#     root = None
#     root = insert(root, 5)
#     root = insert(root, 6)
#     root = insert(root, 3)
#     print(root.value)
#     print(root.right.value)


#
# #
# # class Node(object):
# #     def __init__(self, value:int) -> None:
# #         self.value = value
# #         self.right = None
# #         self.left = None
# #
# # def insert(node:Node, value:int) -> Node:
# #     if node is None:
# #         return Node(value)
# #
# #     if value < node.value:
# #         node.right = insert(node.right, value)
# #
# #     else:
# #         node.left = insert(node.left, value)
# #
# #     return node
# #
# # if __name__ == '__main__':
# #     root = None
# #     root = insert(root, 5)
# #     print(root.value)
#
#
#
#
#
# class Node(object):
#     def __init__(self, value:int) -> None:
#         self.value = value
#         self.right = None
#         self.left = None
#
#
# class BinarySearchTree(object):
#     def __init__(self) -> None:
#         self.root = None
#     def insert(self, value: int) -> None:
#
#         if self.root is None:
#             self.root = Node(value)
#
#
#         def _insert(node: Node, value: int) -> Node:
#             if node is None:
#                 return Node(value)
#
#             if value < node.value:
#
#                 node.left = _insert(node.left, value)
#             else:
#                 node.right = _insert(node.right, value)
#             return node
#
#
#         _insert(self.root, value)
#     #
#     #
# # def inorder(node:Node) -> None:
# #     if node is not None:
# #         inorder(node.left)
# #         print(node.value)
# #         inorder(node.right)
# #
#
#
#
#
#
#
#
#
#     def inorder(self, node: Node) -> None:
#
#         def _inorder(node: Node) -> None:
#             if node is not None:
#                 _inorder(node.left)
#                 print(node.value)
#                 _inorder(node.right)
#
#         _inorder(self.root)
#
# # def search(node:Node, value:int) -> bool:
# #     if node is None:
# #         return False
# #
# #     if node.value == value:
# #         return True
# #
# #     elif node.value < value:
# #         return search(node.right, value)
# #
# #     elif node.value > value:
# #         return search(node.left, value)
# #
#
#
#
# # def min_value(node: Node) -> Node:
# #     current = node
# #     while current.left is not None:
# #         current = current.left
# #     return current
#
#
#     def min_value(self, node: Node) -> Node:
#         current = node
#         while current.left is not None:
#             current = current.left
#         return current
#
#     def search(node:Node, value: int) -> bool:
#
#         def _search(node:Node, value: int) -> bool:
#             if node is None:
#                 return False
#
#             if node.value == value:
#                 return True
#
#
#             elif node.value > value:
#                 return _search(node.left, value)
#
#             elif node.value < value:
#                 return _search(node.right, value)
#
#
# #
# # def min_value(node:Node):
# #     current = node
# #     while current is not None:
# #         current = current.left
# #     return current
#
#
#     def remove(self, value: int) -> Node:
#         def _remove(node: Node, value: int) -> Node:
#             if node is  None:
#                 return node
#             if value < node.value:
#                 node.left = _remove(node.left, value)
#             elif value > node.value:
#                 node.right = _remove(node.right, value)
#             else:
#                 if node.right is None:
#                     return node.left
#                 elif node.left is None:
#                     return node.left
#
#
#                 temp = self.min_value(node.right)
#                 node.value = temp.value
#                 node.right = _remove(node.right, temp.value)
#             return node
#         _remove(self.root, value)
#
#
#
#
#
#
#
#
#
# if __name__ == '__main__':
#
#     root = None
#     binary_tree = BinarySearchTree()
#     binary_tree.insert(8)
#     binary_tree.inorder()

    # root = None
    # root = insert(root, 8)
    # root = insert(root, 6)
    # root = insert(root, 3)
    # # print(root.value)
    # # print(root.left.value)
    # # print(root.left.left.value)
    #
    #
    # inorder(root)
    #
    # print(search(root, 8))


#
# from typing import List
#
# def bubble_sort(numbers: List[int]) -> List[int]:
#
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         for j in range(len_numbers - i - 1):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#     return numbers
#
# if __name__ == '__main__':
#     nums = [1,5,3,13,4,4,9]
#
#     print(bubble_sort(nums))









# from typing import List
#
# def select_sort(numbers:List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         min_idx = i
#         for j in range(i+1, len_numbers):
#             if numbers[min_idx] > numbers[j]:
#                 min_idx = j
#         numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]
#     return numbers
#
#
# if __name__ == '__main__':
#     nums = [1,7,4,5,5,9]
#     print(select_sort(nums))



# from typing import List
#
# def select_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         min_idx = i
#         for j in range(i+1, len_numbers):
#             if numbers[min_idx] > numbers[j]:
#                 min_idx = j
#         numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]
#
#     return numbers
#
# if __name__ == '__main__':
#     nums = [1,34,4,8,9]
#     print(select_sort(nums))





# from typing import List
#
# def insert_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(1, len_numbers):
#         temp = numbers[i]
#         j = i - 1
#         while j > 0 and numbers[j] >temp:
#             numbers[j+1] = numbers[j]
#             j -= 1
#
#         numbers[j+1] = temp
#     return numbers
# if __name__ == '__main__':
#
#     nums = [1,3,4,11,4]
#     print(insert_sort(nums))

#
# from typing import List
#
# def insert_sort(numbers:List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(1, len_numbers):
#         temp =numbers[i]
#         j = i-1
#         while j >= 0 and numbers[j] > temp:
#             numbers[j+1] = numbers[j]
#             j -= 1
#         numbers[j+1] = temp
#     return numbers
#
# if __name__ == '__main__':
#     nums = [44,5,9,8,6,1]
#
#     print(insert_sort(nums))

# from typing import List
#
#
# def insert_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(1, len_numbers):
#         j = i -1
#         temp = numbers[i]
#         while j >= 0:
#             print(j, end=' ')
#             # numbers[j+1] = numbers[j]
#             j -= 1
#         print()
#         # numbers[j+1] = temp
#     # return numbers
#
# if __name__ == '__main__':
#     nums = [21,2,4,4,6]
#     print(insert_sort(nums))


#
#
#
#
# # import re
# # # m = re.match('a.c', 'abc')
# # # print(m.span())
# # # print(m.group())
# #
# # # m = re.findall('a.c', 'test and test abc')
# # # print([w.group() for w in m])
# #
# # # m = re.match('[a-cA-Z0-9]', '1')
# # # m = re.match('\w', '1')
# #
# # # m = re.match('\d','a')
# # # m = re.match('\D','a')
# # # m = re.match('(abc)+','abc')
# #
# # m = re.match('\?', '?')
# #
# # m = re.search('^abc', 'test abc')
# #
#
#
# #
# # import re
# #
# # s = ('')
# #
# # m = re.match(?P<region>r'[\w]('
# #               ''(?P<stack_name>+:[\d])+:stack/[≠]')
#
#
# # # import re
# # #
# # # s = 'My name is Mike'
# # # print(s.split(sep=' '))
# # #
# # #
# # #
# # #
# # # # p = re.compile(r'\w+')
# # # # print(p.split(s))
# # #
# # # p = re.compile('(blue|white|red)')
# # # print(p.sub('color', 'blue socks and red shoes'))
# # # print(p.subn('color', 'blue socks and red shoes', count=1))
# # #
# # #
# # # def hexrepl(match):
# # #     value = int(match.group())
# # #     return hex(value)
# # #
# # #
# # #
# # # p = re.compile(r'\d')
# #
# #
# # #
# # # t = (1,3,4)
# # # # r = '{0[0]}'.format(t)
# # # # print(r)
# # #
# # #
# # # # t = '{0}, {2}, {1}'.format('a', 'b', 'c')
# # # r = '{}, {}'.format(*t)
# # # print(r)
# # #
# # #
# # # d = {'name': 'jun', 'family':'saksai'}
# # # r = '{0[name]} {0[family]}'.format(d)
# # # print(r)
# #
# #
# #
# #
# # r = '{:<30}'.format('left')
# # print(r)
#
# print(int(100), hex(100), oct(100), bin(100))


#
# for i in range(30):
#     for base in 'bdX':
#         print('{:5{base}}'.format(i, base=base), end=' ')
#     # print()







# print('s')
#
# print(repr('s'))


# import datetime
#
# d = datetime.datetime.r



# # print('{!r} {} {!s}'.format('test', 'test1', 'test'))
#
#
# class Point(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     def __str__(self):
#         return 'Point<object>'
#     def __str__(self):
#         return 'Point?????   ({}, {}) '.format(self.x, self.y)
#
#
#
# p = Point(10,200)
# print('{0!r} {0} {0!s}'.format(p))
# print('{0} {0} {0!s}'.format(p))
# print('{0!s} {0} {0!s}'.format(p))


# import json
# import pprint
#
#
#
# l =['apple', 'orange', 'banana', 'peach', 'mango']
# l.insert(0, l[:])
# # print(l)
#
#
# pp = pprint.PrettyPrinter(incident=4, width40)
# print(p)


# # import json
# # import pprint
# #
# l = ['apple', 'orange', 'banana', 'peach','mango']
# # # print(l.insert(0, l[:]))
# #
# #
# #
# d = {'a': 'A', 'b': 'B', 'c': {'x': {'y': 'U'}}}
# #
# #
# #
# #
# # print(json.dumps(d, indent=4))
#
# # import pprint
# # # d.insert(0, d[:])
# # pp = pprint.PrettyPrinter(indent=88,
# #                           width=48,
# #                           compact = True)
# # pp.pprint(l)
#
#
#
#
#
#
# #
# #
# # print(0 | 0)
# # print(0 & 1)
# # print(1 & 1)
# #
# # print(0 ^ 0)
# # print(4 ^ 43)
#
#
# print(bin(0))
#
# print(bin(~0))
# print(bin(~0))
# print(bin(1 << 3))


import enum


