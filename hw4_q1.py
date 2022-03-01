"""
Author: Noa Kirschbaum
Assignment / Part: HW4 - Q1
Date due: 2022-03-03
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

#inputs: pos int (n)
#counts even numbers n times

num_numbers = int(input("Please enter a positive integer: "));

#while loop
print("Executing while-loop...");
x = 1;
while(x < ((num_numbers + 1) * 2)):
    if(x % 2 == 0):
        print(x);
    x += 1;



#for loop
print("Executing for-loop...");
for x in range(1,((num_numbers+1)*2)):
    if(x % 2 == 0):
        print(x);

#I like for-loops!