'''
Задача 2: Найдите сумму цифр трехзначного числа.

'''

# n = int(input())
# a = n // 100
# b = n % 100 // 10
# c = n % 10
# print(f'{a + b + c} ({a} + {b} + {c})')



'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

'''

# s = int(input())
# print(int(s / 6), int(s * 2 / 3), int(s / 6))



'''
Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

'''

# n = int(input())
# a = n // 100000 + n % 100000 //10000 + n % 10000 // 1000
# b = n % 1000 // 100 + n % 100 // 10 + n % 10
# if a == b:
#     print('yes')
# else:
#     print('no')


'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
на два прямоугольника).

'''

# m, n, k = int(input()), int(input()), int(input())
# if k % m == 0 or k % n == 0:
#     print('yes')
# else:
#     print('no')