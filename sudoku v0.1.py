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
		for num in range(1,(len(sudo)+1)):
                	row[i].append(i)
    return sudo

def solve_one(sudo):
    for num in range(1,(len(sudo)+1)):
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

def within_box(sudo):
	spacing = int(len(sudo)**(1/2))
	for row in range(1,spacing+1):
		row_start = int(((i-1)/spacing)*len(sudo))
		row_finish = int((i/spacing)*len(sudo))
		row_temp = sudo[start:finish]
			for column in range(1,spacing+1):
				column_start = int(((i-1)/spacing)*len(sudo))
				column_finish = int((i/spacing)*len(sudo))
				
					

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


#No need to define within(data,dataset) simply create one list for box and if (num not in box) then if type(box[index])) == list and (num in box[index]) then box[index].remove(num)
