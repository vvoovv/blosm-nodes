import bpy
from bpy.types import NodeSocket
from _testcapi import the_number_three


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


class ProkitekturaSocketWallCladding(NodeSocket):
    """
    Node socket type for the condition for wall cladding
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaSocketWallCladding"
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

    material: bpy.props.EnumProperty(
        name = "Wall Material",
        description = "Wall Material",
        items = materialList,
        default = "brick"
    )

    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "material", text=text)

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
            col = layout.column(align=True)
            row = col.row(align=True)
            row.prop(self, "activated", text="use")
            column = row.column(align=True)
            column.enabled = getattr(self, "activated")
            column.prop(self, "value", text=text)
      
    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)
    
class ProkitekturaCheckedSocketMixIn():
    '''See class ProkitekturaCheckedSocketBase'''
    activated: bpy.props.BoolProperty(name = "Activated", description = "activated", default = True)
    python: bpy.props.StringProperty(name = "Python", description = "python code", default = "")

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
    

