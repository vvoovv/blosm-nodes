import bpy
from . import ProkitekturaNode


class ProkitekturaWindow(bpy.types.Node, ProkitekturaNode):
    
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaWindow"
    # Label for nice name display
    bl_label = "Window"
    # Icon identifier
    bl_icon = 'SOUND'
    
    typeList = (
        ("flat", "flat", "flat window"),
        ("rail", "rail", "rail window")
    )
    
    shapeList = (
        ("rectangle", "rectangle", "rectangle"),
        ("topOblique", "top oblique", "top oblique"),
        ("topRound", "top round", "top round"),
        ("topElliptic", "top elliptic", "top elliptic"),
        ("fullCircle", "full circle", "full circle")
    )
    
    type: bpy.props.EnumProperty(
        name = "Window Type",
        description = "Window type (e.g flat, rail)",
        items = typeList,
        default = "flat"
    )
    
    width: bpy.props.FloatProperty(
        name = "Width",
        description = "Window width in meters",
        min = 0.1,
        default = 1.1
    )

    height: bpy.props.FloatProperty(
        name = "Height",
        description = "Window height in meters",
        min = 0.1,
        default = 1.2
    )
    
    panelsRow1: bpy.props.IntProperty(
        name = "Panel in row 1",
        description = "The number of panels in the row 1",
        min = 1,
        default = 2
    )
    
    shape: bpy.props.EnumProperty(
        name = "Window Shape",
        description = "Window shape (e.g rectangle, top oblique, full circle, etc)",
        items = shapeList,
        default = "rectangle"
    )
    
    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        self.draw_buttons_common(context, layout)
        
        layout.prop(self, "type", text="type")
        layout.prop(self, "width", text="width")
        layout.prop(self, "height", text="height")
        layout.prop(self, "shape", text="shape")

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "%s %s %.2fx%.2f" % (self.bl_label, self.panelsRow1, self.width, self.height)