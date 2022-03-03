"""
Author: Noa Kirschbaum
Assignment / Part: HW4 - Q4
Date due: 2022-03-03
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
num_even = 0;
num_odd = 0;
final_str = "";

num_input = input("Please enter a positive integer: ");

for number in range(int(num_input)):
    for digit in str(number):
        if(int(digit) % 2 == 0):
            num_even += 1;
        else:
            num_odd += 1;
    if(num_even > num_odd):
        final_str += str(number) + " ";
    num_even = 0;
    num_odd = 0;

print(final_str);