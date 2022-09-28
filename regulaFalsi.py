import math

class regulaFalsi:
    def __init__(self, func, dFunc, roundOff=3):
        self.round = roundOff
        self.function = self.evalFunction(func)
        self.dFunction = self.evalFunction(dFunc)

    def evalFunction(self, rawFunction):
        rawFunction = rawFunction.replace('log', 'math.log')
        rawFunction = rawFunction.replace('sin', 'math.sin')
        rawFunction = rawFunction.replace('cos', 'math.cos')
        rawFunction = rawFunction.replace('tan', 'math.tan')
        rawFunction = rawFunction.replace('^', '**')

        return(lambda x: eval(rawFunction))
    
    def truncate(self, num):
        return int(num*(10**(self.round + 2)))/(10**(self.round + 2))

    def setInterval(self):
        lower = 0
        upper = 1

        while(self.function(lower) * self.function(upper) >= 0):
            upper = lower
            upper += 1
        
        self.lowerBound = lower
        self.upperBound = upper

    def bisection(self):
        iteration = 0
        Xn = (self.upperBound+self.lowerBound)/2

        print ("\nBisection Table: ")
        print ("{:<3} {:<10} {:<10} {:<10} {:<10}".format('n','An','Bn','Xn', 'f(Xn+1)'))

        while(round(Xn, self.round) != round(self.lowerBound, self.round)):
            print ("{:<3} {:<10} {:<10} {:<10}  {:<10}".format(iteration, self.truncate(self.lowerBound), self.truncate(self.upperBound), self.truncate(Xn), self.truncate(self.function(Xn))))

            if(self.function(Xn) > 0):
                self.upperBound = Xn
            else:
                self.lowerBound = Xn
            
            iteration += 1
            Xn = (self.upperBound+self.lowerBound)/2

        self.bisectionRatio = int(self.lowerBound*(10**self.round))/(10**self.round)
        print(f"\nThe Bisection of the correct ratio: {self.bisectionRatio}")

    def solution(self):
        iteration = 0
        Xn = self.bisectionRatio
        fXn = self.function(Xn)
        dfXn = self.dFunction(Xn)
        Hn = (fXn/dfXn) * (-1)

        print ("\nRegula Falsi Table: ")
        print ("{:<3} {:<10} {:<10} {:<10} {:<12}".format('n','Xn','f(Xn)','df(Xn)', 'Hn = -(f/df)'))

        while(round(fXn, self.round) != round(Hn, self.round)):
            print ("{:<3} {:<10} {:<10} {:<10}  {:<12}".format(iteration, self.truncate(Xn), self.truncate(fXn), self.truncate(dfXn), self.truncate(Hn)))

            iteration += 1
            Xn = Xn - (fXn/dfXn)
            fXn = self.function(Xn)
            dfXn = self.dFunction(Xn)
            Hn = (fXn/dfXn) * (-1)

        print(f"\nThe Solution is: {round(Xn, self.round + 2)}\n")


if(__name__ == "__main__"):
    # rawFunc = "sin(x)+(x^2)-1"
    rawFunc = "x^3-2*(x^2)-2*x+1"
    # derFunc = "cos(x)+2*x"
    derFunc = "3*(x^2)-4*x-2"

    regulaFalsi = regulaFalsi(rawFunc, derFunc)
    regulaFalsi.setInterval()
    regulaFalsi.bisection()
    regulaFalsi.solution()
