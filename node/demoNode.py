import bpy
from bpy.types import NodeSocket, NodeSocketIntUnsigned 

from . import ProkitekturaContainerNode

class ProkitekturaSocketEnum(NodeSocket):
    # Description string
    '''Custom node socket type'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'ProkitekturaSocketEnum'
    # Label for nice name display
    bl_label = "Custom Node Socket"

    # Enum items list
    my_items = (
        ('DOWN', "Down", "Where your feet are"),
        ('UP', "Up", "Where your head should be"),
        ('LEFT', "Left", "Not right"),
        ('RIGHT', "Right", "Not left"),
    )

    my_enum_prop: bpy.props.EnumProperty(
        name="Direction",
        description="Just an example",
        items=my_items,
        default='UP',
    )

    activated: bpy.props.BoolProperty(name = "Activated", description = "activated", default = True)

    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        if self.is_linked:
            layout.label(text=text)
        elif self.is_output:
            col = layout.column(align=True)
            row = col.row(align=True)
            row.prop(self, "activated", text="use")
            column = row.column(align=True)
            column.enabled = getattr(self, "activated")
            column.prop(self, "my_enum_prop", text=text)
        else:
            col = layout.column(align=True)
            row = col.row(align=True)
            row.prop(self, "my_enum_prop", text=text)
            column = row.column(align=True)
            column.prop(self, "activated", text="use")
            row.enabled = getattr(self, "activated")
 
    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


class ProkitekturaDemoAdvancedAttr(bpy.types.Node, ProkitekturaContainerNode  ): # make ProkitekturaNode the first super() in multiple inheritance
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaDemoAdvancedAttr"
    # Label for nice name display
    bl_label = "Advanced Attr"
    # Icon identifier
    bl_icon = 'SOUND'

    # list for iteration over advanced properties
    def declareProperties(self):
        propList = (
            {"type":"std", "name":"countGroundLevel","check":"activateProp1", "text":"count ground level", "pythName":"groundLevel" },
            {"type":"std", "name":"specificLevel",   "check":"activateProp2", "text":"levels",             "pythName":"levels" },
            {"type":"adv", "name":"prop1",           "check":"activateProp3", "text":"str",                "pythName":"strProp" },
            {"type":"adv", "name":"prop2",           "check":"activateProp4", "text":"check",              "pythName":"boolProp" },
            {"type":"adv", "name":"prop3",           "check":"activateProp5", "text":"int",                "pythName":"intProp" },
            {"type":"adv", "name":"prop4",           "check":"activateProp6", "text":"levels",             "pythName":"enumProp" }
        )
        return super().declareProperties() + propList
        
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
    activateProp1: bpy.props.BoolProperty(name = "Activate1", description = "activate1", default = True)
    activateProp2: bpy.props.BoolProperty(name = "Activate2", description = "activate2", default = True)
    activateProp3: bpy.props.BoolProperty(name = "Activate3", description = "activate3", default = False)
    activateProp4: bpy.props.BoolProperty(name = "Activate4", description = "activate4", default = False)
    activateProp5: bpy.props.BoolProperty(name = "Activate5", description = "activate5", default = False)
    activateProp6: bpy.props.BoolProperty(name = "Activate6", description = "activate6", default = False)
   
    showAdvanced: bpy.props.BoolProperty(name = "ShowAdvanced", description = "Show advanced properties",default = False)
   
    def draw(self, context, layout):
        super().draw(context,layout)
        
    def init(self, context):
        super().init(context)
        self.inputs.new('ProkitekturaSocketEnum', "in")        
        self.outputs.new('ProkitekturaSocketEnum', "out")        

    def draw_buttons(self, context, layout):
        innodes = [innode for innode in self.outputs if innode.is_output]
        for node in innodes:
            pass
#            inp = getattr(self,"inputs")
        self.draw_buttons_common(context, layout)
        propList = self.declareProperties()
        self.draw_buttons_checked(context,layout,propList)
        self.draw_buttons_symmetry(context, layout)

