'The genetic algorithm to find a solution to CNF expression'
import _parser
import random

class Algorithm(object):
    'genetic algorithm'
    def __init__(self, parser):
        self.parserclass = parser
        self.expression = ''
        self.valuesetlist = []
        self.correctnessvalue = 0
        self.curtestexpr = '11111'
        self.expressioncheck = False


    def run(self):
        'Runs genetic algorithm'
        generation = 0
        repeatcount = 0
        self.initrandomvalues()
        while self.expressioncheck is False:
            if repeatcount < len(self.valuesetlist):
                self.algorithminitparse(self.valuesetlist[repeatcount])
                repeatcount += 1
            else:
                generation += 1
                repeatcount = 0
                index = 0
                bestvalues = []
                expr_wit_fitness = []
                for x in self.valuesetlist:
                    for y in x:
                        if index >= len(self.curtestexpr):
                            continue
                        if y == self.curtestexpr[index]:
                            self.correctnessvalue += 1
                        index += 1
                    expr_wit_fitness.append((x, self.correctnessvalue))
                    self.correctnessvalue = 0

                comparedindex = 0
                for x in expr_wit_fitness:
                    comparedindex += 1
                    if comparedindex >= len(expr_wit_fitness):
                        comparedindex = 0
                    comparableindex = expr_wit_fitness[comparedindex]
                    if int(x[1]) >= int(comparableindex[1]):
                        if len(bestvalues) >= 2:
                            bestvalue0 = bestvalues[0]
                            bestvalue1 = bestvalues[1]
                            if int(bestvalue0[1]) >= int(bestvalue1[1]):
                                bestvalues.remove(bestvalue1)
                            else:
                                bestvalues.remove(bestvalue0)
                            bestvalues.append(x)
                        else:
                            bestvalues.append(x)

                self.valuesetlist = []
                self.valuesetlist.append(bestvalues[0])
                self.valuesetlist.append(bestvalues[1])
                self.initrandomvalues()

    def algorithminitparse(self, valueset):
        'Initial parse setup for algorithm'
        print 'Init expression: '+ self.parserclass.expression
        self.parserclass.initvariables()
        self.parserclass.initlists()
        self.parserclass.setvariables(valueset)
        self.expression = self.parserclass.setoperations(self.parserclass.exprwithvalues)
        self.expressioncheck = bool(eval(self.expression))
        _parser.savefile(self.expression + ' equals: '+ str(self.expressioncheck))
        print 'Expression to check: ' + self.expression
        print 'Expression is: '+ str(self.expressioncheck)

    def initrandomvalues(self):
        'sets up a list of 0s and 1s'
        while len(self.valuesetlist) < 10:
            numcounter = 0
            randlist = ''
            while numcounter <= 10:
                numcounter += 1
                randlist += str(random.randint(0, 1))
            valueset = randlist
            self.valuesetlist.append(valueset)
        return self.valuesetlist[0]

if __name__ == '__main__':
    print 'test'
    ALGO = Algorithm(_parser.seperatedata(True, 4, _parser.readfile('TestReader.txt')))
    ALGO.run()
