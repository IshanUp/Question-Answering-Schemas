from sympy.solvers import solve
from sympy import Symbol
# using sympy library to solve equations
# pip3 install sympy


class equation:
    def __init__(self):
        self.equation = []

    def append(self, x):
        self.equation.append(str(x))

    def checkComplete(self):
        variables = 0
        num = 0
        for i in self.equation:

            # checking if it is not a number
            if (str(i).islower() and i not in ['+', "-", "/", "*"]):
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
            if(str(i).islower() or str(i) in ['+', "-", "/", "*"]):
                continue
            else:
                sum += int(i)
        return sum

    def solve(self):
        eq = ""
        variable = ""  # will store the variable symbol
        for i in self.equation:
            if (str(i).islower() and i not in ['+', "-", "/", "*"]):
                variable = i
        for i in self.equation:
            eq = eq + " " + str(i)
        eq.lstrip(" ")
        eq.rstrip(" ")
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


def resolve(sentInfo, question):
    # expected input array of dictionary of the form {owner1:'',verb:'',entityValue:0,entityName;'',owner2:''}

    changeOut = ["put", "place", "plant", "add", "sell",
                 "distribute", "load", "give", "takes away", "gave", "planted"]
    changeIn = ["take from", "get", "pick", "buy", "borrow", "steal", "took"]
    increase = ["more", "carry", "find", "found"]
    reduction = ["eat", "destroy", "remove", "decrease", "removed"]
    comparePlus = ["more than", "taller than", "longer than"]
    compareMinus = ["less than", "fewer than", "shorter than"]
    combine = ["together", "in all", "combined",
               "in all", "in total", "total", "altogether"]
    equator = ["has", "had", "played", "wants", "were", "are"]
    for i in range(0, len(sentInfo)):
        sent = sentInfo[i]
        print(sent)
        if(i == 0):
            owner1eq = 0
            owner2eq = 0
            owner1Name = sent['owner1']
            owner2Name = sent['owner2']
            owner1eq = equation()
            owner1eq.append('x1')
            owner2eq = equation()

        if (owner1Name != ""):
            print("here in else")
            if sent['verb'] in increase:
                owner1eq.append('+')
                if (str(sent['entityValue']).islower()):
                    owner1eq.append('x3')
                else:
                    owner1eq.append(sent['entityValue'])
                # owner1eq.append('x1')
            if sent['verb'] in reduction:
                if(sent['owner1'] == owner1Name or owner1Name == ""):
                    if (owner1Name == ""):
                        owner1Name = sent["owner1"]
                    owner1eq.append('-')
                    if (str(sent['entityValue']).islower()):
                        owner1eq.append('x4')
                    else:
                        owner1eq.append(sent['entityValue'])

            if sent['verb'] in changeIn:
                if sent['owner1'] == owner1Name:
                    if(str(sent['entityValue']).islower()):
                        owner1eq.append('+')
                        owner1eq.append('y1')
                        # we now know that a owner 2 exists
                        owner2eq.append('x2')
                        owner2eq.append('-')
                        owner2eq.append("y1")
                    else:
                        owner1eq.append('+')
                        owner1eq.append(sent['entityValue'])
                        owner2eq.append('x2')
                        owner2eq.append("-")
                        owner2eq.append(sent['entityValue'])

            if sent['verb'] in changeOut:
                print("here in changeOut")
                # if this does not happend that means owner1 and owner2 positions have been flipped this means owner2Name is Owner 1
                if sent['owner1'] == owner1Name:
                    if (str(sent['entityValue']).islower()):
                        owner1eq.append('-')
                        owner1eq.append('y1')
                        owner1eq.replace('x1', '0')
                        owner2eq.append('x2')
                        owner2eq.append('+')
                        owner2eq.append('y1')
                        # perhaps make a if statement here to check if owner 2 already has a name
                        owner2Name = sent['owner2']
                    else:
                        owner1eq.append('-')
                        owner1eq.append(sent['entityValue'])
                      #  owner1eq.replace('x1', '0')
                        owner2eq.append('x2')
                        owner2eq.append('+')
                        owner2eq.append(sent['entityValue'])
                        owner2Name = sent['owner2']
            if sent['verb'] in equator:
                if(sent['owner1'] == owner1Name):
                    if (i == 0):
                        owner1eq.append("+")
                        owner1eq.append(sent["entityValue"])
                    else:
                        owner1eq.append("-")
                        owner1eq.append(sent["entityValue"])
        else:
            entity1eq = equation()
            if sent['verb'] in increase:
                owner1eq.append('+')
                if (str(sent['entityValue']).islower()):
                    owner1eq.append('x3')
                else:
                    owner1eq.append(sent['entityValue'])
                # owner1eq.append('x1')
            if sent['verb'] in reduction:
                if(sent['owner1'] == owner1Name or owner1Name == ""):
                    if(owner1Name == "" and sent['owner1'] == ""):
                        owner1Name = sent['owner1']
                    owner1eq.append('-')
                    if (str(sent['entityValue']).islower()):
                        owner1eq.append('x4')
                    else:
                        owner1eq.append(sent['entityValue'])

            if sent['verb'] in changeIn:
                if sent['owner1'] == owner1Name:
                    if(str(sent['entityValue']).islower()):
                        owner1eq.append('+')
                        owner1eq.append('y1')
                        # we now know that a owner 2 exists
                        owner2eq.append('x2')
                        owner2eq.append('-')
                        owner2eq.append("y1")
                    else:
                        owner1eq.append('+')
                        owner1eq.append(sent['entityValue'])
                        owner2eq.append('x2')
                        owner2eq.append("-")
                        owner2eq.append(sent['entityValue'])

            if sent['verb'] in changeOut:
                print("here in changeOut")
                # if this does not happend that means owner1 and owner2 positions have been flipped this means owner2Name is Owner 1
                if sent['owner1'] == owner1Name:
                    if (str(sent['entityValue']).islower()):
                        owner1eq.append('-')
                        owner1eq.append('y1')
                        owner1eq.replace('x1', '0')
                        owner2eq.append('x2')
                        owner2eq.append('+')
                        owner2eq.append('y1')
                        # perhaps make a if statement here to check if owner 2 already has a name
                        owner2Name = sent['owner2']
                    else:
                        owner1eq.append('-')
                        owner1eq.append(sent['entityValue'])
                      #  owner1eq.replace('x1', '0')
                        owner2eq.append('x2')
                        owner2eq.append('+')
                        owner2eq.append(sent['entityValue'])
                        owner2Name = sent['owner2']
            if sent['verb'] in equator:
                print(owner1Name)
                print(sent["owner1"])
                if(sent['owner1'] == owner1Name or owner1Name == ""):
                    if (i == 0):
                        owner1eq.append("+")
                        owner1eq.append(sent["entityValue"])
                    else:
                        print("here")
                        owner1eq.append("-")
                        owner1eq.append(sent["entityValue"])

    a = owner1eq.checkComplete()

    question = question.rstrip('?')
    question = question.split(' ')
    for i in question:
        if i in combine:
            print("combine")
            print(owner1eq.allSum())
            return owner1eq.allSum()
    owner1eq.show()
    if(a == 2):
        owner1eq.replace('x1', '0')
    a = owner1eq.checkComplete()
    print(a)
    print("is the ans")

    if (a == 1):
        if (owner1eq.solve() < 0):
            print(-1*owner1eq.solve())
            return owner1eq.solve
        print(owner1eq.solve())
        return owner1eq.solve

    b = owner2eq.checkComplete()
    if (b == 2):
        owner2eq.replace('x1', "0")
    b = owner2eq.checkComplete()
    if(b == 1):
        print(owner2eq.solve())
        return owner2eq.solve()


sentinfo = [{'owner1': 'Joan', 'verb': 'has', 'entityValue': 70, 'entityName': 'seashells', 'owner2': 'none'}, {'owner1': 'Joan', 'verb': 'removed',
                                                                                                                'entityValue': 10, 'entityName': 'seashells', 'owner2': 'none'}]

question = "How much does he have ?"

resolve(sentinfo, question)
