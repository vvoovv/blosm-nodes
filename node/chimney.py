from . import ProkitekturaNode


class ProkitekturaChimney(ProkitekturaNode):
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaChimney"
    # Label for nice name display
    bl_label = "Chimney"
    # Icon identifier
    bl_icon = 'SOUND'