import random
import math

points = []

for i in range(20):
  num1 = random.random()
  num2 = random.random()

  num1 = int((num1*100))%80
  num2 = int((num2*100))%80

  if(num1<26 or num2<26):
    points.append((num1, num2, "positive"))
  else:
    points.append((num1, num2, "negative"))

print(points)

import math 

def knn(points, input, k):

  closest = []

  for i in points:

    x = i[0]-input[0]
    x = x*x

    y = i[1]-input[1]
    y = y*y

    dist = math.sqrt(x+y)

    closest.append((dist,i[2]))

  closest.sort()

  pos = 0
  neg = 0

  for i in range(k):

    val = closest[i][1]

    if(val=="positive"):
      pos = pos + 1
    else:
      neg = neg + 1

  if(pos>=neg):
    return "positive"
  else:
    return "negative"

limit = 26
input = (40,30)

for i in range(1,6):
  ans = knn(points, input, 5)
  print(i, ans)