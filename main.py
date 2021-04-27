
num1 = int(input("Enter the first fraction's numerator:"))

den1 = int(input("Enter the first fraction's denominator:"))

num2 = int(input("now, enter the second fractions numerator:"))

den2 = int(input("and finally, enter the second fraction's denominator:"))
print("Thank you!")

print('THANK YOU FOR USING THIS CALCULATOR =)\n\n\n\n\n\n\n\n\n\n')

if num1:
    print('calculating den1')




if den1:
    print('calculating num2')

#SEC == 2

if num2:
    print('calculating den2')



if den2:
    print('COMPARING...')

#CALCULATING CODE

secondFracNumber = den1*num2

firstFracNumber = den2*num1

#FORMATING BREAKS:

print('\n\n\n\n\n\n\n\n\n\n\n\n')

#validating _code_

if num1 < den1:
    if firstFracNumber > secondFracNumber:
        print(f'The first fraction is greater then the second fraction! {num1}/{den1} > {num2}/{den2}\n')


    
    if firstFracNumber < secondFracNumber:
        print(f'The second fraction is greater then the first fraction! {num1}/{den1} < {num2}/{den2}\n')
        
    if secondFracNumber == firstFracNumber:
	    print(f'The fractions are equivalent! {num1}/{den1} = {num2}/{den2}\n\n\t\t\t')
    
    if num2 < den2:
        if firstFracNumber > secondFracNumber:
            print(f'The first fraction is greater then the second fraction! {num1}/{den1} > {num2}/{den2}\n')
        
        
        
    if firstFracNumber < secondFracNumber:
        print(f'The second fraction is greater then the first fraction! {num1}/{den1} < {num2}/{den2}\n')
        
    if secondFracNumber == firstFracNumber:
	    print(f'The fractions are equivalent! {num1}/{den1} = {num2}/{den2}\n\n\t\t\t')
