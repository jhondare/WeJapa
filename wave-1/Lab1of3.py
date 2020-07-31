
reservoir_volume = 4.445e8
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
print("original rainfall:: {}".format(rainfall))
rain_per_dec = 0.1 * rainfall
print("the percentage decrease is:: {}".format(rain_per_dec))
rainfall -=  rain_per_dec
print("the new value of the rainfall is:: {}".format(rainfall))

# add the rainfall variable to the reservoir_volume variable

reservoir_volume += rainfall
print("addition of the reservoir volume with the new rainfall:: {}".format(reservoir_volume))


# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm
reservoir_per_increase =(0.05 * reservoir_volume)
reservoir_volume += reservoir_per_increase
print('the reservoir voluming after adding 5percent is:: {}'.format(reservoir_volume))



# decrease reservoir_volume by 5% to account for evaporation

reser_per_dec_2 = (0.05 * reservoir_volume)
reservoir_volume -=reser_per_dec_2
print('the new reservoir voluming after decreasing 5percent is:: {}'.format(reservoir_volume))

# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.

reservoir_volume -= 2.5e5

print("the final volume for the reservior is:: {}".format(reservoir_volume))


# print the new value of the reservoir_volume variable