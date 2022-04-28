import bpy
from bpy.types import Menu


class PIE_MT_AddOtherObjects(Menu):
    bl_idname = "PIE_MT_AddOtherObjects"
    bl_label = "Pie Add Other Objects"
    bl_options = {"REGISTER", "UNDO"}

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # Left -- Lights
        pie.operator_menu_enum("object.light_add", "type")
        # Right -- Camera
        pie.operator("object.smart_add_camera", text="Add Camera", icon="CAMERA_DATA")
        # Bottom -- Light Probe
        pie.operator_menu_enum("object.lightprobe_add", "type")
        # Top -- Smart Lattice
        pie.operator("object.smart_add_lattice", text="Smart Lattice", icon="LATTICE_DATA")
        # Text
        pie.operator("object.text_add", text="Text", icon="SMALL_CAPS")
        # Text
        pie.operator("mesh.primitive_mannequin_add", text="Mannequin", icon="OUTLINER_OB_ARMATURE")