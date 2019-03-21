import bpy
from bpy.types import NodeSocket

from . import ProkitekturaNode


# Custom socket type
class ProkitekturaSocketFootprint(NodeSocket):
    # Description string
    """
    A custom node input socket type for a link with the footprint
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaSocketFootprint"
    # Label for nice name display
    bl_label = "Footprint"

    footprint: bpy.props.IntProperty(
        name = "Footprint",
        description = "for a link with the related footprint",
        default = 1
    )
    
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.8, 0.33, 0.33)


# Custom socket type
class ProkitekturaSocketLevelsDivs(NodeSocket):
    # Description string
    """
    A custom node socket type for levels and divs (i.e. divisions) on the facade
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaSocketLevelsDivs"
    # Label for nice name display
    bl_label = "Levels and Divs"

    levelsDivs: bpy.props.IntProperty(
        name = "facades",
        description = "Levels and divs (divisions) on a facade",
        default = 1
    )
    
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.8, 0.33, 0.33)


class ProkitekturaFacade(ProkitekturaNode):
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
        self.inputs.new('ProkitekturaSocketWallCladding', "material")
        self.inputs.new('NodeSocketColor', "color")
        super().init(context)
        self.inputs.new('ProkitekturaSocketFootprint', "footprint")
        
        self.outputs.new('ProkitekturaSocketLevelsDivs', "levels and divs")

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        layout.prop(self, "facadeType", text="type")