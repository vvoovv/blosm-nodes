import bpy
from . import ProkitekturaNode, ProkitekturaContainerNode


class ProkitekturaDiv(ProkitekturaNode, ProkitekturaContainerNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaDiv"
    # Label for nice name display
    bl_label = "Div"
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
        self.inputWidth()
        super().init(context)
        self.outputWidth()

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):        
        self.draw_buttons_symmetry(context, layout)