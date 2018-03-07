# Title: BubbleSort
# Author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# Purpose: Interface for algorithm files, ensures common ground


class Algorithm:
    """
    An interface for the algorithm files.
    All algorithm files MUST extend this interface.

    @param num_list            the list of numbers the algorithm will sort
    @param viz_enabled         true, if the visualization window should show
    @param highlight_enabled   true, if the code-highlighting window should highlight lines
    @param steps_enabled       true, if the algorithm should run in step-by-step mode
    @param delay               the time, in seconds, the algorithm should pause in operations
    """
    num_list = []
    viz_enabled = False
    highlight_enabled = False
    steps_enabled = False
    delay = 0

    def __init__(self, viz_window, cod_window):
        """
        Initializes the Algorithm file.

        :param viz_window: the visualization window object
        :param cod_window: the code-highlighting window object
        """
        self.viz_window = viz_window
        self.cod_window = cod_window

    def enable_visualization(self, new_value):
        """
        Sets if the visualization window should show the visualization.

        :param new_value: the new value of the boolean
        :return: None
        """
        self.viz_enabled = new_value

    def enable_highlight(self, new_value):
        """
        Sets if the code-highlight window should highlight lines of code.

        :param new_value: the new value of the boolean
        :return: None
        """
        self.highlight_enabled = new_value

    def enable_steps(self, new_value):
        """
        Sets if the algorithm should run in step-by-step mode.

        :param new_value: the new value of the boolean
        :return: None
        """
        self.steps_enabled = new_value

    def set_delay(self, seconds):
        """
        Sets the delay, in seconds, for each algorithm operation.

        :param seconds: time, in seconds, for the delay
        :return: None
        """
        self.delay = seconds

    def sort(self, num_list):
        """
        Runs the algorithm sorting function.
        Sets data on GUI interfaces.

        :param num_list: the list of numbers to be sorted
        :return: the sorted list of numbers
        """
        raise NotImplementedError("sort(num_list) must be implemented in an algorithm!")
