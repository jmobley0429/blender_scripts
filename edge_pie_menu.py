import bpy
from bpy.types import Menu
import pprint


class PIE_MT_edge_menu(Menu):
    # label is displayed at the center of the pie menu.
    bl_idname = "PIE_MT_edge_menu"
    bl_label = "Edge Menu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # Left
        col = pie.split().column()
        op = col.operator("mesh.mark_seam")
        op.clear = False
        op = col.operator("mesh.mark_seam", text="Clear Seam")
        op.clear = True
        col.operator("mesh.boundary_to_seam", text="Boundary to Seam")
        # Right
        col = pie.split().column()
        col.operator("transform.edge_bevelweight", text="Set Bevel Weight").value = 1
        col.operator("transform.edge_bevelweight", text="Clear Bevel Weight").value = -1
        # Bottom

        bx = pie.split().box()
        bx.label(text="Select Edges")
        bx.ui_units_y -= 50
        col = bx.column()
        col.operator("mesh.loop_multi_select", text="Edge Rings").ring = True
        col.operator("mesh.loop_multi_select", text="Edge Loops").ring = False
        col.operator("mesh.select_nth")
        # Top
        bx = pie.split().box()
        bx.label(text="Select")
        col = bx.column()
        col.operator("mesh.edges_select_sharp", text="Sharp Edges")
        col.operator("mesh.loop_to_region", text="Inner Region")
        col.operator("mesh.region_to_loop", text="Boundary Loop")
        #
        col = pie.split().column()
        col.operator("mesh.mark_sharp")
        col.operator("mesh.mark_sharp").clear = True
        #
        col = pie.split().column()
        col.operator("mesh.bridge_edge_loops")
        col.operator("mesh.subdivide")
        #
        # Right
        col = pie.split().column()
        col.operator("transform.edge_crease", text="Set Crease").value = 1
        col.operator("transform.edge_crease", text="Clear Crease").value = -1
        # Bottom
        col = pie.split().column()
        col.operator("mesh.edge_rotate", text="Rotate CW").use_ccw = False
        col.operator("mesh.edge_rotate", text="Rotate CCW").use_ccw = True