age = 10
if age > 18:
    print("Hello")
else:
    print("Hie")
    
dictionary = {
    "name":"nashe",
    "email":"chakurungamatapiwanashe@gmail.com"
}
dictionary

class Car:
    def color_of_car(self):
        print("this is the color of this car")
    def can_move(self):
        print("hello l can move upto 180km per hour")

honda = Car()
honda.color_of_car()

import numpy as np

sda = np.array([10,20,30,40])
sda


zeros = np.zeros((5,5))
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])



n1 = np.arange(10,50,5)
n1
array([10, 15, 20, 25, 30, 35, 40, 45])