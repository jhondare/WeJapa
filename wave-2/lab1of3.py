# Use this playground to experiment with list methods, using Test Run

days_of_the_week = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
months_of_the_year = ['Jan', 'Feb', 'March', 'April', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

print(len(days_in_month)) 

print("---".join(months_of_the_year)) 

months_of_the_year.append('Grunday') #adds a new day to the list
print(months_of_the_year)

print('Wed' in days_in_month)   #checks if the weekday is present and returns either true or false
print('Wed' in days_of_the_week)

print(max(days_in_month))
print(min(days_in_month))