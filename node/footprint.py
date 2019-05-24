import bpy
from . import ProkitekturaNode

class ProkitekturaFootprint(bpy.types.Node, ProkitekturaNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaFootprint"
    # Label for nice name display
    bl_label = "Footprint"
    # Icon identifier
    bl_icon = 'SOUND'

    # list for iteration over advanced properties
    def declareCheckedSockets(self, socketList):
        super().declareCheckedSockets(socketList)
        socketList.extend((
            {"type":"std", "class":"ProkitekturaCheckedSocketIntUnsigned",  "text":"number of levels",  "pythName":"levels"},
            {"type":"std", "class":"ProkitekturaCheckedSocketIntUnsigned",  "text":"min level",         "pythName":"minLevel"},
            {"type":"std", "class":"ProkitekturaCheckedSocketIntUnsigned",        "text":"height",            "pythName":"levelHeight"},
            {"type":"std", "class":"ProkitekturaCheckedSocketRoofShape",    "text":"roof shape",        "pythName":"roofShape"}
        ))

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

