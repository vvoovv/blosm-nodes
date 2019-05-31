import bpy
import math

_frameNodeOffset = (-10, 10)
_rerouteOffset = (-20, 0)


class ProkitekturaOpCreateMarkup(bpy.types.Operator):
    """Create a markup out of selected nodes for the active node"""
    bl_idname = "prokitektura.create_markup"  # important since its how bpy.ops.blender_osm.import_data is constructed
    bl_label = "Create a markup out of selected nodes for the active node"
    bl_description = "Create a markup out of selected nodes for the active node"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # validation 
        nodes = context.space_data.edit_tree.nodes
        parentNode = nodes.active
        if not parentNode:
            self._standardErrorReport()
            return {'CANCELLED'}
        if parentNode.bl_idname in ('NodeFrame', 'NodeReroute'):
            self.report({'ERROR'}, "The parent item for the markup must be a node. Select it the last one.")
            return {'CANCELLED'}
        markupNodes = [
            node for node in nodes if
            node.select and not node.parent and node != nodes.active and
            not node.bl_idname in ('NodeFrame', 'NodeReroute')
        ]
        if not markupNodes:
            self._standardErrorReport()
            return {'CANCELLED'}
        
        # Frame node for the markup items
        frameNode = nodes.new('NodeFrame')
        frameNode.label = "markup"
        frameNode.select = True
        
        # Reroute serving as a kind of socket for the <frameNode>
        reroute = nodes.new('NodeReroute')
        reroute.select = False
        
        # calculate location and vertical dimension for the <frameNode>: top, left, bottom
        t, l, b = -math.inf, math.inf, math.inf
        for node in markupNodes:
            _l, _t = node.location
            _b = _t - node.dimensions[1]
            if _l < l:
                l = _l
            if _t > t:
                t = _t
            if _b < b:
                b = _b
        frameNode.location = (l + _frameNodeOffset[0], t + _frameNodeOffset[1])
        reroute.location = (l + _rerouteOffset[0], b + _rerouteOffset[1])
        
        # create a link from <frameNode> to <reroute>
        context.space_data.edit_tree.links.new(parentNode.outputs["markup"], reroute.inputs[0])
        reroute.parent = frameNode
        for node in markupNodes:
            node.parent = frameNode
            node.select = False
        parentNode.select = False
        nodes.active = frameNode
        return {'FINISHED'}
    
    def _standardErrorReport(self):
        self.report({'ERROR'},
            "Select the parent node and at least one node as the markup member. " +
            "The parent node must be selected the last one. " +
            "The markup nodes can not be part of existing markup."
        )


def menu_func_markup(self, context):
    self.layout.operator(ProkitekturaOpCreateMarkup.bl_idname, text="Markup")

def menu_func_create_markup(self, context):
    self.layout.operator(ProkitekturaOpCreateMarkup.bl_idname, text="Create Markup")