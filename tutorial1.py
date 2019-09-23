nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]

# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)

# n^2 for each in n in nums
# my_list = [n*n for n in nums]
# print(my_list)

# my_list = map(lambda n: n*n, nums)
# print(my_list)

# I want n for each n in nums if n is even
# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

# my_list = [n for n in nums if n%2 ==0]
# print(my_list)

# my_list = filter(lambda n: n%2 == 0, nums)
# print(my_list)

# Want a letter num pair for each letter and each number
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# # print(my_list)

# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# # print(zip(names, heros))

# # my_dict = {}
# # for name, hero in zip(names, heros):
# #     my_dict[name] = hero
# # print(my_dict)

# dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(dict)

# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)

nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# my_gen = (n*n for n in nums)

# for i in my_gen:
#     print(i)

# li = [9,1,8,2,7,3,6,4,5]

# li.sort()

# print(li)

# li = [-6,-5,-4,1,2,3]

# s_li = sorted(li, key=abs)
# print(s_li)

# for i in range(1, 11):
#     sentence = 'the value is {:03}'.format(i)
#     print(sentence)

# pi = 3.14159265

# sentence = 'pi is equal to {:.4f}'.format(pi)
# print(sentence)

# sentence = '1 mb is equal to {:,.2f} bytes'.format(1000**2)
# print(sentence)

import datetime
my_date = datetime.datetime(2016, 9, 14, 12, 30, 45)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)