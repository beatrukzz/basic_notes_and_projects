
# BMI Calculator

def weight_converter():
    weight = float(input("enter your weight in pounds: "))
    weight_in_kg = weight * 0.453592
    print(f"your weight in kg is {round(weight_in_kg,2)}kg")
    return weight_in_kg

def height_converter():
    height = float(input("enter your height in inches: "))
    height_in_meters = height * 0.0254
    print(f"your height in meters is {round(height_in_meters,2)}meters")
    return height_in_meters

def BMI_calculator(weight=None, height=None):
    if weight is None:
        weight = float(input("enter your weight in kg: "))
    if height is None:
        height = float(input("enter your height in meters: "))
    
    height_squared = pow(height, 2)
    BMI = weight / height_squared
    print(f"your BMI is {BMI:.2f}")           # .2f is used to round the number to 2 decimal places
    print("now lets see what that means")
    
    if BMI < 18.5:
        print("you are underweight")
    elif BMI >= 18.5 and BMI <= 24.9:
        print("you are normal weight")
    elif BMI >= 25 and BMI <= 29.9:
        print("you are overweight")
    elif BMI >= 30:
        print("you are obese")
    else:
        print("error")

# Main program logic
choice = input("do you want to calculate your BMI? ")
if choice == "yes":
    option = input("do you know your weight and height in kg and meters? ")
    if option == "yes":
        print("perfect lets calculate your BMI")
        BMI_calculator()
    elif option == "no":
        print("okay lets convert your weight and height")
        weight_kg = weight_converter()
        height_m = height_converter()
        BMI_calculator(weight_kg, height_m)
    else:
        print("please answer yes or no")
else:
    print("goodbye!")
