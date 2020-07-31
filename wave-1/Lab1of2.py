#Quiz: Calculate
#In this quiz you're going to do some calculations for a tiler. 
# Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. 
# Tiles come in packages of 6.

#1. How many tiles are needed?
#2. You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?




# Fill this in with an expression that calculates how many tiles are needed.
w1, l1, w2, l2  = 9, 7, 5, 7
total_area = (w1 * l1) + (w2 * l2)
tiles_needed = int(total_area / 6)   
print(tiles_needed)

# Fill this in with an expression that calculates how many tiles will be left over.
tiles_left = (17 * 6) - (tiles_needed * 6)  
print('the amount of tiles left is {}, invarabily could mean {} packs'. format(tiles_left, 6))


# things which are wordy of note are as follows:
# first of all the tiler is going to tile 2 basic places, one palce would contain -- 9w x 7h, whilst the other would be 5w x 7h
# secondly in a pack of tiles, it contains 6 tiles each 
# now, we need to find tha area of the whole section which he or she is going to tile, remember, we were given W and H so
# what we have here is going to be A = l x b -- this determins the total area we are going to cover 
# now, we move a step further and take  

# a1 -- 63, a2-- 35, total area --98

