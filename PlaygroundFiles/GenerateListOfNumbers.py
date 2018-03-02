# !!! DO NOT INCLUDE IN FINAL PROJECT !!!
#
# title: GenerateFileOfInts
# author: Jordan Stremming
# purpose: Generates a file of N integers separated by new lines
import sys
import time
from pathlib import Path
from random import Random


def __get_output_path():
    # get the input from user
    response = input("Path to output file (*.txt): ")
    while ".txt" not in response:
        print("\tERROR: missing .txt extension\n")
        response = input("Path to output file (*.txt): ")

    # if the path exists, ask if overwrite is OK
    if Path(response).exists():
        # ask if user wants to overwrite, validate
        overwrite = input("\tWARNING: file already exists, overwrite anyway? (Y/N): ")
        while overwrite not in ["Y", "N", "y", "n"]:
            print("\t\tINVALID INPUT")
            overwrite = input("\tWARNING: file already exists, overwrite anyway? (Y/N): ")

        # if not, exit program
        if overwrite in ["N", "n"]:
            print("** please restart the application **")
            time.sleep(3)
            sys.exit()

    # return path given by user
    return response


def __get_size_n():
    # get the size N from the user
    size_n = -1
    while size_n <= 0:
        try:
            size_n = int(input("Please enter size N (int): "))

            if size_n <= 0:
                print("\tSorry, N must be larger than 0")

        except Exception:
            print("\tSorry, that is not an integer.")

    # return the size N given by user
    return size_n


def __gen_list_of_n(size_n):
    # start with a blank list and Random class
    random = Random()

    # generates a randomized list without duplicates
    return_list = random.sample(range(-size_n, size_n), size_n)

    # return the list
    return return_list


def __output_nums_to_file(out_path, num_list):
    # open the file, this automatically closes the file
    with open(out_path, 'w') as file:
        # for each number in the list
        for num in num_list:
            # output the number as a string and add newline
            file.write(str(num) + "\n")


# print header
print("="*50)
print("{:^50}".format("** RANDOM INTEGER FILE GENERATOR **"))
print("{:^50}".format("please be careful when overwriting!"))
print("="*50)

# get the path from the user
path = __get_output_path()
print()
print("-"*50)

# get the size of N from the user
n = __get_size_n()
print()
print("-"*50)

# generate the list of size N
print("* generating list of size", n)
num_list = __gen_list_of_n(n)
print("\t", num_list)
print()
print("-"*50)

# output the numbers to the file
print("* outputting numbers to", path)
__output_nums_to_file(path, num_list)
print()
print("-"*50)

# all done
print("All done! Have a nice day! :D")
time.sleep(5)
