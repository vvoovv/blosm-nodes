import bpy
from . import ProkitekturaContainerNode


class ProkitekturaDiv(ProkitekturaContainerNode,bpy.types.Node):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaDiv"
    # Label for nice name display
    bl_label = "Div"
    # Icon identifier
    bl_icon = 'SOUND'

    # list for iteration over advanced properties
    def declareProperties(self, propList):
        super().declareProperties(propList)
        propList.extend((
            {"type":"std", "name":"arrangement","check":"activateArrangement", "text":"arrangement", "pythName":"arrangement" },
        ))

    # list for iteration over advanced properties
    def declareCheckedSockets(self, socketList):
        super().declareCheckedSockets(socketList)
        socketList.extend((
            {"type":"std", "class":"ProkitekturaCheckedSocketWallCladding", "text":"material",  "pythName":"claddingMaterial"},
            {"type":"std", "class":"ProkitekturaCheckedSocketColor",        "text":"color",     "pythName":"claddingColor"},
            {"type":"std", "class":"ProkitekturaCheckedSocketFloatUnsigned","text":"width",     "pythName":"width"}
        ))
    
    arrangementList = (
        ("h", "horizontal", "horizontal arrangement"),
        ("v", "vertical", "vertical arrangement")
    )
    
    arrangement: bpy.props.EnumProperty(
        name = "Arrangement",
        description = "Arrange items inside the div horizontally or vertically",
        items = arrangementList,
        default = "h"
    )

    # activation check for advanced properties
    activateArrangement: bpy.props.BoolProperty(name = "activateArrangement", description = "activateArrangement", default = True)
 
    propList = []
    socketList = []
   
    def init(self, context):
        if not self.propList:
            self.declareProperties(self.propList)
        if not self.socketList:
            self.declareCheckedSockets(self.socketList)
        
        self.init_sockets_checked(context,self.socketList)        
        super().init(context)
        self.outputs.new('NodeSocketFloatUnsigned', "width")

    def draw_buttons(self, context, layout):
        self.draw_buttons_common(context, layout)
        self.draw_buttons_checked(context, layout, self.propList)
