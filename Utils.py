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
        for line in file:
            # strip the line of "\n"
            line = line.rstrip()

            # check if the line is an integer
            if isInt(line):
                # if int, add to list
                num_list.append(int(line))
            else:
                # otherwise, skip the line
                print("WARNING: line skipped in file, not integer:", line)

    # return the list
    return num_list
