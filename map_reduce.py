import sys
import functools

#for every line in file, count how many each word occurs
def mapper(line):
 d = dict()
 words = line.split()
 for w in words:
 if w not in d:
 d[w] = 1
 else:
 d[w] += 1
 return d
 
#for every line from map(), update dictionary with word counts 
def reducer(x, y):
 if x == 0:
 x = dict()
 for valY in y:
 if valY in x:
 x[valY] += y[valY]
 else:
 x[valY] = y[valY]
 return x
 
#print dictionary sorted by key
def printResults(result):
 for i in sorted(result.keys()): print(i, ": ", result[i])
 
if len(sys.argv) != 2: sys.exit("Invalid arguments provided. Please provide file to
read from")
file = open(sys.argv[1], 'r')
iter = map(mapper, file)
printResults(functools.reduce(reducer, iter, 0))
file.close()