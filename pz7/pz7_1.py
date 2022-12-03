# Вариант 25
# 1. Дано целое число N (>0) и строка S. Преобразовать строку S в строку длины N
# следующим образом: если длина строки S больше N, то отбросить первые символы,
# если длина строки S меньше N, то в ее начало добавить символы «.» (точка).

n = input()
s = input()       #задаем число и строку с помощью ввода с клавиатуры

while (type(n) != int): #запуская цикл while проверка типа данных переменных
    try:
        n = int(n) #Перобразовываем наши введённые значения с целое число
        if len (s) > n:
            s = s[len (s) - n:]
            print (s)
        else:
            print('.' * (n - len (s)), s, sep='')

    except ValueError:
        print('Вы ввели неверное значение!')      #если введено неверное значение задача пойдет заново
        n = input('введите число ')
        s = input('введите строку ')