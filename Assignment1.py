#>>>>Question 1
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 

for item in range(1,6):
  for j in range(1,item+1):
    print(j,end="")
  print()

#>>>>Question 2
# *
# * *
# * * *
# * * * *
# * * * * *


for item in range(1,6):
  for j in range(1,item+1):
    print('*',end="")
  print()

#>>>>>>Question 3
ls=[4,78,43,23,65,-78,-11,3,8,64]
for item in ls:
  if item>max:
    max=item
  elif item<min:
    min=item
print(min)
print(max)

