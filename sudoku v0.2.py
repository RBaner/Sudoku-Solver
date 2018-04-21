#import numpy as np

# User input for puzzle line by line
while True:
    amount = int(input("How many columns in the sudoku puzzle: "))
    if (amount**(1/2))%1 == 0:
        break
    else:
        print("That doesn't seem right. Sudoku Puzzles always have side length n^2 with n blocks per side. Try again.")
print("Input each line with periods for blank spots and numbers where they appear with commas in between")
print("For a row of length 9 the input would be: 4,3,.,5,.,.,6,.,.")
sudo = []
for num in range(1,amount+1):
    while True:
        data = input("Line %s here: " % num)
        data = data.split(",")
        if len(data) == amount:
            sudo.append(data)
            break
        else:
            print("That doesn't seem right. Each row should have the same amount of elements as the side length of the sudoku puzzles. Try again.")

# This block was for testing purposes
"""
a = ['4','3','.','5','.','.','6','.','.']
b = ['.','.','2','1','.','3','.','.','.']
c = ['.','.','.','4','.','2','.','7','3']
d = ['6','.','.','.','3','8','.','.','5']
e = ['.','5',7,'.',9,'.',2,4,'.']
f = [8,'.','.',7,4,'.','.','.',6]
g = [1,9,'.',3,'.',7,'.','.','.']
h = ['.','.','.',9,'.',4,5,'.','.']
i = ['.','.',5,'.','.',6,'.',1,9]

sudo = [a,b,c,d,e,f,g,h,i]
"""

def possibles(sudo):
    for row in sudo:
        for i in range(len(row)):
            if row[i] == ".":
                row[i] = []
                for num in range(1,(len(sudo)+1)):
                	row[i].append(num)
            else:
                row[i] = int(row[i])
    return sudo

def solve_one(sudo):
    for num in range(1,(len(sudo)+1)):
        for index in range(len(sudo)):
            for row in sudo:
                for row_2 in sudo:
                    if row[index] == num and type(row_2[index]) == list and num in row_2[index]:
                        row_2[index].remove(num)
        for row in sudo:
            for index in range(len(row)):
                if num in row and type(row[index]) == list and num in row[index]:
                    row[index].remove(num)
    return sudo

def single_option(sudo):
    for row in sudo:
        for index in range(len(row)):
            if type(row[index]) == list and len(row[index]) == 1:
                row[index] = row[index][0]
    return sudo

def within_box(sudo):
    spacing = int(len(sudo)**(1/2))
    for row in range(1,spacing+1):
        row_start = int(((row-1)/spacing)*len(sudo))
        row_finish = int((row/spacing)*len(sudo))
        for column in range(1,spacing+1):
            column_start = int(((column-1)/spacing)*len(sudo))
            column_finish = int((column/spacing)*len(sudo))
            box = []
            for row in sudo[row_start:row_finish]:
                for item in row[column_start:column_finish]:
                    box.append(item)
            for num in range(1,len(sudo)+1):
                if num in box:
                    for thing in box:
                        if type(thing) == list:
                            if num in thing:
                                thing.remove(num)
            for row in sudo[row_start:row_finish]:
                row[column_start:column_finish] = box[:spacing]
                box[:spacing] = []
    return(sudo)        

def unsolved(sudo):
    for row in sudo:
        for index in row:
            if type(index) == list:
                return True
    return False

def main(sudo):
    possibles(sudo)
    within_box(sudo)
    while unsolved(sudo):
        solve_one(sudo)
        single_option(sudo)
        within_box(sudo)
#    print(np.array(sudo))

main(sudo)
