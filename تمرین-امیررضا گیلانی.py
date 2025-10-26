#جمع
print(2 + 3)
print(10 + 5)
print(-4 + 9)
print(1.5 + 2.3)
print(7 + 0)
print(100 + 250)
print(12 + 8 + 5)
print(20 + (-10))
print(44 + (-12))
print(444 + (-45))

#تفریق
print(10 - 3)
print(7 - 9)
print(-5 - 2)
print(4.5 - 1.2)
print(100 - 50)
print(0 - 8)
print(25 - 10 - 5)
print(20 - 42 - 5)
print(90 - 45 - 5)
print(21 - 5 - 3)

#ضرب
print(2 * 3)
print(5 * -4)
print(1.5 * 2)
print(0 * 100)
print(10 * 10)
print(55 * 3)
print(3 * -35)
print(1.4 * 55)
print(34 * 100)
print(10 * 40)

#تقسیم
print(10 / 2)
print(9 / 3)
print(7 / 2)
print(5.5 / 2)
print(100 / 25)
print(4 / 67)
print(456 / 5)
print(143 / 34)
print(46 / 3)
print(269 / 456)

#جمع با تابع
def add(a, b):
    return a + b

print(add(2, 3))
print(add(10, 5))
print(add(-4, 9))
print(add(1.5, 2.3))
print(add(7, 0))
print(add(100, 250))
print(add(12, 8))
print(add(20, -10))
print(add(25, 6))
print(add(40, -18))

#تفریق با تابع
def subtract(a, b):
    return a - b

print(subtract(10, 3))
print(subtract(7, 9))
print(subtract(-5, 2))
print(subtract(4.5, 1.2))
print(subtract(100, 50))
print(subtract(0, 8))
print(subtract(25, 10))
x, y = 15, 4
print(subtract(x, y))
print(subtract(12, -3))
print(subtract(100, 75))

#ضرب با تابع
def multiply(a, b):
    return a * b

print(multiply(2, 3))
print(multiply(5, -4))
print(multiply(1.5, 2))
print(multiply(0, 100))
print(multiply(10, 10))
a, b = 7, 8
print(multiply(a, b))
print(multiply(3, (4 + 2)))
print(multiply(2, 2 * 2))
print(multiply(12, 0.5))
print(multiply(65, 20))

#تقسیم با تابع
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(9, 3))
print(divide(7, 2))
print(divide(5.5, 2))
print(divide(100, 25))
a, b = 12, 4
print(divide(a, b))
print(divide(20, (2 * 5)))
print(divide(15, 3 * 5))
print(divide(8, 0.5))
x, y = 50, 10
print(divide(x, y))

#مقایسه بزرگ و کوچک بودن اعداد
def is_greater(a, b):
    return a > b

def is_smaller(a, b):
    return a < b

def is_equal(a, b):
    return a == b

def is_not_equal(a, b):
    return a != b

def is_greater_equal(a, b):
    return a >= b

def is_smaller_equal(a, b):
    return a <= b

print(is_greater(10, 5))        
print(is_greater(2, 8))        
print(is_smaller(3, 7))       
print(is_smaller(9, 1))       
print(is_equal(4, 4))          
print(is_equal(6, 9))          
print(is_not_equal(5, 2))     
print(is_not_equal(10, 10))     
print(is_greater_equal(8, 8))   
print(is_smaller_equal(3, 3))  












