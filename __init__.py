import bpy
from bpy.types import NodeTree

from .operator import ProkitekturaOpCreateMarkup

from .socket import ProkitekturaSocketMarkup, ProkitekturaSocketCondition, ProkitekturaSocketWallCladding

from .node.footprint import ProkitekturaFootprint, ProkitekturaSocketRoofShape

from .node.facade import ProkitekturaFacade
    
from .node.div import ProkitekturaDiv
from .node.level import ProkitekturaLevel
from .node.roof_side import ProkitekturaRoofSide
from .node.basement import ProkitekturaBasement

from .node.random_choice import ProkitekturaRandomChoice

from .node.window import ProkitekturaWindow

from .node.balcony import ProkitekturaBalcony

from .node.door import ProkitekturaDoor

from .node.dormer import ProkitekturaDormer

from .node.ridge import ProkitekturaRidge

from .node.chimney import ProkitekturaChimney

from .node.demoNode import ProkitekturaDemoAdvancedAttr, ProkitekturaSocketEnum



### Node Categories ###
# Node categories are a python system for automatically
# extending the Add menu, toolbar panels and search operator.
# For more examples see release/scripts/startup/nodeitems_builtins.py
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem


# Derived from the NodeTree base type, similar to Menu, Operator, Panel, etc.
class ProkitekturaNodeTree(NodeTree):
    # Description string
    """A custom node tree type that will show up in the node editor header"""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = "ProkitekturaNodeTree"
    # Label for nice name display
    bl_label = "Prokitektura nodes"
    # Icon identifier
    bl_icon = 'NODETREE'


# our own base class with an appropriate poll function,
# so the categories only show up in our own tree type


class ProkitekturaNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'ProkitekturaNodeTree'


# all categories in a list
node_categories = [
    # identifier, label, items list
    ProkitekturaNodeCategory("BASEITEMS", "Base Nodes", items=[
        # our basic node
        NodeItem("ProkitekturaFootprint"),
        NodeItem("ProkitekturaFacade"),
        NodeItem("ProkitekturaDiv", label="Div"),
        NodeItem("ProkitekturaLevel"),
        NodeItem("ProkitekturaBasement"),
        NodeItem("ProkitekturaRandomChoice"),
        NodeItem("ProkitekturaDemoAdvancedAttr")
    ]),
    ProkitekturaNodeCategory("WINDOWS", "Windows", items=[
        # the node item can have additional settings,
        # which are applied to new nodes
        # NB: settings values are stored as string expressions,
        # for this reason they should be converted to strings using repr()
        NodeItem(
            "ProkitekturaWindow",
            label="1 panel 80x100",
            settings = {
                "width": repr(0.8),
                "height": repr(1.),
                "panelsRow1": repr(1)
            }
        ),
        NodeItem(
            "ProkitekturaWindow",
            label="2 panels 120x110",
            settings = {
                "width": repr(1.2),
                "height": repr(1.1),
                "panelsRow1": repr(2)
            }
        ),
        NodeItem(
            "ProkitekturaWindow",
            label="3 panels 180x110",
            settings = {
                "width": repr(1.8),
                "height": repr(1.1),
                "panelsRow1": repr(3)
            }
        ),
        NodeItem(
            "ProkitekturaWindow",
            label="2 panels 180x210",
            settings = {
                "width": repr(1.8),
                "height": repr(2.1),
                "panelsRow1": repr(2)
            }
        ),
        NodeItem(
            "ProkitekturaWindow",
            label="3 panels 180x210",
            settings = {
                "width": repr(1.8),
                "height": repr(2.1),
                "panelsRow1": repr(3)
            }
        ),
        NodeItem(
            "ProkitekturaWindow",
            label="roof window",
            settings = {
                "width": repr(0.8),
                "height": repr(1.),
                "panelsRow1": repr(1)
            }
        )
    ]),
    ProkitekturaNodeCategory("DOORS", "Doors", items=[
        NodeItem("ProkitekturaDoor")
    ]),
    ProkitekturaNodeCategory("BALCONIES", "Balconies", items=[
        NodeItem("ProkitekturaBalcony")
    ]),
    ProkitekturaNodeCategory("ROOFITEMS", "Roof Items", items=[
        NodeItem("ProkitekturaRoofSide"),
        NodeItem("ProkitekturaRidge"),
        NodeItem("ProkitekturaDormer"),
        NodeItem("ProkitekturaChimney")
    ]),
    ProkitekturaNodeCategory("AUX", "Auxiliary elements", items=[
        NodeItem("NodeReroute"),
        NodeItem("NodeFrame"),
        ProkitekturaNodeCategory("MARKUP", "Markup", items=[
            NodeItem("NodeReroute"),
            NodeItem("NodeFrame")
        ])
    ])   
]


classes = (
    # operators
    ProkitekturaOpCreateMarkup,
    
    # node stuff
    ProkitekturaNodeTree,
    
    ProkitekturaSocketMarkup,
    ProkitekturaSocketCondition,
    # Footprint
    ProkitekturaSocketRoofShape,
    ProkitekturaFootprint,
    # Facade
    ProkitekturaSocketWallCladding,
    ProkitekturaFacade,
    # Div
    ProkitekturaDiv,
    # Level
    ProkitekturaLevel,
    # Roof Side
    ProkitekturaRoofSide,
    # Basement
    ProkitekturaBasement,
    # Random Choice
    ProkitekturaRandomChoice,
    # Window
    ProkitekturaWindow,
    # Balcony
    ProkitekturaBalcony,
    # Door
    ProkitekturaDoor,
    # Dormer
    ProkitekturaDormer,
    # Ridge
    ProkitekturaRidge,
    # Chimney
    ProkitekturaChimney,
    ProkitekturaDemoAdvancedAttr,
    ProkitekturaSocketEnum
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    nodeitems_utils.register_node_categories('PROKITEKTURA_NODES', node_categories)
    bpy.types.Scene.prop_group = PointerProperty(type=Group)



def unregister():
    nodeitems_utils.unregister_node_categories('PROKITEKTURA_NODES')

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.prop_group


if __name__ == "__main__":
    register()
