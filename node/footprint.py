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
    
    countGroundLevel: bpy.props.BoolProperty(
        name = "Count Ground Level",
        description = "Shall we count the the ground level for the setting below",
        default = False
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