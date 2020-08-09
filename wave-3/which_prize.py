#Practice: Which Prize
#Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, 
# which is stored in the integer variable points.

#Points	Prize
#1 - 50	wooden rabbit
#51 - 150	no prize
#151 - 180	wafer-thin mint
#181 - 200	penguin
#All of the lower and upper bounds here are inclusive, and points can only take on positive integer values up to 200.

#In your if statement, assign the result variable to a string holding the appropriate message based on the value of points. 
# If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. 
# If there's no prize, the message should state "Oh dear, no prize this time."

#Note: Feel free to test run your code with other inputs, but when you submit your answer, only use the original input of points = 174. 
# You can hide your other inputs by commenting them out.


points = 174  # use this input to make your submission
result = ['Wooden Rabbit', 'No Prize', 'Wafer-Thin mint', 'Penguin']

#points = int(input('Please enter a score::'))

if (points>=1 and points<=50):
    print('Congratulations! You won a {}'.format(result[0]))
elif(points>=51 and points<=150):
    print('Oh dear, {} at this time'.format(result[1]))
elif(points>=151 and points<=180):
    print('Congratulations! You won a {}'.format(result[2]))
elif(points>=181 and points<=200):
    print('Congratulations! You won a {}'.format(result[3]))
else: 
    print('ooopsi!!! that point is outta range')
    