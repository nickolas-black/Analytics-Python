#класс окружности с атрибутом радиуса
class circle:
    global pi
    pi = 3.14
    # конструктор класса
    def __init__(self, radius):
      self.radius = radius
    # метод рассчета диаметра окружности
    def diameter(self):
      return self.radius*2
    # метод для расчета длины окружности
    def length(self):
      return 2*self.radius*pi
    # метод для расчета площади
    def area(self):
        return pi*self.radius**2

#класс прямоугольник с атрибутами длина и ширина
class Rectangle:
  global pi
  pi = 3.14
  def __init__(self, length, width):
    if length > width:
      self.length = length
      self.width = width
    else:
      self.length = width
      self.width = length
    #рассчет площади прямоугольника
  def s(self):
    return self.length * self.width
    #расчет диагонали прямоугольника
  def diagonal(self):
    return (self.length**2 + self.width**2)**.5
    #расчет радиуса описанной вокруг прямоугольника окружности
  def radius_opis(self):
    return ((self.length**2 + self.width**2)**.5)/2
    #расчет площади описанной окружности
  def s_opis(self):
    return pi*((self.length**2 + self.width**2)**.5)/2
    #расчет площади вписанной окружности
  def s_vpis(self):
    return pi*(self.width/2)**2             #радиус равен половине (ширины) прямоугольника
    #расчет длины окружности вписанной окуржности
  def l_vpis(self):
    return 2*pi*self.width
    #расчет длины окружности описанной окружности
  def l_opis(self):
    return 2*pi*((self.length**2 + self.width**2)**.5)/2

#класс треугольник с тремя катетами
class Triangle:
    global pi
    pi = 3.14

    # конструктор класса
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.c = h


# метод рассчета площади треугольник
    def area_tr(self):
        p = (self.a + self.b + self.c) / 2
        z = self.a * self.b * self.c
        r = z / 4 * (p * ((p - self.a) * (p - self.b) * (p - self.c)) ** .5)
        return z / (r * 4)

# метод для расчета длины описанной окружности
    def len_tr(self):
        p = (self.a + self.b + self.c) / 2
        z = self.a * self.b * self.c
        r = z / 4 * (p * ((p - self.a) * (p - self.b) * (p - self.c)) ** .5)
        return 2 * r * pi
# метод для расчета радиуса описанной окружности
    def rad_tr(self):
        p = (self.a + self.b + self.c) / 2
        z = self.a * self.b * self.c
        return z / 4 * (p * ((p - self.a) * (p - self.b) * (p - self.c)) ** .5)	
		
#класс прямоугольный параллелепипед с атрибутами длина основания, ширина основания, высота. Унаследовавший часть от класс прямоугольника

class Pr_paral(Rectangle):
  global pi
  pi = 3.14
  def __init__(self, length, width, height):
      self.length = length
      self.width = width
      self.height = height
    #рассчет площади 
  def s(self):
    a = self.length * self.width
    b = self.length*self.height
    c = self.width*self.height
    return (a + b + c)*2
    #расчет диагонали
  def diagonal(self):
    return (self.length**2 + self.width**2 + self.height**2)**.5
  # расчет объема параллелепипеда
  def volume(self):
    return self.length*self.width*self.height

