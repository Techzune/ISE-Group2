# title: VisualizationWindow
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: Backbone of visualization window; displays graphical representation of algorithm

from PyQt5.QtCore import Qt, QLineF
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsScene, QGraphicsView, QGraphicsLineItem

import Utils

NODE_RADIUS = 22


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

        # stores the nodes visible in the window
        self._node_list = []

        # holds if we are actually being used
        self.do_show = False

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

    def add_node(self, text):
        """
        Adds a node to the visualization window
        (automatically generates edges)

        :param text: the text to display in the node
        :return:
        """

        # if not shown, ignore this request
        if not self.do_show:
            return

        # if the list size is 0
        if len(self._node_list) == 0:
            # insert the node without edges
            node = Node(self._scene, 0, 0, str(text))
            self._node_list.append(node)
        else:
            # there are existing nodes, so
            # get the last node in the list
            last = self._node_list[-1]

            # insert the node and add edges
            node = Node(self._scene, last.x() + NODE_RADIUS * 3, 0, str(text))
            self._scene.addItem(node)
            self._node_list.append(node)
            self._scene.addItem(Edge(last, node))

        # center the view
        self.center_all()

    def add_nodes(self, num_list):
        """
        Adds multiple nodes from a list
        (uses add_node(num))

        :param num_list: the list of numbers to add
        """

        # if not shown, ignore this request
        if not self.do_show:
            return

        # loop through the numbers
        for num in num_list:
            # add the number
            self.add_node(num)

    def highlight_node(self, index: int, value: bool):
        """
        Sets the highlight of the specified node
        """

        # if not shown, ignore this request
        if not self.do_show:
            return

        # change the highlight of the node
        self._node_list[index].set_highlight(value)

    def set_node(self, index: int, value):
        """
        Changes the value of the specified node
        """

        # if not shown, ignore this request
        if not self.do_show:
            return

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

        # if not shown, ignore this request
        if not self.do_show:
            return

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

    def __init__(self, scene, pos_x, pos_y, text=""):
        """
        Initializes the Node object

        :param scene: the scene where the Node will be added
        :param pos_x: the X position of the Node in the scene
        :param pos_y: the Y position of the Node in the scene
        :param text: the text for the node (default: "")
        """

        # run QGraphicsEllipseItem init to draw circle
        super().__init__(-NODE_RADIUS, -NODE_RADIUS, 2 * NODE_RADIUS, 2 * NODE_RADIUS)

        # stores any edges
        self.edges = []

        # set the color, position
        self.setBrush(Qt.white)
        self.setPen(QPen(Qt.black, 2.5))
        self.setPos(pos_x, pos_y)
        self.setZValue(1)

        # add self to the items
        scene.addItem(self)

        self.node_text = text

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None):
        """
        Overrides the built in paint(...) function
        """
        super().paint(QPainter, QStyleOptionGraphicsItem, widget)

        # draw the text for the circle
        QPainter.drawText(self.rect(), Qt.AlignCenter | Qt.TextSingleLine, self.text())

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

    def set_highlight(self, enabled: bool):
        """
        Changes if the Node circle is highlighted

        :param enabled: True, if the node is highlighted
        """

        # set the background color if highlighted
        if enabled:
            self.setBrush(Qt.lightGray)
        else:
            self.setBrush(Qt.white)


class Edge(QGraphicsLineItem):
    """
    A line that goes in between Node objects
    """

    def __init__(self, source, destination):
        """
        Initializes the Edge object
        :param source: the source of the edge (from)
        :param destination: the destination of the edge (to)
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
        self.setPen(QPen(Qt.blue, 2.5))

        # apply changes
        self.adjust()

    def adjust(self):
        """
        Updates the edge's line and geometry
        """

        # draw the line
        self.prepareGeometryChange()
        self.setLine(QLineF(self.destination.pos(), self.source.pos()))
