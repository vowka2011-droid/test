# import random


# zagadonoe_chislo = random.randint(1, 100)
# ugadonoe_chislo = 0
# print(zagadonoe_chislo)
# while ugadonoe_chislo!=zagadonoe_chislo:
#     ugadonoe_chislo = int(input('введи число от 1 до 100 \n'))
#     if ugadonoe_chislo>zagadonoe_chislo:
#         print('меньше')
#     else:
#         print('больше')

# print('ты угадал')

N = int(input('какой высоты ёлка '))
zvezda = input('введи значек ')
zvezda_3 = zvezda
space = ' '
for i in range(N):
    space *= N-i-1
    print(space, zvezda, sep='')
    zvezda += 2*zvezda_3
    space = ' '