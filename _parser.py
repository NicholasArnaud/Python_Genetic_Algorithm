'parser for getting strings from file to get CNF Expressions'

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
        self.expressioncheck = False

    def testparse(self):
        'test parser through list'
        print 'Init expression: '+ self.expression
        self.initvariables()
        self.initlists()
        self.setvariables('100110100')
        self.setoperations(self.exprwithvalues)
        self.expressioncheck = bool(eval(self.exprwithvalues))
        savefile(self.exprwithvalues + ' equals: '+ str(self.expressioncheck))
        print 'Expression to check: ' + self.exprwithvalues
        print 'Expression is: '+ str(self.expressioncheck)
        print self.pairs

    def initlists(self):
        'sets up variable list and value list of pairing'
        for i in self.variables:
            if i not in self.vals:
                self.vals.append(i)
        for r_p in self.vals:
            if not self.pairs:
                self.pairs.append((r_p, ''))
                continue
            for x in self.pairs:
                if x[0] == r_p:
                    break
            else:
                self.pairs.append((r_p, ''))

    def initvariables(self):
        'creates the variables'
        indexcount = 0
        for index in self.expression:
            if(ord(index) >= 65) and (ord(index) <= 90):
                self.expression = self.expression.replace(index, chr(ord(index) + 32))
                index = chr(ord(index) + 32)
            if(ord(index) >= 97) and (ord(index) <= 122):
                pass
            else:
                continue
            if not self.variables:
                self.variables.append(index)
                continue
            elif index != self.variables[indexcount]:
                self.variables.append(index)
            indexcount += 1
    def setvariables(self, variable_string):
        'Updates list of tuples that represent each variables value'
        for i in range(0, len(self.pairs), 1):
            new_pair = self.pairs[i]
            new_pair = (new_pair[0], variable_string[i])
            self.pairs[i] = new_pair
        self.exprwithvalues = ''
        for char in self.expression:
            if (ord(char) >= 97) and (ord(char) <= 122):
                for var in self.pairs:
                    if char is var[0]:
                        self.exprwithvalues += var[1]
            else:
                self.exprwithvalues += char

    def setoperations(self, string):
        'sets operations to fit CNF convention'
        string = string.replace('*', ' or ')
        string = string.replace('+', ' and ')
        string = string.replace('!', ' not ')
        self.exprwithvalues = string
        return self.exprwithvalues

def readfile(filename):
    'Runs test cases created from a saved file'
    file_info = open(filename, 'r')
    data_list = file_info.readlines()
    file_info.close()
    return data_list

def seperatedata(atspecificindex, runlimit, data_list):
    'Seperates data list that the readfile function returns'
    if not atspecificindex:
        runcount = 0
        while runcount <= runlimit and runcount <= len(data_list):
            runcount += 1
            if data_list[runcount] == "\n":
                continue
            _string = _parser(data_list[runcount])
            _string.testparse()
    else:
        if runlimit <= len(data_list):
            if data_list[runlimit] == "\n":
                if runlimit + 1 > len(data_list):
                    runlimit -= 1
                else:
                    runlimit += 1
            _string = _parser(data_list[runlimit])
            return _string
        else:
            print 'OUT OF BOUNDS'

def savefile(_string):
    'save expression from parser'
    file_info = open('SavedInfo.txt', 'a+')
    file_info.write(_string + '\n')
    file_info.close()

if __name__ == '__main__':
    seperatedata(True, 3, readfile('TestReader.txt'))


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
