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
halfway = False;
stars_str = "";
num_rows = 0;
spaces = 0;

while(num_rows < (pos_n - 1)):
    num_rows += 1;
    #print("num_rows:", num_rows);
    if (num_rows == num_half):
        halfway = True;
    for i in range(spaces):
        stars_str += " ";
    for i in range(1,loops_n):
        stars_str += "*";
    print(stars_str);
    if (loops_n > 1 and halfway == False):
        loops_n -= 2;
        spaces += 1;
    else:
        loops_n += 2;
        spaces -= 1;
    stars_str = "";