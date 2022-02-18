#3завдання 1
# def mysumm(param1, param2):
#3 sum = param1 + param2
# print(sum)
#
# mysumm(3, 2)
# mysumm(-3, -6)
# mysumm(7, 3)

# Завдання2
# def fizz_buzz(number):
# if number % 3 == 0 and number % 5 == 0:
#           print("FizzBuzz")
# elif number % 3 == 0:
# print("Fizz")
# elif number % 5 == 0:
#           print("Buzz")
# else:
#3 n = str(number)
#          print(n)
#           print (type(n))
#
# fizz_buzz(4)

# Завдання 3
# def tri_area(osnova, visota):
#     space = (osnova * visota) / 2
#     print(space)
#
#
# tri_area(10, 5)

#Завдання 4
# def call_fuel(distance):
#      cal = distance * 10
#      if cal > 100:
#          print(cal)
#      else:
#          print("100")
# call_fuel(123)

#Завдання 5
# def both(num1, num2):
#     if num1 > 0 and num2 > 0:
#         print(True)
#     elif num1 < 0 and num2 < 0:
#         print((False))
#     else:
#         print(False)
#
#
# both(0, -2)

#Завдання 6
# def int_within_bounds(number, lower_bound, upper_bound):
#     if type(number) == int:
#         if upper_bound > number >= lower_bound:
#             print(True)
#         else:
#             print(False)
#
#     else:
#         print(False)
#
#Завдання 7
# int_within_bounds(3, 1, 9)
# int_within_bounds(6, 1, 6)
# int_within_bounds(4.5, 3, 8)
#
# def makes10(a, b):
#     if a == 10 or b == 10 or a + b == 10:
#         print(True)
#     else:
#         print(False)
#
#
# makes10(9, 10)
# makes10(9, 9)
# makes10(1, 9)

#Завдання_8
#def squares_sum(num):
#     sum = 0
#     while num > 0:
#         sum = sum + (num * num)
#         num = num - 1
#     print(sum)
# squares_sum(3)

# Завдання 9
#def sum_even_nums_in_range(start, stop):
#   sum = 0
#   while start <= stop+1:
#       if start % 2 == 0:
#        sum = start + 1
#        if start > stop:
#            break
#            print(sum)
#
#sum_even_nums_in_range(10, 20)

#Завдання_10
#def mean(numbers):
#    s = str(numbers)
#    k = 0
#    for i in range(len(s)):
#        k = k + int(s[i])
#    return k / len(s)
#
#
#print(mean(42))
#print(mean(12345))
#print(mean(666))



