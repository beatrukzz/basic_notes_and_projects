# python compound interest calculator

print("option 1 is the simpler program and option 2 is the more complex program")
option = int(input("Enter the option you want to use: "))
if option == 1:
    investment_amount = float(input("Enter the amount you want to invest: "))
    percentage_increase = float(input("Enter the percentage increase: "))
    years = int(input("Enter the number of years you want to invest the money: "))
    print("calculating....")
    final_amount = investment_amount * (1 + percentage_increase / 100) ** years
    print(f"The final amount after {years} years is £{round(final_amount,2)}")  

if option == 2:

  princliple = 0
  rate = 0
  time = 0

while True:                # when using True and  False in a while loop you have to break it at the end to not cause a never ending loop
  princliple = float(input("Enter the amount you want to invest: "))
  if princliple <= 0:                
    print("Please enter a positive number")
  else:
      break

while True:
  rate = float(input("Enter the percentage increase: "))
  if rate <= 0:
    print("Please enter a positive number")
  else:
      break
    
while True:
  time = int(input("Enter the number of years you want to invest the money: "))
  if time <= 0:
    print("Please enter a positive number")
  else:
      break
    
total = princliple * pow((1 + rate / 100), time) 
print(f"The final amount after {time} years is £{round(total,2)}")
