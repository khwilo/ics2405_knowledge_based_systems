import sys

print(' Welcome---')
soilCond = raw_input("Enter the soil conditions:moist/dry ")

print('TYPE:loam, clay')
soilType = raw_input("Enter the soil Type: ")
if soilType=='loam':
    print('check for adequate organic matter and nutrients')
if soilType=='clay':
    print('apply good amounts of fertiser and deep cultivate')
seeds=raw_input('no. of seeds per hole?')
PH = input("Enter the soil PH(0-14): ")

if soilType == 'moist':
    print('planting depth is 2-3 cm')
    if seeds == 2:
        print('spacing is: (2ft x 2 ft')
    if seeds == 1:
        print('spacing is: (2ft x 1 ft')
 
if soilType == 'dry':
    print('planting depth is 2-3 cm')
    if seeds== 2:
        print('spacing is: (3ft x 2 ft')
    if seeds== 1:
        print('spacing is: (2ft x 1 ft')
    
if (PH >= 1) and (PH < 5):
    print('check for nutrient deficiency.consider liming')
elif (PH >= 5) and (PH < 8):
    print('okay')
elif (PH <= 14):
    print('check for nutrient deficiency.check for toicity') 
else:
    print('wrong value for PH.')
