import bpy
from . import ProkitekturaContainerNode


class ProkitekturaFacade(ProkitekturaContainerNode, bpy.types.Node):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaFacade"
    # Label for nice name display
    bl_label = "Facade"
    # Icon identifier
    bl_icon = 'SOUND'
    
    # list for iteration over advanced properties
    def declareProperties(self, propList):
        propList.extend((
            {"type":"std", "name":"facadeType","check":"activatefacadeType", "text":"type", "pythName":"facadeType" },
        ))
        super().declareProperties(propList)

    def declareCheckedSockets(self, socketList):
        super().declareCheckedSockets(socketList)
        socketList.extend((
            {"type":"std", "class":"ProkitekturaCheckedSocketWallCladding", "text":"material",  "pythName":"claddingMaterial"},
            {"type":"std", "class":"ProkitekturaCheckedSocketColor",        "text":"color",     "pythName":"claddingColor"}
         ))

    facadeTypeList = (
        ("all", "all", "all"),
        ("front", "front", "front"),
        ("back", "back", "back"),
        ("side", "side", "side"),
        ("north", "north", "north"),
        ("east", "east", "east"),
        ("south", "south", "south"),
        ("west", "west", "west")
    )

    facadeType: bpy.props.EnumProperty(
        name = "Facade Type",
        description = "Facade Type",
        items = facadeTypeList,
        default = "all"
    )

    # activation check for advanced properties
    activatefacadeType: bpy.props.BoolProperty(name = "activatefacadeType", description = "activate facadeType", default = True)

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
