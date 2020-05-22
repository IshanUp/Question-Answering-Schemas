from sympy.solvers import solve
from sympy import Symbol
# using sympy library to solve equations
# pip3 install sympy


class equation:
    def __init__(self):
        self.equation = []

    def append(self, x):
        self.equation.append(x)

    def checkComplete(self):
        variables = 0
        for i in self.equation:
            num = 0
            # checking if it is not a number
            if (i.islower() and i not in ['+', "-", "/", "*"]):
                variables += 1
            else:
                num += 1
        if(variables == 1 and num > 0):
            return 1
        elif (variables > 0 and num > 0):
            return variables
        else:
            return -1

    def allSum(self):
        sum = 0
        for i in self.equation:
            if(i.islower()):
                continue
            else:
                sum += i
        return sum

    def solve(self):
        eq = ""
        variable = ""  # will store the variable symbol
        self.equation = ['-', '70', '0', '+', 'variable', '-', '100']
        for i in self.equation:
            if (i.islower() and i not in ['+', "-", "/", "*"]):
                variable = i
        for i in self.equation:
            eq = eq + " " + i
        eq.lstrip(" ")
        eq.rstrip(" ")
        print(eq)
        x = Symbol(variable)
        ans = solve(eq, x)
        ans = ans[0]
        return ans

    def replace(self, x1, x2):
        for i in range(0, len(self.equation)):
            if (self.equation[i] == x1):
                self.equation[i] = x2

    def show(self):
        print(self.equation)


a = ['+', '70', 'x1', '+', 'variable', '-', '100']
c = equation()
ans = c.solve()
print(ans)
