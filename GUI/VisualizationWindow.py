# title: VisualizationWindow
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: Backbone of visualization window; displays graphical representation of algorithm

from PyQt5.QtCore import Qt, QLineF
from PyQt5.QtGui import QPen, QPainter, QFont, QColor
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QGraphicsTextItem, \
    QGraphicsItem

import Utils

# the master radius (size) of all nodes visually
NODE_RADIUS = 22

# the colors of graphs
GRAPH_COLORS = [Qt.black, Qt.blue, Qt.red, Qt.yellow, Qt.green]


class VisualizationWindow(QGraphicsView):

    def __init__(self, main_app):
        # create a graphics scene
        self._scene = QGraphicsScene()

        # run the init of QGraphicsView
        super().__init__(self._scene)

        # setup the view for the graphics
        self.view = QGraphicsView(self._scene)
        self.setRenderHint(QPainter.Antialiasing)
        self.setAlignment(Qt.AlignVCenter)
        self.setWindowTitle("SWEG2 - Visualization Window")
        self.resize(600, 400)

        # save a reference to the main_app
        self._main_application = main_app

        # stores the graphs in the window
        self._graph_list = []

        # holds if we are actually being used
        self.do_show = False

    def resizeEvent(self, event):
        """
        Override resizeEvent to automatically center graphs
        """

        self.center_all()
        super().resizeEvent(event)

    def show(self):
        """
        Overrides original show() method
        """

        self.do_show = True
        super().show()

    def center_all(self):
        """
        Centers the view on the center of the scene
        """

        rect = self._scene.sceneRect()
        self.centerOn(rect.center())

        self.fitInView(rect, Qt.KeepAspectRatio)

    def add_graph(self, g_index, name=""):
        """
        Adds a graph to the view

        :param g_index: the graph's index (starts at 0)
        :param name: the display name of the graph
        """

        color = GRAPH_COLORS[g_index % 5]

        if g_index == 0:
            # place graph at point 0
            self._graph_list.append(Graph(self, self._scene, 0, color, name))
        else:
            # space out the graph
            self._graph_list.append(Graph(self, self._scene, g_index + NODE_RADIUS * 3, color, name))

    def validate_graph(self, g_index):
        """
        Checks if the graph exists, creates it if not

        :param g_index: the index of the graph (starts at 0)
        :return: the graph
        """

        # check if the view has the specified graph
        diff = len(self._graph_list) - g_index
        if diff == 0:
            # the graph needs to be created
            self.add_graph(g_index)
        elif diff < 0:
            # out of range
            raise IndexError("out of range of number of graphs, did you skip an index?")

        # return the graph
        return self._graph_list[g_index]

    def add_node(self, text, g_index: int = 0):
        """
        Adds a node to the specified graph

        :param text: the node value
        :param g_index: the index of the graph (starts at 0)
        """

        # validate the graph
        graph = self.validate_graph(g_index)

        # add the node
        graph.add_node(text)

    def add_nodes(self, num_list: list, g_index: int = 0):
        """
        Adds multiple nodes from a list to a graph
        (uses add_node(num))

        :param num_list: the list of numbers to add
        :param g_index:  the index of the graph (starts at 0)
        """

        # validate the graph
        graph = self.validate_graph(g_index)

        # loop through the numbers
        for num in num_list:
            # add the number
            graph.add_node(num)

    def highlight_node(self, index: int, value: bool, g_index: int = 0):
        """
        Sets the highlight value of the node in the graph

        :param index: the index of the node
        :param value: true, to highlight the node
        :param g_index: the index of the graph
        """

        # validate the graph
        graph = self.validate_graph(g_index)

        # change the highlight of the node
        graph.highlight_node(index, value)

    def set_node(self, index: int, value, g_index: int = 0):
        """
        Sets the value of the node in the graph

        :param index: the index of the node
        :param value: the value of the node
        :param g_index: the index of the graph
        """

        # validate the graph
        graph = self.validate_graph(g_index)

        # change the highlight of the node
        graph.set_node(index, value)

    def swap_nodes(self, a_idx: int, b_idx: int, highlight: bool = True, g_index: int = 0, msec: int = 500):
        """
        Swaps the values of two nodes
        :param a_idx: the index of Node a
        :param b_idx: the index of Node b
        :param highlight: when true, highlight the nodes before swapping (default: True)
        :param g_index: the index of the graph
        :param msec: how long (in milliseconds) to pause in between highlights and swaps
        """

        # validate the graph
        graph = self.validate_graph(g_index)

        # swap the nodes in the graph
        graph.swap_nodes(a_idx, b_idx, highlight, msec)


class Graph:
    """
    A graph of circular nodes
    """

    def __init__(self, view, scene, y_pos, color, name):
        self._view = view
        self._scene = scene
        self._y_pos = y_pos
        self._color = color
        self._name = name
        self._node_list = []

        # create name text
        self._text = QGraphicsTextItem(self._name)
        self._text.setDefaultTextColor(color)
        self._text.setPos(-NODE_RADIUS, self._y_pos - NODE_RADIUS - 20)
        self._scene.addItem(self._text)

    def add_node(self, text):
        """
        Adds a node to the graph
        (automatically generates edges)

        :param text: the node value
        """

        if len(self._node_list) == 0:
            # insert the node without edges
            node = Node(self._scene, 0, self._y_pos, str(text), self._color)
            self._node_list.append(node)
        else:
            # there are existing nodes, so
            # get the last node in the list
            last = self._node_list[-1]

            # insert the node and add edges
            node = Node(self._scene, last.x() + NODE_RADIUS * 3, self._y_pos, str(text), self._color)
            self._scene.addItem(node)
            self._node_list.append(node)
            self._scene.addItem(Edge(last, node, self._color))

        # center the view
        self._view.center_all()

    def add_nodes(self, num_list: list):
        """
        Adds multiple nodes from a list
        (uses add_node(num))

        :param num_list: the list of numbers to add
        """

        # loop through the numbers
        for num in num_list:
            # add the number
            self.add_node(num)

    def highlight_node(self, index: int, value: bool):
        """
        Sets the highlight value of the node

        :param index: the index of the node
        :param value: true, to highlight the node
        """

        # change the highlight of the node
        self._node_list[index].set_highlight(value, text_color=self._color, fill_color=QColor(200, 200, 200))

    def set_node(self, index: int, value):
        """
        Changes the value of the specified node
        """

        # change the highlight of the node
        self._node_list[index].set_text(str(value))

    def swap_nodes(self, a_idx: int, b_idx: int, highlight: bool = True, msec: int = 500):
        """
        Swaps the values of two nodes
        :param a_idx: the index of Node a
        :param b_idx: the index of Node b
        :param highlight: when true, highlight the nodes before swapping (default: True)
        :param msec: how long (in milliseconds) to pause in between highlights and swaps
        """

        # ignore swapping of same nodes
        if a_idx == b_idx:
            return

        # get the nodes to swap
        a = self._node_list[a_idx]
        b = self._node_list[b_idx]

        # enable the highlight, if supposed to
        a.set_highlight(highlight)
        b.set_highlight(highlight)

        # delay, if specified
        Utils.sleep_qt(msec)

        # swap the texts
        a_old = a.text()
        a.set_text(b.text())
        b.set_text(a_old)

        # delay, if specified
        Utils.sleep_qt(msec)

        # remove the highlight, if any
        a.set_highlight(False)
        b.set_highlight(False)

        # delay, if specified
        Utils.sleep_qt(msec)


class Node(QGraphicsEllipseItem):
    """
    A circle that contains text and supports Edge objects
    """

    def __init__(self, scene, pos_x, pos_y, text="", color=Qt.blue):
        """
        Initializes the Node object

        :param scene: the scene where the Node will be added
        :param pos_x: the X position of the Node in the scene
        :param pos_y: the Y position of the Node in the scene
        :param text: the text for the node (default: "")
        :param color: the color of the edge
        """

        # run QGraphicsEllipseItem init to draw circle
        super().__init__(-NODE_RADIUS, -NODE_RADIUS, 2 * NODE_RADIUS, 2 * NODE_RADIUS)

        # stores any edges
        self.edges = []

        # set the color, position
        self.setBrush(Qt.white)
        self.setPen(QPen(color, 2.5))
        self.setPos(pos_x, pos_y)
        self.setZValue(1)

        # add self to the items
        scene.addItem(self)

        self.node_text = text
        self.color = color

    def paint(self, painter, options, widget=None):
        """
        Overrides the built in paint(...) function
        """
        super().paint(painter, options, widget)

        # draw the text for the circle
        painter.drawText(self.rect(), Qt.AlignCenter | Qt.TextSingleLine, self.text())

    def add_edge(self, edge):
        """
        Stores an edge inside the node's edge list
        """
        self.edges.append(edge)

    def text(self):
        """
        Returns the text of the Node
        """
        return self.node_text

    def set_text(self, text):
        """
        Sets the text of the number inside the node
        """
        self.node_text = text
        self.update()

    def set_highlight(self, enabled: bool, text_color=Qt.white, fill_color=None):
        """
        Changes if the Node circle is highlighted

        :param enabled: True, if the node is highlighted
        :param text_color: the color to use for text (default: white)
        :param fill_color: the color to use as a filler (default: graph color)
        """

        # use self color if not defined
        if fill_color is None:
            fill_color = self.color

        # set the background color if highlighted
        if enabled:
            self.setPen(QPen(text_color, 2.5))
            self.setBrush(fill_color)
        else:
            self.setPen(QPen(self.color, 2.5))
            self.setBrush(Qt.white)

        # update the visual node
        self.update()


class Edge(QGraphicsLineItem):
    """
    A line that goes in between Node objects
    """

    def __init__(self, source, destination, color=Qt.blue):
        """
        Initializes the Edge object
        :param source: the source of the edge (from)
        :param destination: the destination of the edge (to)
        :param color: the color of the edge
        """

        # run the QGraphicsLineItem initialization
        super().__init__()

        # store the source
        self.source = source

        # store the destination
        self.destination = destination

        # add this edge to the source
        self.source.add_edge(self)

        # add this edge to the destination
        self.destination.add_edge(self)

        # define the line style
        self.setPen(QPen(color, 2.5))

        # apply changes
        self.adjust()

    def adjust(self):
        """
        Updates the edge's line and geometry
        """

        # draw the line
        self.prepareGeometryChange()
        self.setLine(QLineF(self.destination.pos(), self.source.pos()))
