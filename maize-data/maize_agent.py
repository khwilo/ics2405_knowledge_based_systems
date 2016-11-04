print("HELLO HUMAN!")

print("--Enter the altitude and rainfall of the region to find the maize variety.--")
altitude = input("Altitude: ")
rainfall = input("Rainfall: ")

if ((altitude > 100 and altitude < 500) and (rainfall < 350)):
    print("Dryland and agro-ecozone.")
elif ((altitude > 0 and altitude < 1250) and (rainfall > 350)):
    print("Lowland and agro-ecozone.")
elif ((altitude > 1000 and altitude < 1700) and (rainfall < 750 and rainfall > 1000)):
    print("Medium altitude agro-ecozone.")
elif ((altitude > 1000 and altitude < 1700) and (rainfall < 800 and rainfall > 1500)):
    print("Transitional zone.")
elif ((altitude > 1500 and altitude < 2100) and (rainfall < 800 and rainfall > 1500)):
    print("Highland maize.")
else:
    print("NO VARIETY FOUND!")

print("Enter the soil type. LOAM OR CLAY.")
soilType = raw_input("Type: ")
if soilType=="loam":
    print("Check for adequate organic matter and nutrients.")
elif soilType=='clay':
    print("Apply good amounts of fertiser and deep cultivate.")
else:
    print("WRONG SOIL TYPE!")

print("--Enter the soil condition and the no. of seeds per hole.--")
print("The number of seeds per hole is either 1 or 2.")
soilCondition = raw_input("Condition is either moist or dry: ")
seeds = input("No. of seeds per hole?: ")

if (soilCondition == "moist") and (seeds == 2):
    print("Planting depth is 2-3 cm and the spacing will be (2ft x 2 ft)")
elif (soilCondition == "moist") and (seeds == 1):

    print("Planting depth is 2-3 cm the spacing will be (2ft x 1 ft)")
elif (soilCondition == "dry") and (seeds == 2):
    print("planting depth is 2-3 cm and the spacing will be (3ft x 2 ft)")
elif (soilCondition == "dry") and (seeds== 1):
    print("planting depth is 2-3cm and the spacing will be (2ft x 1 ft)")
else:
    print("WRONG TYPE OF INPUTS!")

PH = input("Enter the soil PH(0-14): ")  
if (PH >= 1) and (PH < 5):
    print("check for nutrient deficiency.consider liming")
elif (PH >= 5) and (PH < 8):
    print("okay")
elif (PH <= 14):
    print("check for nutrient deficiency.check for toicity") 
else:
    print("WRONG VALUE FOR PH!")

print("--Select the deficiency of crop in order from the following choices--")
print("1 - Leaves are dark green with reddish-purple tips and margins.")
print("2 - Yellow leaf margins.")
print("3 - Pale, light green or yellow plants.")
print("4 - Light streaks or bands between the veins from the leaf base to the tip.")
deficiency = input("Choose 1, 2, 3, or 4: ")

if deficiency == 1:
    print("Plant is deficient in phosphorous.")
elif deficiency == 2:
    print("Plant is deficient in potassium.")
elif deficiency == 3:
    print("Plant is deficient in nitrogen.")
elif deficiency == 4:
    print("Plant is deficienct in zinc.")
else:
    print("DEFICIENCY NOT FOUND!")
