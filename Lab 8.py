#q1-3
class Rectangle:
    def __init__(self, width=10, height=10):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def __str__(self):
        return str(self.__width) + " x " + str(self.__height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width,self.__height)

    def get_area(self):
        area = self.__width * self.__height
        return area

    def get_perimeter(self):
        perimeter = 2*(self.__width + self.__height)
        return perimeter

#q4-8
class QuadraticEquation:
    def __init__(self, coeff_a=1, coeff_b=1, coeff_c=1):
        self.__coeff_a = coeff_a
        self.__coeff_b = coeff_b
        self.__coeff_c = coeff_c

    def get_coeff_a(self):
        return self.__coeff_a

    def get_coeff_b(self):
        return self.__coeff_b

    def get_coeff_c(self):
        return self.__coeff_c

    def get_discriminant(self):
        discriminant = self.__coeff_b**2 - (4 * self.__coeff_a * self.__coeff_c)
        return discriminant

    def has_solution(self):
        if self.get_discriminant() < 0:
            return False
        else:
            return True

    def get_root1(self):
        import math
        if self.get_discriminant() >= 0:
            r1 = (-self.__coeff_b + math.sqrt(self.get_discriminant())) / (2 * self.__coeff_a)
            return r1
        else:
            return 0

    def get_root2(self):
        import math
        if self.get_discriminant() >= 0:
            r2 = (-self.__coeff_b - math.sqrt(self.get_discriminant())) / (2 * self.__coeff_a)
            return r2
        else:
            return 0

    def __str__(self):
        if self.get_discriminant() < 0:
            return "The equation has no roots."
        elif self.get_discriminant() == 0:
            return "The root is {:.2f}.".format(self.get_root1())
        elif self.get_discriminant() > 0:
            return "The roots are {:.2f} and {:.2f}.".format(self.get_root1(), self.get_root2())

#q9-10
class Product:
    def __init__(self, product_id, product_name, product_price = 1):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_price = product_price

    def __str__(self):
        return "{}(id = {}), ${}".format(self.__product_name, self.__product_id, self.__product_price)

    def set_product_price(self, product_price):
        if product_price >= 0:
            self.__product_price = product_price

    def get_product_price(self):
        return self.__product_price

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def get_product_name(self):
        return self.__product_name

    def set_product_id(self, product_id):
        if product_id > 0:
            self.__product_id = product_id

    def get_product_id(self):
        return self.__product_id

#q11
class Dog:
    def __init__(self, age):
        self.__age = age

    def __str__(self):
        return "I am a Dog. My age is {}".format(self.__age)

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def speak(self, repeat = 1):
        return print("Woof " * repeat)

#q12
class Robot:
    def __init__(self, name, position = (0, 0)):
        self.__name = name
        self.__x_position = position[0]
        self.__y_position = position[1]
        self.__position = position

    def move_to(self, x_position, y_position):
        self.__x_position = x_position
        self.__y_position = y_position
        self.__position = self.__x_position, self.__y_position

    def up(self, displacement):
        self.__y_position += displacement
        self.__position = self.__x_position, self.__y_position

    def right(self, displacement):
        self.__x_position += displacement
        self.__position = self.__x_position, self.__y_position

    def __str__(self):
        return "{} is at {}".format(self.__name, self.__position)

def main():
    robot1 = Robot("Marvin")
    print(robot1)
    robot1.move_to(5, 11)
    print(robot1)
    robot1.move_to(1, 2)
    print(robot1)
    robot1.up(3)
    robot1.right(-4)
    print(robot1)

    robot1 = Robot("Marvin", (19, 3))
    print(robot1)
    robot1.up(3)
    robot1.right(4)
    print(robot1)
    return

main()
