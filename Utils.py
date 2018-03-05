# title: Utils
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh
# purpose: Provides various utility functions to our program


def isInt(val):
    """
    Tries to convert value into an integer

    :param val: the value to be converted
    :return: True, if the conversion succeeded
    """
    try:
        int(val)
        # conversion succeeded
        return True
    except ValueError:
        # conversion failed
        return False


def file_to_nums(file_path):
    """
    Converts a file of numbers into a list of numbers.
    Assumes numbers are separated by new-lines.

    :param file_path: the path to the file
    :return: the list of numbers
    """

    # create an empty list
    num_list = []

    # open the path as "file" -- this automatically closes the file
    with open(file_path) as file:
        # get each line in the file
        for i, line in enumerate(file, 1):
            # strip the line of "\n"
            line = line.rstrip()

            # check if the line is an integer
            if isInt(line):
                # if int, add to list
                num_list.append(int(line))
            else:
                # otherwise, skip the line
                print("*!* line", i, "skipped in file || not an int:", line, "*!*")

    # return the list
    return num_list

def commas_to_nums(comma_string):
    """
    Converts a list of ints separated by commas into a Python list of ints.

    :param comma_string: the comma-separated int string
    :return: a Python list of ints
    """

    # define the list of ints to return
    num_list = []

    # remove all spaces
    space_free = comma_string.replace(" ", "")

    # split the string by commas
    comma_split = space_free.split(",")

    # for each part in the split
    for part in comma_split:
        # check if the part is an integer
        if isInt(part):
            # append the part
            num_list.append(int(part))
        else:
            print("*!* part skipped || not an integer:", part, "*!*")

    # return the list
    return num_list
