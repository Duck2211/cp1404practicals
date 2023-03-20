"""
algorithm:
#1:for i in range(1, 21, 2)
display i

#a:for u in range(0,110, 10)
display u

#b: for o in range(20, 0,-1)
display o

#2: get amount
# for i in range (amount)
#  for u in ["*"]
#   display u
#a: get amount
lines = 0
for i in range (amount)
    lines += 1
    for i in range (lines)
        print("*", end='')
    display()
"""
# 1: for loop
# for i in range(1, 21, 2):
#     print(i, end=' ')


# for u in range(0,110, 10):
#     print(u, end=' ')

# for o in range(20, 0,-1):
#     print(o, end=' ')

# 2: printing stars
# amount= int(input("number of stars:"))
# for i in range (amount):
#  for u in ["*"]:
#   print(u, end='')
# 3:printing starts in line
amount = int(input("number of stars:"))
# lines = 0
# for i in range (amount):
#     lines += 1
#     for i in range (lines):
#         print("*", end='')
#     print()

# better method:
for i in range(1, amount + 1, 1):
    print('*' * i)
print()
