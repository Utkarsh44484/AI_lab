def activation_function(value):

  if value >= 0:
      value = 1
  else:
      value = 0

  return value

def Perceptron(inputs, output, learning_rate=0.1, max_iterations=1000):

  random1 = random.random()
  random2 = random.random()
  random3 = random.random()

  random1 = (random1*10)
  random2 = (random2*10)
  random3 = (random3*10)

  w = [random1, random2]
  b = random3

  for i in range(max_iterations):

    error = 0

    for i in range(len(inputs)):

      input = inputs[i]
      actual = output[i]

      x1 = input[0]
      x2 = input[1]
      w1 = w[0]
      w2 = w[1]


      calculated = w1*x1 + w2*x2 + b

      calculated = activation_function(calculated)

      if(calculated == actual):
        continue

      delta = actual - calculated

      error = error + 1

      w[0] += learning_rate * delta * x1
      w[1] += learning_rate * delta * x2
      b += learning_rate * delta

    if(error == 0):
      return w, b, i

  return w, b, max_iterations+1

import random

INPUTS = [
    [0,0],
    [0,1],
    [1,0],
    [1,1],
]

OUTPUT_AND_GATE = [0, 0, 0, 1]
OUTPUT_OR_GATE = [0, 1, 1, 1]
OUTPUT_NAND_GATE = [1, 1, 1, 0]
OUTPUT_NOR_GATE = [1, 0, 0, 0]

w_and, b_and, iter_and = Perceptron(INPUTS, OUTPUT_AND_GATE)
print(f'AND gate : {iter_and} iterations')
print(w_and, b_and, iter_and, "\n\n")



w_or, b_or, iter_or = Perceptron(INPUTS, OUTPUT_OR_GATE)
print(f'OR gate : {iter_or} iterations')
print(w_or, b_or, iter_or, "\n\n")



w_nand, b_nand, iter_nand = Perceptron(INPUTS, OUTPUT_NAND_GATE)
print(f'NAND gate : {iter_nand} iterations')
print(w_nand, b_nand, iter_nand, "\n\n")




w_nor, b_nor, iter_nor = Perceptron(INPUTS, OUTPUT_NOR_GATE)
print(f'NOR gate : {iter_nor} iterations')
print(w_nor, b_nor, iter_nor, "\n\n")

