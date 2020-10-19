class Point:

    def __init__(self, arg1=0, arg2=1):
        self.x = arg1
        self.y = arg2


list = []
for _ in range(5):
    print("Enter")
    x = int(input("X: "))
    y = int(input("Y: "))
    pt = Point(x, y)
    list.append(pt.__dict__)
print(list)
