import bpy
from bpy.types import Node


# Mix-in class for all custom nodes in this tree type.
# Defines a poll function to enable instantiation.
class ProkitekturaTreeNode:
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == "ProkitekturaNodeTree"


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

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")