import os
class Parser(object):
    def __init__(self, expression):
        self.expression = expression
        self.variables = []
        self.grammar = ['*', '(', '+', ')', '!', '|', '^', '~']

    def parse(self):
        for index in self.expression:
            if(ord(index) >= 65) and (ord(index) <= 90):
                index = chr(ord(index) -32)
            if(ord(index) >= 97) and (ord(index) <= 122):
                continue

            self.variables.append(index)
        #reformatting in progress
        print (self.variables)


if __name__ == '__main__':
    string = Parser('(a+B)*(B+A)*(!d+E+F)')
    string.parse()

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
