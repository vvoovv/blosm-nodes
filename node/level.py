import bpy
from . import ProkitekturaNode


class ProkitekturaLevel(ProkitekturaNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaLevel"
    # Label for nice name display
    bl_label = "Level"
    # Icon identifier
    bl_icon = 'SOUND'
    
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
        default = "all"
    )
    
    def init(self, context):
        self.inputs.new('ProkitekturaSocketWallCladding', "material")
        self.inputs.new('NodeSocketColor', "color")
        super().init(context)

    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        if not self.levelOptions in ('ground', 'specific', 'last'):
            layout.prop(self, "countGroundLevel", text="count ground level")
        layout.prop(self, "levelOptions", text="levels")
        if self.levelOptions == 'specific':
            layout.prop(self, "specificLevel", text="level number")