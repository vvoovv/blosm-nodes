import bpy

from ..socket import ProkitekturaCheckedSocketBase

# unchecks all checkboxes of checked attrubutes
def _clearAllActivationCheckoxes(self,context):
    for dict in self.propList:
        setattr(self,dict["check"], False)
    for inp in (inp for inp in self.inputs if isinstance(inp,ProkitekturaCheckedSocketBase) ):
        inp.activated = False
        
# checks all checkboxes of checked standard attrubutes
def _defaultAllActivationCheckoxes(self,context):
    for dict in self.propList:
        setattr(self,dict["check"], dict["type"]=="std")
    for text in (socket["text"] for socket in self.socketList if socket["type"]=="std"):
        for inp in (inp for inp in self.inputs if inp.name == text):
            inp.activated = True   
        
# changes state of node between the types "Node", "Definition" or "Use Definition" 
def _definitionTypeUpdate(self, context):
    # new color if pure definition
    if self.typeDefinition == "def":
        self.use_custom_color = True
        self.color = (0.0, 0.8, 1.0)
        _clearAllActivationCheckoxes(self,context)
    elif self.typeDefinition == "usedef":
        self.use_custom_color = True
        self.color = (0.0, 0.4, 0.5)
        _clearAllActivationCheckoxes(self,context)
    else:
        self.use_custom_color = False
        _defaultAllActivationCheckoxes(self,context)
       
    return

# searches for all instances of nodes of type "Definition"
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

# toggles visibility of advanced properties depending of the state of the "Show Advanced" property
def _setAdvanced(self,context):
    for text in (socket["text"] for socket in self.socketList if socket["type"]=="adv"):
        for inp in (inp for inp in self.inputs if inp.name == text):
            inp.hide = not self.showAdvanced   

# shows or hides the symmetryFlip property of the ProkitekturaContainerNode depending on the symmetry property state     
def  _updateSymmetry(self,context):
    flip_index = next((index for (index, d) in enumerate(self.propList) if d["name"] == "symmetryFlip"), None)
    if self.symmetry != "no":
        self.propList[flip_index]["type"] = "std"
    else:
        self.propList[flip_index]["type"] = "hidden"
            


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
    
    showAdvanced: bpy.props.BoolProperty(
        name = "ShowAdvanced", 
        description = "Show advanced properties",
        default = False,
        update = _setAdvanced
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
    def declareProperties(self, propList):
        return

    def declareCheckedSockets(self, socketList):
        return

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
        
        layout.prop(self, "showAdvanced", text="Show Advanced")
    
    def draw_buttons_checked(self, context, layout, propList):
        col = layout.column(align=True)
        hasAdvancedProperties = len([prop for prop in propList if prop["type"]=="adv"])>0
        box = layout.column(align=True).box() if self.showAdvanced and hasAdvancedProperties else None
        for prop in propList:
            if prop["type"]=="std":
                self._drawAttribute(col, prop)
            elif box and prop["type"]=="adv":
                self._drawAttribute(box, prop)
            # else prop["type"]=="hidden"  --> do nothing
    
    def _drawAttribute(self, layout, prop):
        split = layout.row(factor=0.2)
        split.prop(self, prop["check"], text="use")
        column = split.column()
        column.enabled = getattr(self, prop["check"])
        column.prop(self, prop["name"], text=prop["text"])
                
    def init_sockets_checked(self,context,socketList):
        for socket in socketList:
            s = self.inputs.new(socket["class"], socket["text"])
            setattr(s,"python",socket["pythName"])
            if socket["type"]=="adv":
                setattr(s, "hide", True)
                setattr(s, "activated", False)
                setattr(s, "advanced", True)
    
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
    def declareProperties(self, propList):
        super().declareProperties(propList)
        propList.extend((
            {"type":"std", "name":"symmetry",     "check":"activateSym",     "text":"symmetry",         "pythName":"symmetry" },
            {"type":"hidden", "name":"symmetryFlip", "check":"activateSymFlip", "text":"flip for symmetry","pythName":"symmetryFlip" }
        ))
    
    # list for iteration over advanced properties
    def declareCheckedSockets(self, socketList):
        super().declareCheckedSockets(socketList)

    symmetryList = (
        ("no", "no", "no symmetry"),
        ("middleOfLast", "middle of last", "relative to the middle of the last item"),
        ("rightmostOfLast", "rightmost of Last", "relative to the rightmost end of the last item")
    )
    
    symmetry: bpy.props.EnumProperty(
        name = "Symmetry",
        description = "Defines if there is a symmetry of items and the center of the symmetry",
        items = symmetryList,
        default = "no",
        update = _updateSymmetry
    )
    
    symmetryFlip: bpy.props.BoolProperty(
        name = "Flip for Symmetry",
        description = "Flip items on the other side of the center of symmetry to achive the total symmetry or leave the items intact",
        default = False,
        options = {'HIDDEN'}
    )

    activateSym: bpy.props.BoolProperty(name = "activateSym", description = "activateSym", default = True)
    activateSymFlip: bpy.props.BoolProperty(name = "activateSymFlip", description = "activateSymFlip", default = True)


            