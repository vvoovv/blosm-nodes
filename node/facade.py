import bpy
from . import ProkitekturaContainerNode


class ProkitekturaFacade(bpy.types.Node, ProkitekturaContainerNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaFacade"
    # Label for nice name display
    bl_label = "Facade"
    # Icon identifier
    bl_icon = 'SOUND'
    
    facadeTypeList = (
        ("all", "all", "all"),
        ("front", "front", "front"),
        ("back", "back", "back"),
        ("side", "side", "side"),
        ("north", "north", "north"),
        ("east", "east", "east"),
        ("south", "south", "south"),
        ("west", "west", "west")
    )

    facadeType: bpy.props.EnumProperty(
        name = "Facade Type",
        description = "Facade Type",
        items = facadeTypeList,
        default = "all"
    )

    def init(self, context):
        super().init(context)
        self.initCladding()

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        self.draw_buttons_common(context, layout)
        layout.prop(self, "facadeType", text="type")
        self.draw_buttons_symmetry(context, layout)