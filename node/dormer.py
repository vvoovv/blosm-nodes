import bpy
from . import ProkitekturaNode


class ProkitekturaDormer(bpy.types.Node, ProkitekturaNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaDormer"
    # Label for nice name display
    bl_label = "Dormer"
    # Icon identifier
    bl_icon = 'SOUND'

    def draw_buttons(self, context, layout):
        self.draw_buttons_common(context, layout)