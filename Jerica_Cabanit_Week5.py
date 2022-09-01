#1st Activity
length=int(input('Enter the length of the backyard'))
area=length*length
print(area)

#2nd Activity
length=int(input('Enter the length of the backyard'))
perimeter=4*length
print(area)

#3rd Activity
if area > perimeter :
    print('The area is bigger than the perimeter')
elif perimeter > area :
    print('The perimeter is bigger than the area')
elif perimeter == area :
    print('The area is the same amount as the perimeter')

#5th Activity
counter=0
while(counter < 3):
    ctemp=int(input('enter temp'))
    f=(9/5) *ctemp+32
    print('farenheit temp is', f)
    counter=counter+1
if counter == 2 :
    break

#6th Activity
#This program will calculate the grade
#input: marks
marks=int(input('type your marks'))
#process: comparison: A is >=90, B is >=80, C is >=70, D is >=60
# otherwise grade will be F
if marks >= 90:
   grade='A'
elif marks >=80:
   grade='B'  
elif marks >=70:
   grade='C'  
elif marks >=60:
   grade='D'  
else :
	grade='F'
#output: grade
print('grade is', grade)

#7th Activity
#input : licence, demerit points and insurance
lic=int(input('do you have a licence, yes or no' ))
demerit_points=int(input('type the demerit points'))
ins=int(input('is your insurance current, yes or no'))
#check if the driver has a licence, the number of demerit points should be more than 3 and has current insurance.
if lic=='yes' and demerit_points > 3 and ins=='yes':
    print('you are eligible to drive')
else :
    print('you are not eligible to drive')
