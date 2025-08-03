# customize your ride

print("\n1. Bike\n2.Car\nEnter your ride ")
ch = input()
if ch == "1":
    ch1 = input("\n1. Scooty\n2.Yamaha\nEnter yur choie ")
    if ch1 == "1":
        print("You have selected scooty")
    elif ch1 == "2":
        print("You have selected Yahama")
    else:
        print("wrong input")
elif ch == "2":
    ch1 = input("\n1. Tesla\n2.Lamborghini\nEnter your choice ")
    if ch1 == "1":
        print("you have selected Tesla")
    elif ch1 == "2":
        print("You have selected Lamborghini")
    else:
        print("wrong input")
else:
    print("invalid input2")