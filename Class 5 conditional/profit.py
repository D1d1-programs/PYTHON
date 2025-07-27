# profit or loss

cp = float(input("Enter the cost price"))
sp = float(input("Enter the selling price"))

if sp > cp:
    print(f" The profit we got is ${sp-cp}")
else:
        print(f" The loss we got is ${cp-sp}")