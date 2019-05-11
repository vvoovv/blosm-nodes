import bpy

def _definitionTypeUpdate(self, context):
    # new color if pure definition
    if self.typeDefinition == "def":
        self.use_custom_color = True
        self.color = (0.0, 0.8, 1.0)
    elif self.typeDefinition == "usedef":
        self.use_custom_color = True
        self.color = (0.0, 0.4, 0.5)
    else:
        self.use_custom_color = False
       
    return

def _searchDefinitionItems(self,context):
    if self.typeDefinition == "usedef":
        tree = context.space_data.edit_tree
        defNodesList = [
            (node.defName, node.defName, node.defName) for node in tree.nodes
            if node.bl_idname == self.bl_idname and node.typeDefinition == "def"
        ]
    else:
        defNodesList = []
    return defNodesList


# Derived from the Node base type.
class ProkitekturaNode:
    # === Basics ===
    # Description string
    """
    Mix-in class for Prokitektura nodes
    """
    
    definitionTypeList = (
        ("none", "Node", "Standard Node"),
        ("def", "Definition", "Set Definition"),
        ("usedef", "Use Definition", "Use Definition")
    )

    typeDefinition: bpy.props.EnumProperty(
        name = "DefinitionType",
        description = "Definition Type",
        items = definitionTypeList,
        default = "none",
        update = _definitionTypeUpdate
    )
    
    useDefinition: bpy.props.EnumProperty(
        name = "UseDefinition",
        description = "Use Definition",
        items = _searchDefinitionItems,
    )

    defName: bpy.props.StringProperty(
        name = "Style definition",
        description = "Name for style definition",
        default = ''
    )
    """
    A poll function to enable instantiation.
    """
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == "ProkitekturaNodeTree"

    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties
    #my_string_prop: bpy.props.StringProperty()
    #my_float_prop: bpy.props.FloatProperty(default=3.1415926)

    # === Optional Functions ===
    # Initialization function, called when a new node is created.
    # This is the most common place to create the sockets for a node, as shown below.
    # NOTE: this is not the same as the standard __init__ function in Python, which is
    #       a purely internal Python method and unknown to the node system!
    def init(self, context):
        self.inputs.new('ProkitekturaSocketCondition', "condition")
        
#        defSocket = self.outputs.new('ProkitekturaSocketDef', "defines")
#        defSocket.hide = True
        self.outputs.new('ProkitekturaSocketMarkup', "markup")
    
    def draw_buttons_common(self, context, layout):
        layout.prop(self, "typeDefinition", text="type")
        if self.typeDefinition == "usedef":
            layout.prop(self, "useDefinition", text="use")
        if self.typeDefinition == "def":
            layout.prop(self, "defName", text="def")
    
    def initCladding(self):
        self.inputs.new('ProkitekturaSocketWallCladding', "material")
        self.inputs.new('NodeSocketColor', "color")
    
    def inputWidth(self):
        self.inputs.new('NodeSocketFloatUnsigned', "width")

    def outputWidth(self):
        self.outputs.new('NodeSocketFloatUnsigned', "width")
        

class ProkitekturaContainerNode(ProkitekturaNode):
    """
    Mix-in class for container nodes (Div, Layer, Basement, RoofSide, Ridge)
    """
    
    symmetryList = (
        ("no", "no", "no symmetry"),
        ("middleOfLast", "middle of last", "relative to the middle of the last item"),
        ("rightmostOfLast", "rightmost of Last", "relative to the rightmost end of the last item")
    )
    
    symmetry: bpy.props.EnumProperty(
        name = "Symmetry",
        description = "Defines if there is a symmetry of items and the center of the symmetry",
        items = symmetryList,
        default = "no"
    )
    
    symmetryFlip: bpy.props.BoolProperty(
        name = "Flip for Symmetry",
        description = "Flip items on the other side of the center of symmetry to achive the total symmetry or leave the items intact",
        default = False
    )
    
    #def insert_link(self, link):
    #    nodeTree = bpy.context.space_data.edit_tree
    #    nodeFrame = nodeTree.nodes.new('NodeFrame')
    #    nodeFrame.location = link.to_node.location.copy()
    #    nodeFrame.select = False
    #    link.from_node.select = False
    #    link.to_node.select = True
    #    bpy.ops.node.translate_attach(TRANSFORM_OT_translate={"value":(30., -30., 0), "release_confirm":True})
        #bpy.ops.node.translate_attach(TRANSFORM_OT_translate={"value":(30., -30., 0), "constraint_axis":(False, False, False), "constraint_matrix":(1, 0, 0, 0, 1, 0, 0, 0, 1), "constraint_orientation":'GLOBAL', "mirror":True, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":True, "use_accurate":False}, NODE_OT_attach={}, NODE_OT_insert_offset={})
    
    def draw_buttons_container(self, context, layout):
        self.draw_buttons_common(context, layout)
        self.draw_buttons_symmetry(context, layout)
    
    def draw_buttons_symmetry(self, context, layout):
        layout.prop(self, "symmetry", text="symmetry")
        if self.symmetry != "no":
            layout.prop(self, "symmetryFlip", text="flip for symmetry")