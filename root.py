#Это первая программа на Python в репозитории
"""Эта программа поможет вам вычислить квадратный корень из любого числа
Попробуйте ее усовершенствовать, например, добавив обработку исключений
Обратите также внимание на комментарии. Желательно комментировать
все изменения кода, которые Вы вносите.
Задание:
1. Добавьте проверку введенной пользователем переменной на принадлежность
   ко множеству чисел (что данные, которые ввел пользователь не являются
   символами отличными от цифр). Реализовать это можно с помощью оператора try,
   который выполняет обработку исключений (ошибок) Например так:
   a = input()
   try:
       if a == "Exit" or a == "exit":
           break
       b = int(a)
       c = b ** 0.5
       print(c)
       except ValueError as err:
           print(err).
3. Добавьте обработку исключений - при возникновении ошибки из-за неправильно
   введеного значения пользователем, программа должна продолжить работу,
   запросив у пользователя еще одно число.
4. Не забывайте добавлять комментарии к вашему коду.
"""

while True:
    a = input("Введите число: ")
    try:
        b=int(a)
        c = b ** 0.5
        print(c)
    except ValueError as err:
        print(err)
        continue

