import bpy
from bpy.types import NodeTree

from .socket import ProkitekturaSocketMarkup, ProkitekturaSocketDefs, ProkitekturaSocketCondition,\
    ProkitekturaSocketWallCladding

from .node.footprint import ProkitekturaFootprint,\
    ProkitekturaSocketRoofShape, ProkitekturaSocketFacades, ProkitekturaSocketRoofSides

from .node.facade import ProkitekturaFacade,\
    ProkitekturaSocketFootprint, ProkitekturaSocketLevelsDivs
    
from .node.div import ProkitekturaDiv
from .node.level import ProkitekturaLevel
from .node.basement import ProkitekturaBasement

from .node.random_choice import ProkitekturaRandomChoice


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
    ProkitekturaNodeCategory('SOMENODES', "Some Nodes", items=[
        # our basic node
        NodeItem("ProkitekturaFootprint"),
        NodeItem("ProkitekturaFacade"),
        NodeItem("ProkitekturaDiv"),
        NodeItem("ProkitekturaLevel"),
        NodeItem("ProkitekturaBasement"),
        NodeItem("ProkitekturaRandomChoice")
    ]),
    ProkitekturaNodeCategory('OTHERNODES', "Other Nodes", items=[
        # the node item can have additional settings,
        # which are applied to new nodes
        # NB: settings values are stored as string expressions,
        # for this reason they should be converted to strings using repr()
        NodeItem("ProkitekturaFootprint", label="Node A", settings={
            "my_string_prop": repr("Lorem ipsum dolor sit amet"),
            "my_float_prop": repr(1.0),
        }),
        NodeItem("ProkitekturaNode", label="Node B", settings={
            "my_string_prop": repr("consectetur adipisicing elit"),
            "my_float_prop": repr(2.0),
        }),
    ]),
]


classes = (
    ProkitekturaNodeTree,
    ProkitekturaSocketMarkup,
    ProkitekturaSocketDefs,
    ProkitekturaSocketCondition,
    # Footprint
    ProkitekturaSocketRoofShape,
    ProkitekturaSocketFacades,
    ProkitekturaSocketRoofSides,
    ProkitekturaFootprint,
    # Facade
    ProkitekturaSocketFootprint,
    ProkitekturaSocketLevelsDivs,
    ProkitekturaSocketWallCladding,
    ProkitekturaFacade,
    # Div
    ProkitekturaDiv,
    # Level
    ProkitekturaLevel,
    # Basement
    ProkitekturaBasement,
    # Random Choice
    ProkitekturaRandomChoice
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    nodeitems_utils.register_node_categories('CUSTOM_NODES', node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories('CUSTOM_NODES')

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__main__":
    register()
