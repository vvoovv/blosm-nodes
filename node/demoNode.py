import bpy
from bpy.types import NodeSocket 

from . import ProkitekturaNode


class ProkitekturaDemoAdvancedAttr(bpy.types.Node, ProkitekturaNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaDemoAdvancedAttr"
    # Label for nice name display
    bl_label = "Advanced Attr"
    # Icon identifier
    bl_icon = 'SOUND'

    # list for iteration over advanced properties
    propList = (
        {"type":"std", "name":"countGroundLevel","check":"",             "text":"count ground level", "pythName":"groundLevel" },
        {"type":"std", "name":"specificLevel",   "check":"",             "text":"levels",             "pythName":"levels" },
        {"type":"adv", "name":"prop1",           "check":"activateProp1","text":"str",                "pythName":"strProp" },
        {"type":"adv", "name":"prop2",           "check":"activateProp2","text":"check",              "pythName":"boolProp" },
        {"type":"adv", "name":"prop3",           "check":"activateProp3","text":"int",                "pythName":"intProp" },
        {"type":"adv", "name":"prop4",           "check":"activateProp4","text":"levels",             "pythName":"enumProp" }
    )
        
    optionsList = (
        ("all", "all levels", "All"),
        ("ground", "ground level only", "Ground level only"),
        ("allButLast", "all but last one", "All levels but the last one"),
        ("last", "last level", "The last level"),
        ("specific", "specific level", "Specific level"),
        ("even", "even levels", "Even levels"),
        ("odd", "odd levels", "Odd levels")
    )
    
    # examples of mandatory  attributes 
    countGroundLevel: bpy.props.BoolProperty(name = "Count Ground Level",description = "Shall we count the the ground level for the setting below",default = False)    
    specificLevel: bpy.props.IntProperty(name = "Specific Level",description = "The number of the specific level",subtype = 'UNSIGNED',default = 1,min = 0)

    # examples of advanced properties
    prop1: bpy.props.StringProperty(name = "Property1", description = "Name for property1",default = 'prop1')
    prop2: bpy.props.BoolProperty(name = "Property2", description = "Name for property2",default = False)
    prop3: bpy.props.IntProperty(name = "Property3", description = "Value for property1",default = 1)
    prop4: bpy.props.EnumProperty(name = "Property4", description = "Level for property1",items = optionsList,default = "all")

    # example of activation checks for advanced properties
    activateProp1: bpy.props.BoolProperty(name = "Activate1", description = "activate1", default = False)
    activateProp2: bpy.props.BoolProperty(name = "Activate2", description = "activate2", default = False)
    activateProp3: bpy.props.BoolProperty(name = "Activate3", description = "activate3", default = False)
    activateProp4: bpy.props.BoolProperty(name = "Activate4", description = "activate4", default = False)
    
    showAdvanced: bpy.props.BoolProperty(name = "ShowAdvanced", description = "Show advanced properties",default = False)
   
    def draw(self, context, layout):
        super().draw(context,layout)
        
    def init(self, context):
        super().init(context)
        self.inputs.new('NodeSocketIntUnsigned', "std in")        
        self.outputs.new('NodeSocketIntUnsigned', "std out")

    def draw_buttons(self, context, layout):
        self.draw_buttons_common(context, layout)
        
        for prop in [ prop for prop in self.propList if prop["type"]=="std"]:
            layout.prop(self, prop["name"], text=prop["text"])
     
        col = layout.column(align=True)
        col.prop(self, "showAdvanced", text="Show Advanced")
        if self.showAdvanced:
            box = col.box()
            for prop in [ prop for prop in self.propList if prop["type"]=="adv"]:
                row = box.row()
                row.prop(self, prop["check"], text="use")
                row.prop(self, prop["name"], text=prop["text"])
       


