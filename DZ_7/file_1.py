#1.
#Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

# def reversed_generator(my_list):
#     for _ in range(len(my_list)):
#         yield my_list[-1]
#         my_list.pop()
# my_new_list = reversed_generator([1, 2, 3, 4, 5])
# for i in my_new_list:
#     print(i)

#2.
#Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл

my_list = [1, 2, 3, 4, 5]
new_list = list(x ** 2 for x in my_list if x % 2 == 0)
print(new_list)

new_list_2 = []
for x in my_list:
    if x % 2 == 0:
        new_list_2.append(x ** 2)
print(new_list_2)

#3.
#Напишіть функцію-генератор для отримання n перших простих чисел.

# def func_generator(n):
#     counter = 0
#     num = 2
#     while counter < n:
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield num
#             counter += 1
#         num += 1
# a = func_generator(9)
# for f in a:
#     print(f)