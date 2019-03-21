import bpy
from bpy.types import NodeSocket

from . import ProkitekturaNode


# Custom socket type
class ProkitekturaSocketRoofShape(NodeSocket):
    # Description string
    """
    A custom node socket type for the roof shapes
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaSocketRoofShape"
    # Label for nice name display
    bl_label = "Roof Shape"

    # Enum items list
    roofShapeList = (
        ("flat", "flat", "flat"),
        ("gabled", "gabled", "gabled"),
        ("hipped", "hipped", "hipped"),
        ("pyramidal", "pyramidal", "pyramidal"),
        ("skillion", "skillion", "skillion"),
        ("dome", "dome", "dome"),
        ("onion", "onion", "onion"),
        ("round", "round", "round"),
        ("half-hipped", "half-hipped", "half-hipped"),
        ("gambrel", "gambrel", "gambrel"),
        ("saltbox", "saltbox", "saltbox"),
        ("mansard", "mansard", "mansard")
    )

    roofShape: bpy.props.EnumProperty(
        name = "Roof Shape",
        description = "Roof Shape",
        items = roofShapeList,
        default = "flat"
    )

    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "roofShape", text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


# Custom socket type
class ProkitekturaSocketFacades(NodeSocket):
    # Description string
    """
    A custom node socket type for facades generated through the extrusion of a footprint
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaSocketFacades"
    # Label for nice name display
    bl_label = "Facades"

    facades: bpy.props.IntProperty(
        name = "facades",
        description = "Facades generated through the extrusion of a footprint",
        default = 1
    )
    
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.8, 0.33, 0.33)


# Custom socket type
class ProkitekturaSocketRoofSides(NodeSocket):
    # Description string
    """
    A custom node socket type for roof sides generated through the extrusion of the footprint
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaSocketRoofSides"
    # Label for nice name display
    bl_label = "Roof Sides"

    roofSides: bpy.props.IntProperty(
        name = "roof sides",
        description = "Roof sides generated through the extrusion of a footprint",
        default = 1
    )
    
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.8, 0.33, 0.33)


class ProkitekturaFootprint(ProkitekturaNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaFootprint"
    # Label for nice name display
    bl_label = "Footprint"
    # Icon identifier
    bl_icon = 'SOUND'

    def init(self, context):
        super().init(context)
        self.inputs.new('NodeSocketIntUnsigned', "number of levels")
        self.inputs.new('NodeSocketIntUnsigned', "min level")
        self.inputs.new('NodeSocketFloatUnsigned', "level height")
        self.inputs.new('ProkitekturaSocketRoofShape', "roof shape")
        
        self.outputs.new('ProkitekturaSocketFacades', "facades")
        self.outputs.new('ProkitekturaSocketRoofSides', "roof sides")