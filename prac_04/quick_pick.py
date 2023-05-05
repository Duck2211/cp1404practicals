import random
MIN_VALUE = 1
MAX_VALUE = 45

for i in range(0,5):
    number_list = []
    for j in range(0,6):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        while number in number_list:
            number = random.randint(MIN_VALUE, MAX_VALUE)
        number_list.append(number)
    number_list.sort()
    print(" ".join("{:2}".format(number) for number in number_list))