import bpy
from bpy.props import FloatVectorProperty
from mathutils import Color

from ..node import ProkitekturaNode

def indent(indnt):
    return (" " * 4 * indnt)


class CodeParser():
    
    def __init__(self, tree):
        self.tree = tree

    def parse(self):
        #s tyles definition
        pycode = "styles = {\n"
        pycode += "\"" + self.tree.name + "\": ["
        comma = "\n"
    
        prokitekturaNodes = [node for node in self.tree.nodes if isinstance(node,ProkitekturaNode)]

        # find all Footprint nodes and parse them
        for node in prokitekturaNodes:
            if node.bl_idname in {'ProkitekturaFootprint'}:
                pycode += comma + self.parseNode(node, 1)
                comma = ",\n"
            
        # find all definition nodes and parse them
        for node in prokitekturaNodes:
            if node.typeDefinition == "def":
                pycode += comma + self.parseNode(node, 1)
                comma = ",\n"
                
        # find all standard nodes (out of frames) and parse them
        for node in prokitekturaNodes:
            if node.typeDefinition == "none" and node.parent is None:
                pycode += comma + self.parseNode(node, 1)
                comma = ",\n"
   
        # end of styles definition
        pycode += "\n]\n}\n"
    
        return pycode
 
    def resolveInputLink(self,socket):
        return socket.value # not yet implemented !!!!!!!!!!!!!

    def parseValue(self, value):
        if isinstance(value,str):
            return "\"" + value + "\""
        elif isinstance(value,Color):
            return "(" + str(value.r) + "," + str(value.g) + "," + str(value.b) + ")"
        else:
            return str(value)

    def parseSocketValue(self,socket):
        if socket.is_linked:
            value = resolveInputLink(socket)
        else:
            value = socket.value
        return self.parseValue(value)

    def parseMarkupNodes(self,markupSocket,indnt):
        comma = "\n"
        pycode = ""

        # find ReRoute node
        reRouteNode = markupSocket.links[0].to_node
        markupFrameNode = reRouteNode.parent
        nodesInFrame = [node for node in self.tree.nodes if node.parent == markupFrameNode and isinstance(node,ProkitekturaNode)]
        
        # sort them somwhow according position (not yet implemented)

        for node in nodesInFrame:
            pycode += comma + self.parseNode(node, indnt)
            comma = ",\n"

        return pycode

    def parseNode(self,node,indnt):
        # write node label
        pycode = indent(indnt) + node.bl_label + "("
        comma = "\n"
    
        # Definition nodes
        if node.typeDefinition == "def":
            pycode += comma + indent(indnt+1) + "defName = \"" + node.defName + "\""
            comma = ",\n"        
        
        # Use Definition nodes
        if node.typeDefinition == "usedef":
            pycode += comma + indent(indnt+1) + "use = [\"" + node.defName + "\"]"
            comma = ",\n"  
            
        if len(node.label) > 0:
            pycode += comma + indent(indnt+1) + "label = \"" + node.label + "\""
            comma = ",\n"  
    
        # parse node properties
        propList = node.propList
        if len(propList)>0:
            for entry in propList:
                if getattr(node,entry["check"]):
                    pycode += comma + indent(indnt+1) + entry["pythName"] + " = " + self.parseValue(getattr(node,entry["name"]))
                    comma = ",\n"
   
        # parse node input sockets
        socketList = node.socketList
        if len(socketList)>0:
            for entry in socketList:
                socket = [socket for socket in node.inputs if socket.name == entry["text"] ][0]
                if socket.activated:                
                    pycode += comma + indent(indnt+1) + entry["pythName"] + " = " + self.parseSocketValue(socket)
                    comma = ",\n"
                
        # process markup, if linked
        markupSocket = [outnode for outnode in node.outputs if outnode.is_output and outnode.bl_idname in {'ProkitekturaSocketMarkup'}][0]
        if markupSocket.is_linked:
            pycode += comma + indent(indnt+1) + "markup = ["
            comma = "\n"
            pycode += self.parseMarkupNodes(markupSocket,indnt+2)
            pycode += "\n" + indent(indnt+1) + "]"
   
        pycode += "\n" + indent(indnt) + ")"
        return pycode


