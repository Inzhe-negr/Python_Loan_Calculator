
dim = [int(input()) for _ in range(3)]
x, y = int(input()), int(input())
dim.sort()

if dim[0] <= min(x, y) and dim[1] <= max(x, y):
    print("The box can be carried")
else:
    print("The box cannot be carried")
