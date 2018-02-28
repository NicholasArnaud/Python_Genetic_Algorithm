import random

class Parser(object):
    "Collects the string and seperates it into seperate strings to variablize"
    def __init__(self, expression):
        self.expression = expression
        self.variables = []
        self.vals = []
        self.pairs = []
        self.value = 0
        self.grammar = ['*', '(', '+', ')', '!', '|', '^', '~']

    def parse(self):
        "Parses through list"
        self.initvariables()
        for i in self.variables:
            if i not in self.vals:
                self.vals.append(i)
        for r_p in self.vals:
            self.value = random.randint(0, 1)
            self.pairs.append((r_p, str(self.value)))
        print self.variables
        print self.vals
        print self.pairs

    def initvariables(self):
        "creates the variables"
        for index in self.expression:
            if(ord(index) >= 65) and (ord(index) <= 90):
                index = chr(ord(index) + 32)
            if(ord(index) >= 97) and (ord(index) <= 122):
                pass
            else:
                continue
            self.variables.append(index)


if __name__ == '__main__':
    STRING = Parser('(a+B)*(B+A)*(!d+E+F)')
    STRING.parse()

# parse (A+B)*(B+A)*(!D+E+F)
# class Object
# 1 arguement
# -string/ from file
# -specific Format/ Grammer
# //(A+B)*(B+A)*(!D+E+F)
# -ALL Letters/ Variables no duplicates
# -ALL Groups of Parentheses
# -[('A',),('B',),('D',),('E',)('F',)]
# + stands for 'and'
# * stands for 'or'
