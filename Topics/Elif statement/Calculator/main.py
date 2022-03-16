a, b, action = float(input()), float(input()), input()
if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "*":
    print(a * b)
elif action == "pow":
    print(a ** b)
elif b == 0.0:
    print("Division by 0!")
elif action == "/":
    print(a / b)
elif action == "mod":
    print(a % b)
elif action == "div":
    print(a // b)
