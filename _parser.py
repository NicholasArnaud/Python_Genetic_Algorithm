'parser for strings to get variables'
import random


class _parser(object):
    'Collects the string and seperates it into seperate strings to variablize'
    def __init__(self, expression):
        self.expression = expression
        self.exprwithvalues = ''
        self.variables = []
        self.vals = []
        self.pairs = []
        self.value = 0
        self.grammar = ['*', '(', '+', ')', '!', '|', '^', '~', '=', '&']
        self.correctstatement = False

    def parse(self):
        'Parses through list'
        print self.expression
        self.initvariables()

        print self.expression
        for i in self.variables:
            if i not in self.vals:
                self.vals.append(i)
        for r_p in self.vals:
            self.pairs.append((r_p, ''))

        self.setvariables('100110')
        self.setoperations(self.exprwithvalues)
        savefile(self.exprwithvalues)
        trueexpression = bool(eval(self.exprwithvalues))
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

    def setvariables(self, variable_string):
        'Updates list of tuples that represent each variables value'
        for i in range(0, len(self.pairs), 1):
            new_pair = self.pairs[i]
            new_pair = (new_pair[0], variable_string[i])
            self.pairs[i] = new_pair
        print self.pairs
        for char in self.expression:
            if (ord(char) >= 97) and (ord(char) <= 122):
                for var in self.pairs:
                    if char is var[0]:
                        self.exprwithvalues += var[1]
            else:
                self.exprwithvalues += char
        print self.exprwithvalues

    def setoperations(self, string):
        'sets operations to fit CNF convention'
        for index in string:
            if index in self.grammar:
                if index == '*':
                    self.exprwithvalues = self.exprwithvalues.replace(index, ' or ')
                if index == '+':
                    self.exprwithvalues = self.exprwithvalues.replace(index, ' and ')
                if index == '!':
                    self.exprwithvalues = self.exprwithvalues.replace(index, ' not ')

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

def savefile(_string):
    'save expression from parser'
    file_info = open('SavedInfo.txt', 'a+')
    file_info.write(_string + '\n')
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
