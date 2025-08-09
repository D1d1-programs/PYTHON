# power calculator
b = int(input("Enter the Base :"))
p = int(input("Enter the power :"))

res = 1

for d in range(p):
    res = res* b

print(f'the answer to {b} power {p} is {res}')