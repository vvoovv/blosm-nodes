import bpy
from . import ProkitekturaContainerNode


class ProkitekturaBasement(bpy.types.Node, ProkitekturaContainerNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaBasement"
    # Label for nice name display
    bl_label = "Basement"
    # Icon identifier
    bl_icon = 'SOUND'

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):        
        self.draw_buttons_container(context, layout)

    def init(self, context):
        super().init(context)
        self.initCladding()