class EquationSystem:
    funcs = []

    def __init__(self, *args):
        self.funcs = args

    def to_string(self):
        return " ⌈" + str(self.funcs[0]) + ", \n<\n ⌊" + str(self.funcs[1])