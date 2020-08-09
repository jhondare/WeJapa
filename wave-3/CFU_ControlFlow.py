#Question: What type of loop should we use?
#You need to write a loop that takes the numbers in a given list named num_list:
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
#Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.
#Would you use a while or a for loop to write this code?
## Please use this space to test and run your code
# i would use the FOR-loop because its flexible and increments automatically 


odd_array = []

for num in num_list: 
    if (num % 2 == 1):
        if (len(odd_array) <=4):
            print('this is an odd number . . . lets add it to an odd array')
            odd_array.append(num)
            print(odd_array)
            print(len(odd_array))
        else: 
            print('. . .  oopsi!, we have exceeded the desired length of the array') 
            break
    else: 
        print('this is an even number ')
print('The sum of the entire odd_array is:: {}'.format(sum(odd_array)))