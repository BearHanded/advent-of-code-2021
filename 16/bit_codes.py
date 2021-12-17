from util import christmas_input
import math

FILE_1 = './input.txt'
TEST_FILE = './test_input.txt'
version_sum = 0
DEBUG = False


def round_length(number):
    return 4 * round(number / 4)


def get_literal(packet):
    global version_sum
    version = packet[0:3]  # VVV
    version_sum += int(version, 2)
    final_number = False
    idx = 6
    bits = ""
    while not final_number:  # get groups of 5 until last is zero
        if packet[idx] == "0":
            final_number = True
        bits += packet[idx + 1: idx + 5]
        idx += 5

    number_out = int(bits, 2)
    # command_length = round_length(idx + 4)
    return number_out, idx


def perform_operand(sub_packets, type_id):
    result = 0
    if type_id == 0:  # SUM
        return sum(sub_packets)
    elif type_id == 1:  # PRODUCT
        out = 1
        for sub in sub_packets:
            out *= sub
        return out
    elif type_id == 2:  # MIN
        return min(sub_packets)
    elif type_id == 3:  # MAX
        return max(sub_packets)
    elif type_id == 5:  # >
        return int(sub_packets[0] > sub_packets[1])
    elif type_id == 6:  # <
        return int(sub_packets[0] < sub_packets[1])
    elif type_id == 7:  # ==
        return int(sub_packets[0] == sub_packets[1])
    return result


def operator(packet):
    global version_sum
    version = packet[0:3]  # VVV
    type_id = int(packet[3:6], 2)  # TTT
    version_sum += int(version, 2)
    length_type = packet[6]  # I
    length_size = 15 if length_type == "0" else 11
    length_size_end = 7 + length_size
    length = int(packet[7:length_size_end], 2)  # L

    total_length = 7 + length_size

    sub_packets = []
    idx = length_size_end
    if length_type == "0":  # next 15 are total length of sub-packets
        queue = packet[idx:idx + length]
        while len(queue) > 0 and "1" in queue:
            subtype_id = queue[3:6]  # TTT  (4 is literal)
            operation = COMMAND_TYPES.get(int(subtype_id, 2), operator)
            out, sub_length = operation(queue)
            queue = queue[sub_length:]
            sub_packets.append(out)
        total_length += length
    else:  # next 11 are number of sub-packets
        for _ in range(length):
            subtype_id = packet[idx + 3:idx + 6]  # TTT  (4 is literal)
            operation = COMMAND_TYPES.get(int(subtype_id, 2), operator)
            out, sub_length = operation(packet[idx:])
            sub_packets.append(out)
            idx += sub_length
            total_length += sub_length

    output = perform_operand(sub_packets, type_id)
    return output, total_length


def hex_to_binary(hex_str):
    num_of_bits = int(len(hex_str) * math.log2(16))
    return bin(int(hex_str, 16))[2:].zfill(num_of_bits)


COMMAND_TYPES = {
    4: get_literal
}


def run(hex_str, version_display=False):
    binary = hex_to_binary(hex_str)
    global version_sum
    version_sum = 0
    while len(binary) > 0 and "1" in binary:
        type_id = binary[3:6]  # TTT  (4 is literal)
        operation = COMMAND_TYPES.get(int(type_id, 2), operator)
        output, command_length = operation(binary)
        binary = binary[command_length:]
    if version_display:
        print("Version Sum", version_sum, end=" ")
    print("Output:", output)


# Parse
if DEBUG:
    print("Diagnostics: ")
    # print("Versions")
    # run("D2FE28", version_display=True)
    # run("38006F45291200", version_display=True)  # 10, 20
    # run("EE00D40C823060", version_display=True)  # 1 2 3
    # run("8A004A801A8002F478", version_display=True)  # v16
    # run("620080001611562C8802118E34", version_display=True)  # v12
    # run("C0015000016115A2E0802F182340", version_display=True)  # v23
    print("Outputs")
    run("C200B40A82")
    run("04005AC33890")  # v31
    run("880086C3E88112")  # v31
    run("CE00C43D881120")  # v31
    run("D8005AC2A8F0")  # v31
    run("F600BC2D8F")  # v31
    run("9C005AC2F8F0")  # v31
    run("9C0141080250320F1802104A08")  # v31
else:
    print("\nRunning")
    transmission = christmas_input.file_as_string(FILE_1)
    run(transmission, version_display=True)
