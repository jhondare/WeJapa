#Factorials with For Loops
#Now use a for loop to find the factorial!

#It will now be great practice for you to try to revise the code you wrote above to find the factorial of a number, 
# but this time, using a for loop. Try it in the code editor below!

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
if number < 0:
     print('Ooopsi! you cant find the factorial of a negative number')
elif number == 0:
    print('shebi you know this would give you one ba?')
else:
    for fact in range(product, number + 1):
        product=product * fact
# print the factorial of number
print(product)