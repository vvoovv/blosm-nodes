import bpy
from . import ProkitekturaNode


class ProkitekturaWindow(bpy.types.Node, ProkitekturaNode):
    
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaWindow"
    # Label for nice name display
    bl_label = "Window"
    # Icon identifier
    bl_icon = 'SOUND'
    
    # list for iteration over advanced properties
    def declareProperties(self, propList):
        super().declareProperties(propList)
        propList.extend((
            {"type":"std",    "name":"type",       "check":"activateProp1", "text":"type",       "pythName":"type" },
            {"type":"std",    "name":"shape",      "check":"activateProp5", "text":"shape",      "pythName":"shape" },
            {"type":"std",    "name":"width",      "check":"activateProp2", "text":"width",      "pythName":"width" },
            {"type":"std",    "name":"height",     "check":"activateProp3", "text":"height",     "pythName":"height" },
            {"type":"hidden", "name":"panelsRow1", "check":"activateProp4", "text":"panelsRow1", "pythName":"panels" }
        ))
 
    typeList = (
        ("flat", "flat", "flat window"),
        ("rail", "rail", "rail window")
    )
    
    shapeList = (
        ("rectangle", "rectangle", "rectangle"),
        ("topOblique", "top oblique", "top oblique"),
        ("topRound", "top round", "top round"),
        ("topElliptic", "top elliptic", "top elliptic"),
        ("fullCircle", "full circle", "full circle")
    )
    
    type: bpy.props.EnumProperty(
        name = "Window Type",
        description = "Window type (e.g flat, rail)",
        items = typeList,
        default = "flat"
    )
    
    width: bpy.props.FloatProperty(
        name = "Width",
        description = "Window width in meters",
        min = 0.1,
        default = 1.1
    )

    height: bpy.props.FloatProperty(
        name = "Height",
        description = "Window height in meters",
        min = 0.1,
        default = 1.2
    )
    
    panelsRow1: bpy.props.IntProperty(
        name = "Panel in row 1",
        description = "The number of panels in the row 1",
        min = 1,
        default = 2
    )
    
    shape: bpy.props.EnumProperty(
        name = "Window Shape",
        description = "Window shape (e.g rectangle, top oblique, full circle, etc)",
        items = shapeList,
        default = "rectangle"
    )

    # activation checks for properties
    activateProp1: bpy.props.BoolProperty(name = "Activate1", description = "activate1", default = True)
    activateProp2: bpy.props.BoolProperty(name = "Activate2", description = "activate2", default = True)
    activateProp3: bpy.props.BoolProperty(name = "Activate3", description = "activate3", default = True)
    activateProp4: bpy.props.BoolProperty(name = "Activate4", description = "activate4", default = True)
    activateProp5: bpy.props.BoolProperty(name = "Activate5", description = "activate5", default = True)
    
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

    # Optional: custom label
    # Explicit user label overrides this, but here we can define a label dynamically
    def draw_label(self):
        return "%s %s %.2fx%.2f" % (self.bl_label, self.panelsRow1, self.width, self.height)