"""
Author: Noa Kirschbaum
Assignment / Part: HW4 - Q2
Date due: 2022-03-03
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

pos_n = 2*(int(input("Please enter a positive number: ")));
loops_n = pos_n;
num_half = round(pos_n/2);
halfway_point = False;
stars_str = "";
num_rows = 0;
num_spaces = 0;

while(num_rows < (pos_n - 1)):
    num_rows += 1;
    #print("num_rows:", num_rows);
    if (num_rows == num_half):
        halfway_point = True;
    for i in range(num_spaces):
        stars_str += " ";
    for i in range(1,loops_n):
        stars_str += "*";
    print(stars_str);
    if (loops_n > 1 and halfway_point == False):
        loops_n -= 2;
        num_spaces += 1;
    else:
        loops_n += 2;
        num_spaces -= 1;
    stars_str = "";