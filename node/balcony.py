import bpy
from . import ProkitekturaNode


class ProkitekturaBalcony(bpy.types.Node, ProkitekturaNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaBalcony"
    # Label for nice name display
    bl_label = "Balcony"
    # Icon identifier
    bl_icon = 'SOUND'
    
    def draw_buttons(self, context, layout):
        self.draw_buttons_common(context, layout)