from util import christmas_input

FILE = './input.txt'
sonar_list = [int(i) for i in christmas_input.file_to_array(FILE)]

total_increases = 0
for i in range(1, len(sonar_list)):
    if sonar_list[i] > sonar_list[i-1]:
        total_increases += 1

print("Increases: ", total_increases)
