name = input("Your name:")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

second_file = open("name.txt", 'r')
name = second_file.read()
print(f"your name is {name}")
second_file.close()

third_file = open("numbers", 'r')
read_file = third_file.readlines()
number = int(read_file[0]) + int(read_file[1])
third_file.close()
print(f"the total is {number}")

fourth_file = open("numbers", 'r')
read_number = fourth_file.readlines()
total_number = 0
for i in range(0, len(read_number)):
    total_number += int(read_number[i])
fourth_file.close()
print(f"the total number is {total_number}")
