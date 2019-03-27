import bpy
from bpy.types import NodeSocket


class ProkitekturaSocketMarkup(NodeSocket):
    """
    Node socket type to start a markup definition.
    All markup items must be connected in the following way:
        * the output socket "next" is linked to the input socket "previous";
        * the input socket "previous" of the first markup item is linked
            to the output socket "markup" of the parent item for the markup items
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaSocketMarkup"
    # Label for nice name display
    bl_label = "Markup"

    markup: bpy.props.IntProperty(
        name = "markup",
        description = "An output socket to tart a markup definition inside some elements",
        default = 1
    )

    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        layout.label(text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


class ProkitekturaSocketMarkupItem(NodeSocket):
    """
    Node socket type for a markup item.
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaSocketMarkupItem"
    # Label for nice name display
    bl_label = "Markup Item"

    markup: bpy.props.IntProperty(
        name = "markup",
        description = "A socket to connect neighbor markup items",
        default = 1
    )

    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        if self.is_linked and not self.is_output:
            if isinstance(self.links[0].from_socket, ProkitekturaSocketMarkup):
                layout.label(text="markup")
            else:
                layout.label(text="previous")
        else:
            layout.label(text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


class ProkitekturaSocketDefs(NodeSocket):
    """
    Node socket type for style definitions inside an element
    """
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaSocketDefs"
    # Label for nice name display
    bl_label = "Definitions"

    definitions: bpy.props.StringProperty(
        name = "definitions",
        description = "Style definitions for children elements",
        default = ''
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

    definitions: bpy.props.IntProperty(
        name = "condition",
        description = "Condition for an element style",
        default = 1
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