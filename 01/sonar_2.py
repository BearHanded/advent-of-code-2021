from util import christmas_input

FILE = './input.txt'
sonar_list = [int(i) for i in christmas_input.file_to_array(FILE)]

total_increases = 0
for i in range(3, len(sonar_list)):
    idx_a = i-1
    idx_b = i

    sum_a = sonar_list[idx_a-2] + sonar_list[idx_a-1] + sonar_list[idx_a]
    sum_b = sonar_list[idx_b-2] + sonar_list[idx_b-1] + sonar_list[idx_b]

    if sum_b > sum_a:
        total_increases += 1;

print("Increases: ", total_increases);
