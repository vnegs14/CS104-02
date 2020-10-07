#intialize all variables to 0
temp = 0

while temp < 999:
    temp=int(input("Please enter the current temperature: "))

    if temp >= 90 and temp < 999:
        print("Wear Shorts")
    elif temp >= 70 and temp < 90:
        print("Short sleeves are fine")
    elif temp >= 50 and temp < 70:
        print("Wear a jacket")
    elif temp >= 32 and temp < 50:
        print("Wear a heavy jacket")
    elif temp < 32:
        print("Stay inside, very cold")
temp=999
print("Program has ended")
