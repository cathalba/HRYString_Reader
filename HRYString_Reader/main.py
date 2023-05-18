# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re



def find_zero_indices(string):
    indices = []
    for i, char in enumerate(string):
        if char == '0':
            indices.append(i)
    return indices


def search_string_in_file(file_path, search_string, regex, fail_count):

    try:
        with open(file_path, 'r') as file:
            found = False
            #print("searching for" + '"HRYIndex": ' + search_string)
            for line in file:
                if str('"HRYIndex": ' + search_string) in line:
                    ##print(f"Found '{search_string}' in line {line_number}:")
                    #print(line)
                    found = True
                if found and re.search(regex, line) and (fail_count == 0):
                    fail = re.search(regex, line).group(regex_group)
                    fail_count += 1
                    #print("HRY partition to ignore = " + str(fail))
                    failing_par = str(fail)
                    partition_list.append(failing_par)
            if not found:
                print(f"'{search_string}' not found in the file.")
    except FileNotFoundError:
        print("File not found.")




# Example usage


#binary_string = '11111100000111001111111'
binary_string = input("please provide your HRY string: ")

zero_indices = find_zero_indices(binary_string)
print("HRY indices:", zero_indices)
regex = r"HRYPrint\"\: \"(.*)(\")"
regex_group = 1
fail_count = 0
partition_list = []
partition_str = str("PartitionsToIgnore = \"")
count = 0

#file_path = "C:\\Users\\cathalba\\source\\repos\\lnl\\Modules\\SCN_CCF\\InputFiles\\UCLK_HRY.json"
file_path = input("please provide your HRY json  filepath: ")

for element in zero_indices:
    element = str(element)
    search_string_in_file(file_path, element, regex, fail_count)
    #partition_list.append(failing_par)
    #print("failng par = " + failing_par)


#print(partition_list)

for i in partition_list:
    partition_str += i
    count += 1
    if count < len(partition_list):
        partition_str += ","
    else:
        partition_str += "\";"


print(partition_str)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
