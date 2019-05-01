import bpy
from . import ProkitekturaContainerNode


class ProkitekturaRoofSide(bpy.types.Node, ProkitekturaContainerNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaRoofSide"
    # Label for nice name display
    bl_label = "Roof Side"
    # Icon identifier
    bl_icon = 'SOUND'
    
    roofSideTypeList = (
        ("all", "all", "all"),
        ("front", "front", "front"),
        ("back", "back", "back"),
        ("side", "side", "side"),
        ("north", "north", "north"),
        ("east", "east", "east"),
        ("south", "south", "south"),
        ("west", "west", "west")
    )

    roofSideType: bpy.props.EnumProperty(
        name = "Roof Side Type",
        description = "Roof Side Type",
        items = roofSideTypeList,
        default = "all"
    )

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        layout.prop(self, "roofSideType", text="type")
        self.draw_buttons_container(context, layout)