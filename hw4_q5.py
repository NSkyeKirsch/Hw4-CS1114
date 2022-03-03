"""
Author: Noa Kirschbaum
Assignment / Part: HW4 - Q5
Date due: 2022-03-03
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

import turtle;

polygon_n = int(input("Please enter the shape (as an integer): "));

turtle.speed(0.2);

for loop in range(20):
    for i in range(polygon_n):
        turtle.forward(100);
        turtle.left(360/polygon_n);

    turtle.left(360/20);


