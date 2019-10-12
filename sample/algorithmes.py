"""Простейшие алгоритмы."""

# from random import randint


def maximum(*args):
    """Поиск максимума."""
    maxNum = args[0]
    for i in args:
        if i > maxNum:
            maxNum = i
    return maxNum


def minimum(*args):
    """Поиск минимума."""
    minNum = args[0]
    for i in args:
        if i < minNum:
            minNum = i
    return minNum


def sortedList(lst, direction="ascending"):
    """
    Сортировка списка.

    На вход принимает список с числовыми значениями и направление сортировки
    Аргумент direction может принимать значения:
    'ascending' (по умолчанию) и 'descending'
    """
    listIndexes = range(len(lst))
    for i in listIndexes:
        for j in listIndexes:
            if direction == "ascending":
                if lst[i] < lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
            elif direction == "descending":
                if lst[i] > lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
    return lst


def factorial(number):
    """Рекурсивный расчет факториала."""
    if number == 1:
        return number
    else:
        return number * factorial(number-1)


def fibonacci_1(length):
    """Возврат ряда чисел Фибоначчи с помощью цикла."""
    fiblst = [0, 1, 2]
    length -= 3
    while length:
        length -= 1
        fiblst.append(fiblst[-2] + fiblst[-1])
    return fiblst


def fibonacci_2(length):
    """Рекурсивный поиск числа Фибоначчи."""
    if length < 2:
        return length
    return fibonacci_2(length-1) + fibonacci_2(length-2)


def fibonacci_3(length):
    """Приближенный расчет числа Фибоначчи."""
    return ((1+5**0.5)**length - (1-5**0.5)**length)/(2**length*5**0.5)


def leapYear(year):
    """Определение високосности года."""
    if (year % 4 != 0) or (year % 100 == 0) and (year % 400 != 0):
        return False
    return True


if __name__ == "__main__":
    # Выполнение проверок

    assert maximum(1, 2, 3, 4, 5) == 5
    assert maximum(90, 12, 14, 90, 80) == 90
    assert maximum(*[1, 2, 3, 4, 5]) == 5

    assert minimum(1, 2, 3, 4, 5) == 1
    assert minimum(90, 12, 14, 90, 80) == 12
    assert minimum(*[1, 2, 3, 4, 5]) == 1

    assert sortedList([90, 12, 14, 90, 80]) == [12, 14, 80, 90, 90]
    assert sortedList([90, 12, 14, 90, 80], "descending") == [90, 90, 80, 14, 12]

    assert factorial(2) == 2
    assert factorial(5) == 120
    assert factorial(10) == 3628800

    assert fibonacci_1(10)[-1] == 55
    assert fibonacci_2(10) == 55
    assert (int(fibonacci_3(10)) == 55) is True
    assert fibonacci_3(300) == 2.2223224462942268e+62

    assert leapYear(1880) is True
    assert leapYear(2040) is True
    assert leapYear(1992) is True
    assert leapYear(1991) is False
    assert leapYear(2013) is False
    assert leapYear(1900) is False

    # print(sortedList([randint(0,100) for i in range(10)]))
    print("Success!")
