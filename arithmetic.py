def arithmetic_arranger(problems, show_results = False):

#Code for Too Many Problems Error
    if len(problems) > 5:
        print ('Error: Too many problems.')
        exit()

    firstnumbers = []
    operator = []
    secondnumbers = []
    result = []
    num = 0
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    space = ' '*3
    fspace = []
    sspace = []
    fourthspace = []

#Creating List for First Number, Operator, Second Number and Result
    for fnumber in problems:
        z = str(problems[num]).split()
        if z[0].isdigit() == False:
#Code for Numbers must be digits error.
            print ('Error: Numbers must only contain digits.')
            exit()
        num = num + 1
        firstnumbers.append(z[0])
    num = 0

    for op in problems:
        z = str(problems[num]).split()
        num = num + 1
        operator.append(z[1])

    num = 0
    for snumber in problems:
        z = str(problems[num]).split()
        if z[2].isdigit() == False:
#Code for Numbers must be digits error.
            print ('Error: Numbers must only contain digits.')
            exit()
        num = num + 1
        secondnumbers.append(z[2])

    num = 0
    for number in range(len(problems)):
        if operator[num] == '+':
            result.append(int(firstnumbers[number]) + int(secondnumbers[number]))
        elif operator[num] == '-':
            result.append(int(firstnumbers[number]) - int(secondnumbers[number])) 

#Code for Proper Operator Error
        else:
            print ("Error: Operator must be '+' or '-'.")
            exit()
        num = num + 1 

#Code for Error  Max of Four Digits Only
    num = 0
    for char in range(len(firstnumbers)):
        if len(firstnumbers[num]) > 4:
            print ('Error: Numbers cannot be more than four digits.')
            exit()
        if len (secondnumbers[num]) > 4:
            print ('Error: Numbers cannot be more than four digits.')
            exit()
        num = num + 1
# Creating The Lines That Will Appear Vertically
    num = 0
    for value in range(len(firstnumbers)):
        higher = max(len(firstnumbers[num]), len(secondnumbers[num]))
        fspace.append((higher - len(firstnumbers[num]) + 2))
        sspace.append((higher - len(secondnumbers[num]) + 2))
        fourthspace.append((higher - len(str(result[num])) + 2))
        num = num + 1

    num = 0
    for digit in firstnumbers:
        line1 = line1 + " " * fspace[num] + digit.rjust(1) + space
        num = num + 1

    num = 0
    for op in operator:
        if operator[num] == "+" or operator[num] == "-":
            line2 = line2 + op + (" " * (sspace[num] - 1)) + secondnumbers[num].rjust(1) + space
            num = num + 1
        else:
            print ("Error: Operator must be '+' or '-' .")
            break

    num = 0
    for num in range(len(firstnumbers)):
        if len(firstnumbers[num]) > len(secondnumbers[num]):
            line3 = line3 + '-' * len('  ' + firstnumbers[num]) + space
        else:
            line3 = line3 + '-' * len('  ' + secondnumbers[num]) + space
    num = 0
    for answer in result:
        line4 = line4 + " " * int(fourthspace[num])  + str(answer).rjust(1) + space
        num = num + 1
#Displaying Lines with Results
    arranged_problems = (line1 + '\n' + line2 + '\n' + line3)
#Displaying Lines without Results
    if show_results == True:
        arranged_problems= (line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 )
    print (arranged_problems)
