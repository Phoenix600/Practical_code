# Taking temperature as input from the user
# According to the value of temp print specific message

# float type var to store temp

float_temp = float(input("[+]Enter the temperature : "))

# conditions 

if float_temp < -273 :
    print("Invalid temperature")
elif float_temp == -273 :
    print("Absolute zero temperature")
elif (float_temp > -273 and float_temp < 0 ):
    print("Temperature below freezing point")
elif float_temp == 0 :
    print("Temperature is at freezing point")
elif (float_temp >0 and float_temp < 100) :
    print("Temperature range is normal")
elif float_temp == 100 :
    print("Temperature is at boiling point")
else :
    print("Temperature is above boiling point")
