class Parser(object):
    def __init__(self, expression):
        self.expression = expression


if __name__ == '__main__':
    parse = Parser('(a+B)*(B+A)*(!d+E+F)')
    pairs = []
    vals = []
    variables = []
    for index in parse.expression:
      #  if(index == '(') or (index == ')') or (index == '*') or (index == '+') or (index == "!"):
      #      continue
        if(ord(index) >= 97) or (ord(index) <= 122):
            index = chr(ord(index) -32)
        if(ord(index) <= 65) or (ord(index) >= 90):
            continue
        variables.append(index)
    for i in variables:
        if i not in vals:
            vals.append(i)
    for rv in vals:
        pairs.append((rv, ''))
    print variables
    print vals
    print pairs
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
