# pyhton weight converter

weight, unit = float(input("enter your weight? ")), input("would you like to convert it to lbs or kg? ")
if unit == "lbs":
    weight = weight * 2.20462
    print(f"your weight is {round(weight,2)} lbs")
elif unit == "kg":
    weight = weight / 2.20462
    print(f"your weight is {round(weight,2)} kg")
else:
    print("invalid unit")
    exit()
