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

def possibles(sudo):
    for row in sudo:
        for i in range(len(row)):
            if row[i] != ".":
                row[i] = int(row[i])
            if type(row[i]) != int:
                row[i] = [1,2,3,4,5,6,7,8,9]
    return sudo

def solve_one(sudo):
    for num in range(1,10):
        for index in range(len(row)):
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

def naked_pair(sudo):
    print("what")

def inside(data,number):
	for index in range(len(data)):
		if type(data[index]) == list:
			return inside(data[index],number)
		elif number in data:
			return True

def main(sudo):
    possibles(sudo)
    solve_one(sudo)
    single_option(sudo)

print(main(sudo))
