import bpy
from . import ProkitekturaContainerNode


class ProkitekturaRidge(bpy.types.Node, ProkitekturaContainerNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaRidge"
    # Label for nice name display
    bl_label = "Ridge"
    # Icon identifier
    bl_icon = 'SOUND'
    
    def draw_buttons(self, context, layout):
        self.draw_buttons_container(context, layout)