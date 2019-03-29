import bpy
from bpy.types import Node


class ProkitekturaTreeNode:
    """
    Mix-in class for all custom nodes in this tree type.
    Defines a poll function to enable instantiation.
    """
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == "ProkitekturaNodeTree"


class ProkitekturaContainerNode:
    """
    Mix-in class for container nodes (Div, Layer, Basement, RoofSide, Ridge)
    """
    symmetryList = (
        ("no", "no", "no symmetry"),
        ("middleOfLast", "middle of last", "relative to the middle of the last item"),
        ("rightmostOfLast", "rightmost of Last", "relative to the rightmost end of the last item")
    )
    
    symmetry: bpy.props.EnumProperty(
        name = "Symmetry",
        description = "Defines if there is a symmetry of items and the center of the symmetry",
        items = symmetryList,
        default = "no"
    )
    
    symmetryFlip: bpy.props.BoolProperty(
        name = "Flip for Symmetry",
        description = "Flip items on the other side of the center of symmetry to achive the total symmetry or leave the items intact",
        default = False
    )
    
    def draw_buttons_symmetry(self, context, layout):
        layout.prop(self, "symmetry", text="symmetry")
        if self.symmetry != "no":
            layout.prop(self, "symmetryFlip", text="flip for symmetry")


# Derived from the Node base type.
class ProkitekturaNode(Node, ProkitekturaTreeNode):
    # === Basics ===
    # Description string
    """
    Mix-in class for Prokitektura nodes
    """

    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties
    #my_string_prop: bpy.props.StringProperty()
    #my_float_prop: bpy.props.FloatProperty(default=3.1415926)

    # === Optional Functions ===
    # Initialization function, called when a new node is created.
    # This is the most common place to create the sockets for a node, as shown below.
    # NOTE: this is not the same as the standard __init__ function in Python, which is
    #       a purely internal Python method and unknown to the node system!
    def init(self, context):
        self.inputs.new('ProkitekturaSocketCondition', "condition")
        self.inputs.new('ProkitekturaSocketMarkupItem', "markup or previous")
        self.inputs.new('ProkitekturaSocketDefs', "defs")
        
        self.outputs.new('ProkitekturaSocketMarkup', "markup")
        self.outputs.new('ProkitekturaSocketMarkupItem', "next")
        self.outputs.new('ProkitekturaSocketDefs', "defs")
    
    def inputWidth(self):
        self.inputs.new('NodeSocketFloatUnsigned', "width")

    def outputWidth(self):
        self.outputs.new('NodeSocketFloatUnsigned', "width")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")