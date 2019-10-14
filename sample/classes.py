class EmptyClass(object):
    pass


class ClassName(Parent1, Parent2):
    """Создание нового класса"""
    variable = 0 # Свойство класса

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        print("Конструктор класса")

    def __del__(self):
        print("Деструктор класса")

    def method(self):
        # Метод класса
        pass

    @staticmethod
    def st_hello():
        print("Hello, World!")

    @classmethod
    def cl_hello(cls):
        print("Hello, World!")

    def __add__(self, other):
        return self.variable + other

    def _private(self):
        print("Это внутренний метод объекта")

    def __veryprivate(self):
        pass

    def getvalue(self): # получение значения атрибута
        return self._value

    def setvalue(self, value): # установка значения атрибута
        self._value = value

    def delvalue(self): # удаление атрибута
        del self._value


class NewClass(ClassName):
    pass


pntr = ClassName
obj1 = ClassName()
obj1 = ClassName(10, 20)


obj1.method()
obj1.variable


# Динамическое изменение класса
def squareMethod(self, x):
  return x*x


EmptyClass.square = squareMethod
obj2 = EmptyClass()
obj2.square(5) # 25

ClassName.st_hello() # Hello, World!
obj1.st_hello() # Hello, World!

ClassName.cl_hello()

obj1._private() # Это внутренний метод объекта
obj1.__veryprivate() # AttributeError

obj1._ClassName__veryprivate()


class Polymorf(ClassName):

    def method(self):
        return 0

    def methodSuper(self):
        super(Polymorf, self).method()




try:
    a = 1/0
except ZeroDivisionError:
    a = 0
except ValueError:
    a = 1
else:
    print("Упешно")
finally:
    print("Завершение блока")


try:
    a = 1/0
except:
    a = 0



def power(x):
    return x**2

assert power(2) == 4, "Ответ не сходится"


file = open("name.txt", '+') # r,w,x,a - чтение, запись, создание, дозапись

file.read()
file.read(n)

file.readline()

file.write()
file.writelines()

file.close()


with open('name.txt', '+') as file:
    file.write('Hello\n')

del obj
