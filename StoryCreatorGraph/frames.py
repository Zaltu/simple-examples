"""
Nodes corresponding to the View Frames of the old implementation in story-creator
"""
from NodeGraphQt import BaseNode


class PersonaXNode(BaseNode):
    """
    Sets identifier.
    Hyper-OO ahoy!
    """
    # Node identifier
    __identifier__ = "personax"


class InfoNode(PersonaXNode):
    """
    Node implementation of InfoFrame
    """
    # Default node name
    NODE_NAME = "InfoNode"

    def __init__(self):
        super().__init__()

        # InfoFrame has only one text property.
        self.add_text_input("info_text", "Informative Text")

        ## Add IO
        # Any number of previous nodes can connect.
        self.add_input("Previous", multi_input=True)
        # Can only connect to a single output.
        self.add_output("Next", multi_output=False)

class SpeakNode(PersonaXNode):
    """
    Node implementation of SpeakFrame
    """
    # Default node name
    NODE_NAME = "SpeakNode"

    def __init__(self):
        super().__init__()

        ## SpeakFrame properties
        self.add_text_input("text", "Text")
        self.add_combo_menu("chars", "Speaker", items=["Elizabeth", "MC", "Sister"])
        self.add_combo_menu("arcanas_point", "Arcana", items=["Fool", "Magician", "Aeon"])
        self.add_text_input("points", "Points")
        self.add_combo_menu("arcanas_angle", "Arcana", items=["Fool", "Magician", "Aeon"])
        self.add_text_input("angle", "Angle")
        self.add_combo_menu("emotions", "Emotion", items=["Neutral", "Happy", "Sad"])
        # Handling of more points/angle/arcana through buttons and tabs TODO
        # Importing all these lists TODO

        ## Add IO
        # Any number of previous nodes can connect.
        self.add_input("Previous", multi_input=True)
        # Connects to all choices
        self.add_output("Next", multi_output=True)


class CameraNode(PersonaXNode):
    """
    Node implementation of CameraFrame
    """
    # Default node name
    NODE_NAME = "CameraNode"

    def __init__(self):
        super().__init__()

        ## CameraFrame properties
        self.add_text_input("cx", "Camera's Position x")
        self.add_text_input("cy", "Camera's Position y")
        self.add_text_input("cz", "Camera's Position z")
        self.add_text_input("lx", "Look at x")
        self.add_text_input("ly", "Look at y")
        self.add_text_input("lz", "Look at z")

        ## Add IO
        # Any number of previous nodes can connect.
        self.add_input("Previous", multi_input=True)
        # Can only connect to a single output.
        self.add_output("Next", multi_output=False)


class MoveNode(PersonaXNode):
    """
    Node implementation of MoveFrame
    """
    # Default node name
    NODE_NAME = "MoveNode"

    def __init__(self):
        super().__init__()

        ## MoveFrame properties
        self.add_text_input("lx", "Go to x")
        self.add_text_input("ly", "Go to y")
        self.add_combo_menu("person", "Person", items=["Elizabeth", "MC", "Sister"])
        self.add_combo_menu("anim", "Animation", items=["Run", "Walk", "Surprise", "Idle"])

        ## Add IO
        # Any number of previous nodes can connect.
        self.add_input("Previous", multi_input=True)
        # Can only connect to a single output.
        self.add_output("Next", multi_output=False)
