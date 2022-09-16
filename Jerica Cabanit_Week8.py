#1st Activity
marks = [56,77,90,45,80]
total = sum(marks, 0)
print (total)

#2nd Activity
num = list(input('Enter 10 numbers: '))
numlist = num
low = min(numlist)
high = max(numlist)
average = numlist / 10
total = sum(numlist, 1)
print(low, high, average, total)

#3rd Activity
rainfall = list(input('Enter the total rainfall for 12 months: '))
low = min(rainfall)
high = max(rainfall)
average = rainfall / 12
total = sum(rainfall)
print(low, high, average, total)

#4th Activity
    #1st Question
number=10.0
total=0.0
while number > 0:
    number=float(input('Enter a positive number (negative to quit):' ))
if number < 0:
    total=total
    print('Total =', format(total, '.2f'))

    #2nd Question
radius=0.0
area=0.0
circumference=0.0
user_preference=int(input('What is your preference? Enter 1 for area, enter 2 for circumference: '))
radius=float(input('Enter the radius: '))
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
if user_preference == 1:
    print(area)
elif user_preference == 2:
    print(circumference)

    #3rd Question
character='#'
numrows=7
space=' '
counter1=0
counter2=0
while counter1<=numrows:
    counter2=counter1+2
    while counter2<=numrows+2:
        if counter2==0 or counter2==counter1+1:
            print(character, end=' ')
        else:
            print(character, end=' ')
        counter2=counter2+1
    counter1=counter1+1
    print()