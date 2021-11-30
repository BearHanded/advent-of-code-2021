def get_file_and_print(filename):
    fp = open(filename, 'r')
    print(BColors.OKGREEN + "--------")
    print("IMPORTING ", filename)
    print("--------" + BColors.ENDC)
    return fp


def file_to_array(filename):
    fp = get_file_and_print(filename)
    input_iterable = map(lambda x: x.replace("\n", ""), fp.readlines())
    input_array = list(input_iterable)
    return input_array


def file_as_string(filename):
    fp = get_file_and_print(filename)
    input_iterable = map(lambda x: x.replace("\n", ""), fp.readlines())
    input = list(input_iterable)[0]
    return input


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'