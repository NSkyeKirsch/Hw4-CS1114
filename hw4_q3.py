"""
Author: Noa Kirschbaum
Assignment / Part: HW4 - Q3
Date due: 2022-03-03
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

row_str = "";
row_number = 2;

num_input = int(input("Please enter a positive integer: "));
num_spaces = num_input;

while(row_number <= (num_input + 1)):
    for i in range(num_spaces):
        row_str += " ";
    for numbers in range(1,(row_number)):
        row_str += str(numbers);
    print(row_str);
    row_number += 1;
    row_str = "";
    num_spaces -= 1;