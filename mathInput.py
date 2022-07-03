import math

rawFunc = input("Enter: ")

rawFunc = rawFunc.replace('sin', 'math.sin')
rawFunc = rawFunc.replace('cos', 'math.cos')
rawFunc = rawFunc.replace('tan', 'math.tan')
rawFunc = rawFunc.replace('sinh', 'math.sinh')
rawFunc = rawFunc.replace('cosh', 'math.cosh')
rawFunc = rawFunc.replace('tanh', 'math.tanh')

print(rawFunc)

f = lambda x: eval(rawFunc)
y = f(math.pi * 0.5)
print(y)