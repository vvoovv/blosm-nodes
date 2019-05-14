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