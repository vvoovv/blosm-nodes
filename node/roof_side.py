import bpy
from . import ProkitekturaContainerNode


class ProkitekturaRoofSide(ProkitekturaContainerNode, bpy.types.Node):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaRoofSide"
    # Label for nice name display
    bl_label = "Roof Side"
    # Icon identifier
    bl_icon = 'SOUND'
    
    # list for iteration over advanced properties
    def declareProperties(self, propList):
        super().declareProperties(propList)
        propList.extend((
            {"type":"std", "name":"roofSideType","check":"activateRoofSideType", "text":"type", "pythName":"facadeType" },
        ))

    roofSideTypeList = (
        ("all", "all", "all"),
        ("front", "front", "front"),
        ("back", "back", "back"),
        ("side", "side", "side"),
        ("north", "north", "north"),
        ("east", "east", "east"),
        ("south", "south", "south"),
        ("west", "west", "west")
    )

    roofSideType: bpy.props.EnumProperty(
        name = "Roof Side Type",
        description = "Roof Side Type",
        items = roofSideTypeList,
        default = "all"
    )

    # activation check for advanced properties
    activateRoofSideType: bpy.props.BoolProperty(name = "activateRoofSideType", description = "activateRoofSideType", default = True)

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
