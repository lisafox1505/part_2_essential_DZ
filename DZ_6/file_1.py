#1.
# iterable = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# for i in iterable:
#     print(i)

#2.
from example_5 import main
main()

#3.
# class IterNumberRevers:
#     def __init__(self, my_list):
#         self.my_list = my_list
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if abs(self.index) > len(self.my_list):
#             raise StopIteration
#         save_num = self.my_list[self.index]
#         self.index -= 1
#         return save_num
#
# obj = iter(IterNumberRevers([1, 2, 3, 4, 5]))
#
# while True:
#     try:
#         print(obj.__next__())
#     except StopIteration:
#         print("StopIteration")
#         break

