from . import ProkitekturaNode, ProkitekturaContainerNode


class ProkitekturaRidge(ProkitekturaNode, ProkitekturaContainerNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaRidge"
    # Label for nice name display
    bl_label = "Ridge"
    # Icon identifier
    bl_icon = 'SOUND'