import bpy
from bpy.types import NodeSocket 

from . import ProkitekturaContainerNode

class ProkitekturaDemoAdvancedAttr(bpy.types.Node, ProkitekturaContainerNode  ): # make ProkitekturaNode the first super() in multiple inheritance
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaDemoAdvancedAttr"
    # Label for nice name display
    bl_label = "Advanced Attr"
    # Icon identifier
    bl_icon = 'SOUND'

    # list for iteration over advanced properties
    def declareProperties(self, propList):
        super().declareProperties(propList)
        propList.extend((
            {"type":"std", "name":"countGroundLevel","check":"activateProp1", "text":"count ground level", "pythName":"groundLevel" },
            {"type":"std", "name":"specificLevel",   "check":"activateProp2", "text":"levels",             "pythName":"levels" },
            {"type":"adv", "name":"prop1",           "check":"activateProp3", "text":"str",                "pythName":"strProp" },
            {"type":"adv", "name":"prop2",           "check":"activateProp4", "text":"check",              "pythName":"boolProp" },
            {"type":"adv", "name":"prop3",           "check":"activateProp5", "text":"int",                "pythName":"intProp" },
            {"type":"adv", "name":"prop4",           "check":"activateProp6", "text":"levels",             "pythName":"enumProp" }
        ))
 
     # list for iteration over advanced properties
    def declareCheckedSockets(self, socketList):
        super().declareProperties(socketList)
        socketList.extend((
            {"type":"std", "class":"ProkitekturaSocketEnum","text":"levels", "pythName":"std" },
            {"type":"adv", "class":"ProkitekturaSocketEnum","text":"levels", "pythName":"adv" }
        ))
       
    optionsList = (
        ("all", "all levels", "All"),
        ("ground", "ground level only", "Ground level only"),
        ("allButLast", "all but last one", "All levels but the last one"),
        ("last", "last level", "The last level"),
        ("specific", "specific level", "Specific level"),
        ("even", "even levels", "Even levels"),
        ("odd", "odd levels", "Odd levels")
    )
    
    propList = []
    socketList = []
    
    # examples of mandatory  attributes 
    countGroundLevel: bpy.props.BoolProperty(name = "Count Ground Level",description = "Shall we count the the ground level for the setting below",default = False)    
    specificLevel: bpy.props.IntProperty(name = "Specific Level",description = "The number of the specific level",subtype = 'UNSIGNED',default = 1,min = 0)

    # examples of advanced properties
    prop1: bpy.props.StringProperty(name = "Property1", description = "Name for property1",default = 'prop1')
    prop2: bpy.props.BoolProperty(name = "Property2", description = "Name for property2",default = False)
    prop3: bpy.props.IntProperty(name = "Property3", description = "Value for property1",default = 1)
    prop4: bpy.props.EnumProperty(name = "Property4", description = "Level for property1",items = optionsList,default = "all")

    # example of activation checks for advanced properties
    activateProp1: bpy.props.BoolProperty(name = "Activate1", description = "activate1", default = True)
    activateProp2: bpy.props.BoolProperty(name = "Activate2", description = "activate2", default = True)
    activateProp3: bpy.props.BoolProperty(name = "Activate3", description = "activate3", default = False)
    activateProp4: bpy.props.BoolProperty(name = "Activate4", description = "activate4", default = False)
    activateProp5: bpy.props.BoolProperty(name = "Activate5", description = "activate5", default = False)
    activateProp6: bpy.props.BoolProperty(name = "Activate6", description = "activate6", default = False)
      
    def init(self, context):
        if not self.propList:
            self.declareProperties(self.propList)
        if not self.socketList:
            self.declareCheckedSockets(self.socketList)

        super().init(context)          
        self.init_sockets_checked(context,self.socketList)   

 
    def draw_buttons(self, context, layout):
        self.draw_buttons_common(context, layout)
        self.draw_buttons_checked(context, layout, self.propList)
        #self.draw_buttons_symmetry(context, layout)
        for text in [ socket["text"] for socket in self.socketList if socket["type"]=="adv"]:
            for inp in [ inp for inp in context.active_node.inputs if inp.name == text]:
                inp.do_hide( not self.showAdvanced )

