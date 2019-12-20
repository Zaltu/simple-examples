import os

from NodeGraphQt import (NodeGraph,
                         BaseNode,
                         BackdropNode,
                         setup_context_menu)
from NodeGraphQt import QtWidgets, QtCore, PropertiesBinWidget, NodeTreeWidget

from frames import InfoNode, SpeakNode, CameraNode, MoveNode

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    # Base node graph widget
    graph = NodeGraph()

    # set up default menu and commands.
    setup_context_menu(graph)

    # widget used for the node graph.
    graph_widget = graph.widget
    graph_widget.resize(1100, 800)
    graph_widget.show()


    # show the properties bin when a node is "double clicked" in the graph.
    properties_bin = PropertiesBinWidget(node_graph=graph)
    properties_bin.setWindowFlags(QtCore.Qt.Tool)
    def show_prop_bin(node):
        if not properties_bin.isVisible():
            properties_bin.show()
    graph.node_double_clicked.connect(show_prop_bin)


    # registered nodes.
    reg_nodes = [
        InfoNode,
        SpeakNode,
        CameraNode,
        MoveNode
    ]
    for n in reg_nodes:
        graph.register_node(n)

    info_node = graph.create_node(
        'personax.InfoNode',
        name='Default=info, changed to desc',
        pos=[0, 0]
    )
    speak_node = graph.create_node(
        'personax.SpeakNode',
        name='Default=speak, changed to desc',
        pos=[0, 0]
    )
    camera_node = graph.create_node(
        'personax.CameraNode',
        name='Default=camera, changed to desc',
        pos=[0, 0]
    )
    move_node = graph.create_node(
        'personax.MoveNode',
        name='Default=move, changed to desc',
        pos=[0, 0]
    )


    app.exec_()
