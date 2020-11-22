import random, string

class Point:

    max_x = 100
    max_y = 100

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return f'{self.name}[{self.x};{self.y}]'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __pow__(self, exp):
        return self.x ** exp, self.y ** exp

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    @staticmethod
    def random_generate():
        min = -20
        max = 30
        return random.choice(string.ascii_uppercase), random.randint(min, max), random.randint(min, max)

    @classmethod
    def change_max_x(cls, new_max_x):
        cls.max_x = new_max_x

    @classmethod
    def change_max_y(cls, new_max_y):
        cls.max_y = new_max_y

    @classmethod
    def change_max_xy(cls, new_max_x, new_max_y):
        cls.max_x = new_max_x
        cls.max_y = new_max_y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        try:
            x = int(x)
        except ValueError:
            raise ValueError('The value you are trying to assign to x is not a number.')
        if x > self.max_x:
            raise Exception(f'The value you are trying to assign to x is greater than maximum possible value, which is: {Point.max_x}')
        elif x < self.max_x * - 1:
            raise Exception(f'The value you are trying to assign to x is lower than minimum possible value, which is: {Point.max_x * - 1}')
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        try:
            y = int(y)
        except ValueError:
            raise ValueError('The value you are trying to assign to y is not a number.')
        if y > self.max_y:
            raise Exception(f'The value you are trying to assign to y is greater than maximum possible value, which is: {Point.max_y}')
        elif y < self.max_y * - 1:
            raise Exception(f'The value you are trying to assign to y is lower than minimum possible value, which is: {Point.max_y * - 1}')
        else:
            self.__y = y


class Circle:

    def __init__(self, point1, point2):
        self.x1 = point1.x
        self.y1 = point1.y
        self.name1 = point1.name
        self.x2 = point2.x
        self.y2 = point2.y
        self.name2 = point2.name

    def __lt__(self, other):
        return self.diameter() < other.diameter()

    def __gt__(self, other):
        return self.diameter() > other.diameter()

    def diameter(self):
        return pow(pow(self.x1 - self.x2, 2) + pow(self.y1 - self.y2, 2), 0.5)

    def center(self):
        return (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2

    def create(self):
        if point1 == point2:
            raise Exception(f'Can not create a circle because point {point1.name} and point {point2.name} have the same coordinates.')
        else:
            return self.diameter() / 2, self.center()


class Ellipse(Circle):

    ellipse_xy = -1

    def center_ellipse(self):
        return (self.x1, self.y2), (self.x2, self.y1)

    def get_a_ellipse(self):
        if abs(self.center_ellipse()[0][1] - self.y1) > abs(self.center_ellipse()[0][0] - self.x2):
            self.ellipse_xy = 0
        else:
            self.ellipse_xy = 1
        return abs(self.center_ellipse()[0][1] - self.y1) if abs(self.center_ellipse()[0][1] - self.y1) > abs(self.center_ellipse()[0][0] - self.x2) else abs(self.center_ellipse()[0][0] - self.x2)

    def get_b_ellipse(self):
        return abs(self.center_ellipse()[0][0] - self.x2) if abs(self.center_ellipse()[0][0] - self.x2) < abs(self.center_ellipse()[0][1] - self.y1) else abs(self.center_ellipse()[0][1] - self.y1)

    def get_e_ellipse(self):
        return pow(pow(self.get_a_ellipse(), 2) - pow(self.get_b_ellipse(), 2), 0.5)

    def get_f_ellipse(self, pos, plus_minus):
        x, y = self.center_ellipse()[pos]
        if self.ellipse_xy == 1:
            if plus_minus == 'plus':
                return x + self.get_e_ellipse(), y
            else:
                return x - self.get_e_ellipse(), y
        else:
            if plus_minus == 'plus':
                return x, y + self.get_e_ellipse()
            else:
                return x, y - self.get_e_ellipse()

    def create(self):
        if self.x1 == self.x2 and self.y1 == self.y2:
            raise Exception(f'Cannot create an ellipse because point {self.name1} and point {self.name2} have the same coordinates.')
        elif abs(self.center_ellipse()[0][1] - self.y1) == abs(self.center_ellipse()[0][0] - self.x2):
            raise Exception(f'Cannot create ellipse because a = b and that means it is a circle.')
        else:
            # a, b, e, major_axis,     (S1, F1, F2)    (S2, F1, F2)
            # a, b, e, major_axis,      AS1x, AS1y, AF1x, AF1y, AF2x, AF2y      BS2x, BS2y, BF1x, BF1y, BF2x, BF2y
            return self.get_a_ellipse(), self.get_b_ellipse(), self.get_e_ellipse(), self.ellipse_xy, self.center_ellipse()[0][0], self.center_ellipse()[0][1], self.get_f_ellipse(0, 'minus')[0], self.get_f_ellipse(0, 'minus')[1], self.get_f_ellipse(0, 'plus')[0], self.get_f_ellipse(0, 'plus')[1], self.center_ellipse()[1][0], self.center_ellipse()[1][1], self.get_f_ellipse(1, 'minus')[0], self.get_f_ellipse(1, 'minus')[1], self.get_f_ellipse(1, 'plus')[0], self.get_f_ellipse(1, 'plus')[1]


class Hyperbola(Circle):

    def center_hyperbola(self):
        return (self.x1, self.y2), (self.x2, self.y1)

    def get_a_b_hyperbola(self):
        return abs(self.center_hyperbola()[0][1] - self.y1), abs(self.center_hyperbola()[0][0] - self.x2)

    def get_e_hyperbola(self):
        return pow(pow(self.get_a_b_hyperbola()[0], 2) + pow(self.get_a_b_hyperbola()[1], 2), 0.5)

    def get_f_hyperbola(self, pos, plus_minus, rotation):
        x, y = self.center_hyperbola()[pos]
        if rotation == 'horizontal':
            if plus_minus == 'plus':
                return x + self.get_e_hyperbola(), y
            else:
                return x - self.get_e_hyperbola(), y
        else:
            if plus_minus == 'plus':
                return x, y + self.get_e_hyperbola()
            else:
                return x, y - self.get_e_hyperbola()

    def create(self):
        if self.x1 == self.x2 and self.y1 == self.y2:
            raise Exception(f'Cannot create an hyperbola because point {self.name1} and point {self.name2} have the same coordinates.')
        else:
            # ((S1 F1 F2 a b) or (F1 F2 a b))    ((S2 F1 F2 a b) or (F1 F2 a b))      e
            # CS1x, CS1y, C1F1x, C1F1y, C1F2x, C1F2y, Ca1, Cb1, C2F1x, C2F1y, C2F2x, C2F2y, Ca2, Cb2, DS1x, DS1y, D1F1x, D1F1y, D1F2x, D1F2y, Da1, Db1, D2F1x, D2F1y, D2F2x, D2F2y, Da2, Db2, ec
            return self.center_hyperbola()[0][0], self.center_hyperbola()[0][1], self.get_f_hyperbola(0, 'minus', 'horizontal')[0], self.get_f_hyperbola(0, 'minus', 'horizontal')[1], self.get_f_hyperbola(0, 'plus', 'horizontal')[0], self.get_f_hyperbola(0, 'plus', 'horizontal')[1], self.get_a_b_hyperbola()[0], self.get_a_b_hyperbola()[1], \
                   self.get_f_hyperbola(0, 'minus', 'vertical')[0], self.get_f_hyperbola(0, 'minus', 'vertical')[1], self.get_f_hyperbola(0, 'plus', 'vertical')[0], self.get_f_hyperbola(0, 'plus', 'vertical')[1], self.get_a_b_hyperbola()[1], self.get_a_b_hyperbola()[0], \
                   self.center_hyperbola()[1][0], self.center_hyperbola()[1][1], self.get_f_hyperbola(1, 'minus', 'horizontal')[0], self.get_f_hyperbola(1, 'minus', 'horizontal')[1], self.get_f_hyperbola(1, 'plus', 'horizontal')[0], self.get_f_hyperbola(1, 'plus', 'horizontal')[1], self.get_a_b_hyperbola()[0], self.get_a_b_hyperbola()[1], \
                   self.get_f_hyperbola(1, 'minus', 'vertical')[0], self.get_f_hyperbola(1, 'minus', 'vertical')[1], self.get_f_hyperbola(1, 'plus', 'vertical')[0], self.get_f_hyperbola(1, 'plus', 'vertical')[1], self.get_a_b_hyperbola()[1], self.get_a_b_hyperbola()[0], self.get_e_hyperbola()


class Parabola(Circle):

    def get_parameter_parabola(self):
        if self.x1 == self.x2:
            return abs(self.y1 - self.y2) * 2
        else:
            return abs(self.x1 - self.x2) * 2

    def get_directrix_parabola(self):
        if self.x1 == self.x2:
            if self.y1 + self.get_parameter_parabola() / 2 == self.y2:
                return self.x1, self.y1 - self.get_parameter_parabola() / 2
            else:
                return self.x1, self.y1 + self.get_parameter_parabola() / 2
        else:
            if self.x1 + self.get_parameter_parabola() / 2 == self.x2:
                return self.x1 - self.get_parameter_parabola() / 2, self.y1
            else:
                return self.x1 + self.get_parameter_parabola() / 2, self.y2

    def create(self):
        if self.x1 == self.x2 and self.y1 == self.y2:
            raise Exception(f'Cannot create an hyperbola because point {self.name1} and point {self.name2} (focus) have the same coordinates.')
        elif self.x1 == self.x2 or self.y1 == self.y2:
            #   p, Dx, Dy
            return self.get_parameter_parabola(), self.get_directrix_parabola()[0], self.get_directrix_parabola()[1]
        else:
            raise Exception(f'Cannot create an parabola because point {self.name1} and point {self.name2} (focus) does not have the same coordinates for either x or y.')


#   Points

point1 = Point(5, 10, 'A')
point2 = Point(8, 15, 'B')


print(f'point1 before change  {point1}')
point1.x = -3
point1.y = 0
print(f'point1 after change   {point1}')
print(f'point2 before change  {point2}')
point2.x = 3
point2.y = 6
print(f'point2 after change   {point2}')

print(point1)
print(point1 ** 2)
print(point1 + point2)

print(f'Random generated point: {Point.random_generate()[0]}[{Point.random_generate()[1]};{Point.random_generate()[2]}]')

print('\n')

#   Circle

circle1 = Circle(point1, point2)
print('Circle with points {}[{};{}] and {}[{};{}] has center with coordinates S[{};{}] and radius of {}'.format(circle1.name1, circle1.x1, circle1.y1, circle1.name2, circle1.x2, circle1.y2, circle1.create()[1][0], circle1.create()[1][1], round(circle1.create()[0], 2)))

point1.x = 28
print(f'point1.x was changed to {point1.x}')
circle1 = Circle(point1, point2)
print('Circle with points {}[{};{}] and {}[{};{}] has center with coordinates S[{};{}] and radius of {}'.format(circle1.name1, circle1.x1, circle1.y1, circle1.name2, circle1.x2, circle1.y2, circle1.create()[1][0], circle1.create()[1][1], round(circle1.create()[0], 2)))

point3 = Point(8, 40, 'C')
point4 = Point(14, 9, 'D')
circle2 = Circle(point3, point4)
print(f'{circle1 < circle2} - Diameter of circle1 is smaller than diameter of circle2.')

print('\n')

#   Ellipse

point1.x = -5
point1.y = 0
point2.x = 0
point2.y = -3

ellipse1 = Ellipse(point1, point2)

a, b, e, major_axis, AS1x, AS1y, AF1x, AF1y, AF2x, AF2y, BS2x, BS2y, BF1x, BF1y, BF2x, BF2y = [str(x) for x in ellipse1.create()]

print('{} ellipse with points {}[{};{}] and {}[{};{}] has a first possible center of S1[{};{}], '
      'focus F1[{};{}] F2[{};{}] \nand a second possible center of S2[{};{}], focus F1[{};{}] F2[{};{}]. '
      'The major radius = {} and the minor radius = {}, eccentricity = {}.'
      ''.format('Horizontal' if int(major_axis) == 1 else 'Vertical', ellipse1.name1, ellipse1.x1, ellipse1.y1,
                ellipse1.name2, ellipse1.x2, ellipse1.y2, AS1x, AS1y, round(float(AF1x), 2), round(float(AF1y), 2), round(float(AF2x), 2), round(float(AF2y), 2), BS2x, BS2y, round(float(BF1x), 2), round(float(BF1y), 2), round(float(BF2x), 2), round(float(BF2y), 2), a, b, round(float(e), 2)))


point1.x = -3
point1.y = 0
point2.x = 0
point2.y = -10

ellipse1 = Ellipse(point1, point2)

a, b, e, major_axis, AS1x, AS1y, AF1x, AF1y, AF2x, AF2y, BS2x, BS2y, BF1x, BF1y, BF2x, BF2y = [str(x) for x in ellipse1.create()]

print('{} ellipse with points {}[{};{}] and {}[{};{}] has a first possible center of S1[{};{}], '
      'focus F1[{};{}] F2[{};{}] \nand a second possible center of S2[{};{}], focus F1[{};{}] F2[{};{}]. '
      'The major radius = {} and the minor radius = {}, eccentricity = {}.'
      ''.format('Horizontal' if int(major_axis) == 1 else 'Vertical', ellipse1.name1, ellipse1.x1, ellipse1.y1,
                ellipse1.name2, ellipse1.x2, ellipse1.y2, AS1x, AS1y, round(float(AF1x), 2), round(float(AF1y), 2), round(float(AF2x), 2), round(float(AF2y), 2), BS2x, BS2y, round(float(BF1x), 2), round(float(BF1y), 2), round(float(BF2x), 2), round(float(BF2y), 2), a, b, round(float(e), 2)))

print('\n')

#   Hyperbola

point1.x = -2
point1.y = 0
point2.x = 0
point2.y = 4

hyperbola1 = Hyperbola(point1, point2)

CS1x, CS1y, C1F1x, C1F1y, C1F2x, C1F2y, Ca1, Cb1, C2F1x, C2F1y, C2F2x, C2F2y, Ca2, Cb2, DS1x, DS1y, D1F1x, D1F1y, D1F2x, D1F2y, Da1, Db1, D2F1x, D2F1y, D2F2x, D2F2y, Da2, Db2, ec = [str(x) for x in hyperbola1.create()]

print('Hyperbola with points {}[{};{}] and {}[{};{}] has a first possible center of S1[{};{}].\n'
      'For horizontal transverse axis hyperbola -> F1[{};{}], F2[{};{}], a = {}, b = {}.\n'
      'For vertical transverse axis hyperbola   -> F1[{};{}], F2[{};{}], a = {}, b = {}.\n'
      'And a second possible center of S2[{};{}].\n'
      'For horizontal transverse axis hyperbola -> F1[{};{}], F2[{};{}], a = {}, b = {}.\n'
      'For vertical transverse axis hyperbola   -> F1[{};{}], F2[{};{}], a = {}, b = {}.\n'
      'Eccentricity = {}'.format(hyperbola1.name1, hyperbola1.x1, hyperbola1.y1, hyperbola1.name2, hyperbola1.x2, hyperbola1.y2, CS1x, CS1y,
                                 round(float(C1F1x), 2), round(float(C1F1y), 2), round(float(C1F2x), 2), round(float(C1F2y), 2), Ca1, Cb1,
                                 round(float(C2F1x), 2), round(float(C2F1y), 2), round(float(C2F2x), 2), round(float(C2F2y), 2), Ca2, Cb2,
                                 DS1x, DS1y,
                                 round(float(D1F1x), 2), round(float(D1F1y), 2), round(float(D1F2x), 2), round(float(D1F2y), 2), Da1, Db1,
                                 round(float(D2F1x), 2), round(float(D2F1y), 2), round(float(D2F2x), 2), round(float(D2F2y), 2), Da2, Db2, round(float(ec), 2)))


print('\n')

#   Parabola

point1.x = -2
point1.y = 0
point2.x = -2
point2.y = 4

parabola1 = Parabola(point1, point2)

p, Dx, Dy = [str(x) for x in parabola1.create()]
print(f'Parabola with points {point1.name}[{point1.x};{point1.y}] (vertex) and {point2.name}[{point2.x};{point2.y}] (focus) -> p = {p}, D = [{Dx};{Dy}].')