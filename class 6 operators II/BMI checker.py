# bmi checker

w = float(input("enter the weight in kilograms"))
h = float(input("enter the height in metre"))

bmi = w/(h * h)

if bmi <18.5:
    print("you are underweight")
elif bmi < 25:
    print("you are healthy")
elif bmi < 30:
     print("you are overweight")
else:
    print("you are obessed")