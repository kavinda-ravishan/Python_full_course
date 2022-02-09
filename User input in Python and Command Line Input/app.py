from sys import argv
print(f"Argument 0 : {argv[0]}")
print(f"Argument 1 : {argv[1]}")

x = int(input("X : "))
y = int(input("Y : "))

op = input("Equation : ")
z = eval(op)

print(f'{op} = {z}')

# python app.py hello
