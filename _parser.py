'parser for strings to get variables'
import random


class _parser(object):
    'Collects the string and seperates it into seperate strings to variablize'
    def __init__(self, expression):
        self.expression = expression
        self.variables = []
        self.vals = []
        self.pairs = []
        self.value = 0
        self.grammar = ['*', '(', '+', ')', '!', '|', '^', '~', '=', '&']

    def parse(self):
        'Parses through list'
        print self.expression
        self.initvariables()
        self.setoperations(self.expression)
        print self.expression
        for i in self.variables:
            if i not in self.vals:
                self.vals.append(i)
        for r_p in self.vals:
            self.value = random.randint(0, 1)
            self.pairs.append((r_p, str(self.value)))

        savefile(self.expression)
        print self.variables
        print self.vals
        print self.pairs

    def initvariables(self):
        'creates the variables'
        for index in self.expression:
            if(ord(index) >= 65) and (ord(index) <= 90):
                self.expression = self.expression.replace(index, chr(ord(index) + 32))
                index = chr(ord(index) + 32)
            if(ord(index) >= 97) and (ord(index) <= 122):
                pass
            else:
                continue
            self.variables.append(index)

    def setoperations(self, string):
        'sets operations to fit CNF convention'
        for index in string:
            if index in self.grammar:
                if index == '*':
                    self.expression = self.expression.replace(index, ' or ')
                if index == '+':
                    self.expression = self.expression.replace(index, ' and ')

def readfile(filename):
    'Runs test cases created from a saved file'
    file_info = open(filename, 'r')
    data_list = file_info.readlines()
    for data in data_list:
        if data[0] == "\n":
            continue
        _string = _parser(data)
        _string.parse()
    file_info.close()

def savefile(string):
    'save expression from parser'
    file_info = open('SavedInfo.txt', 'a+')
    file_info.write(string + '\n')
    file_info.close()

if __name__ == '__main__':
    readfile('TestReader.txt')


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
