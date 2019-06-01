import bpy
from . import ProkitekturaContainerNode

def _updateForOptions(self,context):
    count_index = next((index for (index, d) in enumerate(self.propList) if d["name"] == "countGroundLevel"), None)
    if self.levelOptions in ('ground', 'specific', 'last'):
        self.propList[count_index]["type"] = "hidden"
    else:
        self.propList[count_index]["type"] = "std"

    specific_index = next((index for (index, d) in enumerate(self.propList) if d["name"] == "specificLevel"), None)
    if self.levelOptions == 'specific':
        self.propList[specific_index]["type"] = "std"
    else:
        self.propList[specific_index]["type"] = "hidden"
        
    
class ProkitekturaLevel(bpy.types.Node, ProkitekturaContainerNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaLevel"
    # Label for nice name display
    bl_label = "Level"
    # Icon identifier
    bl_icon = 'SOUND'
    
    # list for iteration over advanced properties
    def declareProperties(self, propList):
        propList.extend((
            {"type":"std",    "name":"levelOptions",    "check":"activateProp2", "text":"levels",             "pythName":"strProp" },
            {"type":"std",    "name":"countGroundLevel","check":"activateProp1", "text":"count ground level", "pythName":"groundLevel" },
            {"type":"hidden", "name":"specificLevel",   "check":"activateProp3", "text":"level number",       "pythName":"index" }
        ))
        super().declareProperties(propList)

    def declareCheckedSockets(self, socketList):
        super().declareCheckedSockets(socketList)
        socketList.extend((
            {"type":"std", "class":"ProkitekturaCheckedSocketWallCladding", "text":"material",  "pythName":"claddingMaterial"},
            {"type":"std", "class":"ProkitekturaCheckedSocketColor",        "text":"color",     "pythName":"claddingColor"}
         ))

    # Enum items list
    levelOptionsList = (
        ("all", "all levels", "All"),
        ("ground", "ground level only", "Ground level only"),
        ("allButLast", "all but last one", "All levels but the last one"),
        ("last", "last level", "The last level"),
        ("specific", "specific level", "Specific level"),
        ("even", "even levels", "Even levels"),
        ("odd", "odd levels", "Odd levels")
    )
    
    countGroundLevel: bpy.props.BoolProperty(
        name = "Count Ground Level",
        description = "Shall we count the the ground level for the setting below",
        default = False
    )
    
    specificLevel: bpy.props.IntProperty(
        name = "Specific Level",
        description = "The number of the specific level",
        subtype = 'UNSIGNED',
        default = 1,
        min = 0
    )
    
    levelOptions: bpy.props.EnumProperty(
        name = "Options for level numbers",
        description = "Options for level numbers. The option above \"Count Ground Level\" is taken into account",
        items = levelOptionsList,
        default = "all",
        update = _updateForOptions
    )
    
    # example of activation checks for advanced properties
    activateProp1: bpy.props.BoolProperty(name = "Activate1", description = "activate1", default = True)
    activateProp2: bpy.props.BoolProperty(name = "Activate2", description = "activate2", default = True)
    activateProp3: bpy.props.BoolProperty(name = "Activate3", description = "activate3", default = True)

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
