import bpy
from . import ProkitekturaContainerNode


class ProkitekturaBasement(ProkitekturaContainerNode, bpy.types.Node):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaBasement"
    # Label for nice name display
    bl_label = "Basement"
    # Icon identifier
    bl_icon = 'SOUND'

    # list for iteration over advanced properties
    def declareCheckedSockets(self, socketList):
        super().declareCheckedSockets(socketList)
        socketList.extend((
            {"type":"std", "class":"ProkitekturaCheckedSocketWallCladding", "text":"material",  "pythName":"claddingMaterial"},
            {"type":"std", "class":"ProkitekturaCheckedSocketColor",        "text":"color",     "pythName":"claddingColor"}
        ))

    # Additional buttons displayed on the node.
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
