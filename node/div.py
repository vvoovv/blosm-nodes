import bpy
from . import ProkitekturaNode


class ProkitekturaDiv(ProkitekturaNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaDiv"
    # Label for nice name display
    bl_label = "Div (Division)"
    # Icon identifier
    bl_icon = 'SOUND'
    
    arrangementList = (
        ("h", "horizontal", "horizontal arrangement"),
        ("v", "vertical", "vertical arrangement")
    )
    
    arrangement: bpy.props.EnumProperty(
        name = "Arrangement",
        description = "Arrange items inside the div horizontally or vertically",
        items = arrangementList,
        default = "h"
    )
    
    def init(self, context):
        self.inputs.new('ProkitekturaSocketWallCladding', "material")
        self.inputs.new('NodeSocketColor', "color")
        super().init(context)