class Point3D:
    coords = []

    def __init__(self, args):
        self.coords = args

    def get_coords(self):
        return tuple(self.coords)

    def set_coords(self, pos, val):
        self.coords[pos] = val


pt = Point3D([1, 2, 3, 4])
pt.set_coords(2, 5)
print(pt.get_coords())
