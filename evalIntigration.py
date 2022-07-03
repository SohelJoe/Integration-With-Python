import math

class EvalIntegration:
    def __init__(self, func, lowerBound, upperBound, iteration, roundOff=9, type=2):
        self.type = type
        self.series = [2,4]
        self.round = roundOff
        self.iteration = iteration
        self.function = self.evalFunction(func)
        self.lowerBoundString = lowerBound
        self.lowerBound = eval(lowerBound.replace('pi', 'math.pi'))
        self.upperBoundString = upperBound
        self.upperBound = eval(upperBound.replace('pi', 'math.pi'))
        self.stepLengthString = self.stepLengthToString()
        self.stepLength = eval(self.stepLengthString.replace('pi', 'math.pi'))
        self.funtionalValue = 0
    
    def evalFunction(self, rawFunction):
        rawFunction = rawFunction.replace('log', 'math.log')
        rawFunction = rawFunction.replace('sin', 'math.sin')
        rawFunction = rawFunction.replace('cos', 'math.cos')
        rawFunction = rawFunction.replace('tan', 'math.tan')
        rawFunction = rawFunction.replace('^', '**')

        return(lambda x: eval(rawFunction))

    def floatToFraction(self, fValue):
        lowDevisor = 1
        frac, whole = math.modf(fValue * lowDevisor)
        while (frac != 0):
            lowDevisor+=1
            frac, whole = math.modf(fValue * lowDevisor)
        return((int(whole), lowDevisor))

    def stepLengthToString(self):
        if('pi' in self.upperBoundString or 'pi' in self.lowerBoundString):
            lBoundPi = self.lowerBound / math.pi
            uBoundPi = self.upperBound / math.pi
            upper, lower = self.floatToFraction((uBoundPi - lBoundPi)/self.iteration)

            if(upper == 1):
                return(f"(pi/{lower})")
            else:
                return(f"({upper}*pi)/{lower}")
        else:
            upper, lower = self.floatToFraction((self.upperBound - self.lowerBound) / self.iteration)
            return(f"{upper}/{lower}")

    def dataChart(self):
        if(self.type == 2):
            self.series = [2,4]
            finalMultiplier = self.stepLength / 3
            print("\nSeries using Simson's One-Third Law:")
        elif(self.type == 6):
            self.series = [2,5,1,6,1,5]
            finalMultiplier = (3 * self.stepLength) / 10
            print("\nSeries using [5,1,6,1,5,2,5]:")
        elif(self.type == 1):
            self.series = [2]
            finalMultiplier = self.stepLength / 2
            print("\nSeries using [2]:")
        else:
            print("\nSeries Not Found.")
            return

        print ("{:<20} {:<22} {:<4} {:<22}".format('Xn','f(Xn)','Cn','CnYn'))

        for i in range(self.iteration + 1):
            Xn = (self.lowerBound + (self.stepLength * i))

            if(i == 0 or i == self.iteration):
                Cn = 1
            else:
                Cn = self.series[i % self.type]
            
            Yn = self.function(Xn)
            CnYn = (Cn * Yn)
            self.funtionalValue += CnYn
            
            print ("{:<20} {:<22} {:<4} {:<22}".format(f"{self.lowerBoundString}+[{i}*{self.stepLengthString}]", round(Yn, self.round), Cn, round(CnYn, self.round)))
        
        self.funtionalValue =  round(self.funtionalValue * finalMultiplier, self.round)


# rawFunction = input("Enter: ")
rawFunction = '(2.3*(sin(2*x))+3.2*(cos(2*x)))^(1/2)'
# lowerBound = input("Lower Bound: ")
lowerBound = '0'
# upperBound = input("Upper Bound: ")
upperBound = 'pi/4'
# iteration = int(input("Iterations: "))
iteration = 12

integration = EvalIntegration(rawFunction, lowerBound, upperBound, iteration, type=2)
integration.dataChart()
print(f"\nThe Output: {integration.funtionalValue}")