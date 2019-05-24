import bpy
from . import ProkitekturaNode


class ProkitekturaDormer(bpy.types.Node, ProkitekturaNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaDormer"
    # Label for nice name display
    bl_label = "Dormer"
    # Icon identifier
    bl_icon = 'SOUND'

    propList = []
    socketList = []

    def init(self, context):
        if not self.propList:
            self.declareProperties(self.propList)
        if not self.socketList:
            self.declareCheckedSockets(self.socketList)
        
        self.init_sockets_checked(context,self.socketList)
        super().init(context)
 
    def draw_buttons(self, context, layout):
        self.draw_buttons_common(context, layout)
        self.draw_buttons_checked(context, layout, self.propList)
