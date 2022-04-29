import sys

#1.read_file:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
with open('LP-1.txt', 'r') as file1:
    LP1 = file1.readlines()
#assign lines from file
list1 = []
lines = []
c = []

list1 = [LP1[i].split() for i in range(0, len(LP1))]
first_line = list1[0]
lines = [list1[i] for i in range(0, len(list1) - 1)]

if lines[1][0] == 's.t':
    lines[1].remove('s.t')
elif lines[1][0] == 'st':
    lines[1].remove('st')
elif lines[1][0] == 'subject' and lines[1][1] == 'to':
    lines[1].remove('subject')
    lines[1].remove('to')
else:
    sys.exit('incorrect format')

#If the last line is only permited to have a (>= or ≥) symbol then this line should be: if not (list1[-1][-2] == '>=' or list1[-1][-2] == '≥'):
if not (list1[-1][-2] == '<=' or list1[-1][-2] == '≤' or list1[-1][-2] == '=' or list1[-1][-2] == '>=' or list1[-1][-2] == '≥'):
    sys.exit('incorrect format2')

#2.process_first_line:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
num = ''
MinMax = []

if first_line[0] == 'min':
    MinMax.append(-1)
elif first_line[0] == 'max':
    MinMax.append(1)
else:
    sys.exit("incorrect format")

counter = 3
col = 0

if first_line[counter] == '-':
    num = '-'
    counter += 1
elif first_line[counter] == '+':
    num = ''
    counter += 1

if first_line[counter][0] == 'x':
    c.append(1)
elif first_line[counter][0] == '-' and first_line[counter][1] == 'x':
    c.append(-1)
else:
    for char in first_line[counter]:
        if char.isdigit():
            num += char
        else:
            break
    c.append(int(num))

counter += 1

while (counter < len(first_line)):
    # check_sign
    if first_line[counter] == '-':
        num = '-'
    elif first_line[counter] == '+':
        num = ''
    else:
        sys.exit('incorrect format')

    counter += 1

    # check_coefficients
    if first_line[counter][0] == 'x':
        num += '1'
    else:
        for char in first_line[counter]:
            if char.isdigit():
                num += char
            else:
                break
    c.append(int(num))

    counter += 1

#3.process_lines:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
A = []
Eqin = []
b = []
row = -1
col = 0

for i in range(1, len(lines)):
    A.append([])
    row += 1
    line = lines[i]
    counter = 0
    num = ''

    #format check
    if not (line[-1].isdigit() or line[-2] == '<=' or line[-2] == '≤' or line[-2] == '=' or line[-2] == '>=' or line[-2] == '≥'):
        sys.exit('incorrect format')

    #first item
    if line[counter] == '-':
        num = '-'
        counter += 1
    elif line[counter] == '+':
        num = ''
        counter += 1

    if line[counter][0] == 'x':
        num += '1'
    elif line[counter][0] == '-' and line[counter][1] == 'x':
        num = '-1'
    else:
        for char in line[counter]:
            if char.isdigit():
                num += char
            else:
                break
    A[row].append(int(num))

    num = ''
    counter += 1

    while (counter < len(line)):
        while not (line[counter] == '<=' or line[counter] == '≤' or line[counter] == '=' or line[counter] == '>=' or line[counter] == '≥'):
            # check_sign
            if line[counter] == '-':
                num = '-'
            elif line[counter] == '+':
                num = ''
            else:
                sys.exit('incorrect format')

            counter += 1

            if line[counter][0] == 'x':
                num += '1'
            else:
                for char in line[counter]:
                    if char.isdigit():
                        num += char
                    else:
                        break
            A[row].append(int(num))

            counter += 1
            num = ''

        if(line[counter] == '<=' or line[counter] == '≤'):
            Eqin.append(-1)
        elif(line[counter] == '='):
            Eqin.append(0)
        elif(line[counter] == '>=' or line[counter] == '≥'):
            Eqin.append(1)
        counter += 1
        if line[counter].isdigit():
            b.append(int(line[counter]))
        else:
            sys.exit('incorrect format')

        counter += 1

#4.export file:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
with open('LP-2.txt', 'w+') as file2:
    for item in MinMax:
        file2.write('[ %d ]  ' % item)
    file2.write('[  ')
    for item in c:
        file2.write('%d  ' % item)
    file2.write(']  x \ns.t        ')
    for row, item, item2 in zip(range(len(A)), Eqin, b):
       for item in A[row]:
            file2.write('%d  ' % item)
       file2.write('[ %d ]  ' % item)
       file2.write(' %d' % item2)
       file2.write('\n           ')
    file2.write(' x  >=  0')