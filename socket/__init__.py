import bpy
from bpy.types import NodeSocket


class ProkitekturaSocketMarkup(NodeSocket):
    """
    Output socket connected to a Frame with markup nodes
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaSocketMarkup"
    # Label for nice name display
    bl_label = "Markup"
    
    markup: bpy.props.BoolProperty(
        name = "markup",
        description = "An output socket connected to a Frame with markup nodes",
        default = True
    )

    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


class ProkitekturaSocketCondition(NodeSocket):
    """
    Node socket type for the condition for an element style
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaSocketCondition"
    # Label for nice name display
    bl_label = "Condition"
    
    hideForDef = True

    definitions: bpy.props.BoolProperty(
        name = "condition",
        description = "Condition for an element style",
        default = True
    )
    
    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


    


class ProkitekturaCheckedSocketBase(NodeSocket):
    '''
    ProkitekturaBaseCheckedSocket is the base class for checked sockets. I requires to be customized by a
    subclass. Every subclass needs to define the properties 'activated' and 'python', whereas the former defines the
    checkbox and the later the variable name used in the python structure created by the parser. This can easily be 
    done using multiple inheritance with the min-in class ProkitekturaCheckedSocketMixIn below.
 
    For example (notice the order of the parent classes!):
        class ProkitekturaCheckedSocketCustom(ProkitekturaCheckedSocketMixIn, ProkitekturaCheckedSocketBase):

    The property of the customized socket requires to get the attribute name 'value', to be easily accessible
    by the parser.
    '''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'ProkitekturaCheckedSocketBase'
    # Label for nice name display
    bl_label = "Base custom checkable node socket"
      
    def draw(self, context, layout, node, text):
        if self.is_linked:
            layout.label(text=text)
        else:
            if self.advanced:
                layout = layout.box()
            col = layout.column(align=True)
            split = col.split(factor=0.2)
            split.prop(self, "activated", text="use")
            column = split.column(align=True)
            column.enabled = getattr(self, "activated")
            column.prop(self, "value", text=text)
      
    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


class ProkitekturaCheckedSocketMixIn():
    '''See class ProkitekturaCheckedSocketBase'''
    
    activated: bpy.props.BoolProperty(name = "Activated", description = "activated", default = True)
    
    python: bpy.props.StringProperty(name = "Python", description = "python code", default = "")
    
    advanced: bpy.props.BoolProperty(name = "Advanced", description = "advanced", default = False)
    
class ProkitekturaCheckedSocketIntUnsigned(ProkitekturaCheckedSocketMixIn, ProkitekturaCheckedSocketBase):
    # Description string
    """
    A custom node socket type for unsigned integers
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaCheckedSocketIntUnsigned"
    # Label for nice name display
    bl_label = "Unsigned Integer"
    
    value: bpy.props.IntProperty(min=0, subtype='UNSIGNED')

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)

class ProkitekturaCheckedSocketFloat(ProkitekturaCheckedSocketMixIn, ProkitekturaCheckedSocketBase):
    # Description string
    """
    A custom node socket type for floats
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaCheckedSocketFloat"
    # Label for nice name display
    bl_label = "Float"
    
    value: bpy.props.FloatProperty()

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)

class ProkitekturaCheckedSocketFloatUnsigned(ProkitekturaCheckedSocketMixIn, ProkitekturaCheckedSocketBase):
    # Description string
    """
    A custom node socket type for unsigned floats
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaCheckedSocketFloatUnsigned"
    # Label for nice name display
    bl_label = "Float"
    
    value: bpy.props.FloatProperty(min=0.0)

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)

class ProkitekturaCheckedSocketColor(ProkitekturaCheckedSocketMixIn, ProkitekturaCheckedSocketBase):
    # Description string
    """
    A custom node socket type for colors
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaCheckedSocketColor"
    # Label for nice name display
    bl_label = "Color"
     
    value: bpy.props.FloatVectorProperty(
        name = "color",
        subtype='COLOR',
        default=(1.0, 1.0, 1.0),
        min=0.0, max=1.0,
        description="color picker"
    )
 
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)

class ProkitekturaCheckedSocketRoofShape(ProkitekturaCheckedSocketMixIn, ProkitekturaCheckedSocketBase):
    # Description string
    """
    A custom node socket type for the roof shapes
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaCheckedSocketRoofShape"
    # Label for nice name display
    bl_label = "Roof Shape"

    # Enum items list
    roofShapeList = (
        ("flat", "flat", "flat"),
        ("gabled", "gabled", "gabled"),
        ("hipped", "hipped", "hipped"),
        ("pyramidal", "pyramidal", "pyramidal"),
        ("skillion", "skillion", "skillion"),
        ("dome", "dome", "dome"),
        ("onion", "onion", "onion"),
        ("round", "round", "round"),
        ("half-hipped", "half-hipped", "half-hipped"),
        ("gambrel", "gambrel", "gambrel"),
        ("saltbox", "saltbox", "saltbox"),
        ("mansard", "mansard", "mansard")
    )

    value: bpy.props.EnumProperty(
        name = "Roof Shape",
        description = "Roof Shape",
        items = roofShapeList,
        default = "flat"
    )

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)

class ProkitekturaCheckedSocketWallCladding(ProkitekturaCheckedSocketMixIn, ProkitekturaCheckedSocketBase):
    """
    Node socket type for the condition for wall cladding
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaCheckedSocketWallCladding"
    # Label for nice name display
    bl_label = "Cladding"

    # Enum items list
    materialList = (
        ("brick", "brick", "brick"),
        ("plaster", "plaster", "plaster"),
        ("shiplap", "wood: ship lap", "wood: ship lap"),
        ("loglap", "wood: log lap", "wood: log lap"),
        ("log", "wood: log", "wood: log"),
        ("pvc", "PVC", "PVC")
    )

    value: bpy.props.EnumProperty(
        name = "Wall Material",
        description = "Wall Material",
        items = materialList,
        default = "brick"
    )

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)

class ProkitekturaSocketEnum(ProkitekturaCheckedSocketMixIn, ProkitekturaCheckedSocketBase):
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
 
    value: bpy.props.EnumProperty(
        name="Direction",
        description="Just an example",
        items=my_items,
        default='UP',
    )
    
    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)