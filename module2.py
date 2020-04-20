# import module1, cubed
import statistics


##nums = [1, 5, 33, 12, 46, 33, 2]
##print(statistics.mean(nums))  # 18.857142857142858
##print(statistics.stdev(nums))  # 18.160658683250556 標本標準偏差
##print(statistics.variance(nums))  # 329.8095238095238 標本標準分散
##
##print(cubed.pow_3(7))  # 343
##print(49*7)
##
##import os
##
##print(os.path.join("Users", "bob", "st.txt"))
##
##with open("st.txt", "w", encoding="utf-8") as f:
##    f.write("Hi from Python ぱ")

##import csv
##with open("st.csv", "r") as f:
##    r = csv.reader(f, delimiter=",")
##    for row in r:
##        print(",".join(row))

##class Shape:
##    def __init__(self,w,l):
##        self.width = w
##        self.len = l
##
##    def print_size(self):
##        print("{} by {}".format(self.width, self.len))
##
##    def what_am_i(self):
##        print("I am a shape")
##
##
##class Square(Shape):  # 継承
##    def area(self):
##        print(self.width + self.len)
##        return self.width * self.len
##
##    def print_size(self):
##        print("I am {} by {}".format(self.width, self.len))
##
##    def culculate_perimeter(self):
##        print("外周: {}".format(self.len * 4))
##
##    def change_size(self,nw):
##        self.width = self.width + nw
##        return self.width
##
##class Rectangle(Shape):
##    def culculate_perimeter(self):
##        print("外周: {}".format(self.len * 4))
##
##
##sq = Square(2,5)
##sq.culculate_perimeter()
##sq.what_am_i()
##sq.area()
##sq.change_size(10)
##sq.area()
##rc = Rectangle(3,7)
##rc.culculate_perimeter()
##rc.what_am_i()

class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")


a_square = Square(29)
print(Square.square_list)
another_square = Square(93)
print(Square.square_list)
