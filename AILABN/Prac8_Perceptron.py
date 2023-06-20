AND_GATE = [0, 0, 0, 1]
OR_GATE = [0, 1, 1, 1]
NAND_GATE = [1, 1, 1, 0]
NOR_GATE = [1, 0, 0, 0]

x = [[0, 0], [0, 1], [1, 0], [1, 1]]

w1,w2 = 1,1
count_and = 0
count_or = 0
count_nand = 0
count_nor = 0


and_b = [0,-1,-1,-1]
or_b = [0,0,0,-1]
nand_b = [1,0,0,-2]

for i in range(0,4):
  print(x[i][0]*w1 + x[i][1]*w2 + and_b[i])
  count_and=count_and + 1

print("The iterations for AND gate are ",count_and)

for i in range(0,4):
  print(x[i][0]*w1 + x[i][1]*w2 + or_b[i])
  count_or=count_or + 1

print("The iterations for OR gate are ",count_or)

for i in range(0,4):
  print(x[i][0]*w1 + x[i][1]*w2 + nand_b[i])
  count_nand=count_nand + 1

print("The iterations for NAND gate are ",count_nand)