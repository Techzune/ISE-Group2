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
