import bpy
from bpy.types import Menu


class PIE_MT_ParticleSubPie(Menu):
    bl_idname = "PIE_MT_ParticleSubPie"
    bl_label = "Pie Add Particle Modifiers"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        ob = context.object
        return ob and ob.type != 'GPENCIL'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        op = pie.operator("object.modifier_add", text="Cloth", icon="MOD_CLOTH")
        op.type = "CLOTH"
        op = pie.operator("object.modifier_add", text="Particle", icon="PARTICLES")
        op.type = "PARTICLE_SYSTEM"
        op = pie.operator("object.modifier_add", text="Soft Body", icon="MOD_SOFT")
        op.type = "SOFT_BODY"
        op = pie.operator("rigidbody.object_add", text="Rigid Body", icon="RIGID_BODY")


class PIE_MT_MeshSubPie(Menu):
    bl_idname = "PIE_MT_MeshSubPie"
    bl_label = "Pie Add Mesh Modifiers"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        ob = context.object
        return ob and ob.type != 'GPENCIL'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("object.custom_remesh", text="Remesh", icon="MOD_REMESH")
        pie.operator("object.custom_decimate", text="Decimate", icon="MOD_DECIM")
        op = pie.operator("object.modifier_add", text="Smooth", icon="MOD_SMOOTH")
        op.type = "SMOOTH"
        op = pie.operator("object.modifier_add", text="Wireframe", icon="MOD_WIREFRAME")
        op.type = "WIREFRAME"


class PIE_MT_AddModifier(Menu):
    bl_idname = "PIE_MT_AddModifier"
    bl_label = "Pie Add Modifier"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        ob = context.object
        return ob and ob.type != 'GPENCIL'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # Left -- Mirror
        pie = layout.menu_pie()
        box = pie.split().column()
        op = box.operator('object.custom_mirror_modifier', text="Mirror X", icon="MOD_MIRROR")
        op.mirror_type = "X"
        op = box.operator('object.custom_mirror_modifier', text="Mirror Y", icon="MOD_MIRROR")
        op.mirror_type = "Y"
        op = box.operator('object.custom_mirror_modifier', text="Mirror Z", icon="MOD_MIRROR")
        op.mirror_type = "Z"
        # Right -- Bevel / Shading
        box = pie.split().column()
        box.operator('object.custom_bevel_modifier', text="Bevel", icon="MOD_BEVEL")
        box.operator('object.custom_bevel_subsurf_modifier', text="Bevel Subsurf", icon="MOD_SUBSURF")
        op = box.operator('object.modifier_add', text="Weighted Normal", icon="MOD_NORMALEDIT")
        op.type = "WEIGHTED_NORMAL"
        # Bottom -- Deform
        box = pie.split().column()
        box.operator("object.custom_simple_deform", text="Bend", icon="MOD_SIMPLEDEFORM")
        box.operator("object.custom_shrinkwrap", text="Shrinkwrap", icon="MOD_SHRINKWRAP")
        box.operator("object.custom_lattice", text="Lattice", icon="OUTLINER_DATA_LATTICE")
        # Top -- Mesh \ Edges
        box = pie.split().column()
        op = box.operator("object.array_modal", text="Array", icon="MOD_ARRAY")
        box.operator("object.custom_shrinkwrap", text="Solidify", icon="MOD_SOLIDIFY")
        box.operator("object.custom_lattice", text="Screw", icon="MOD_SCREW")
        # TL --
        op = pie.operator('wm.call_menu_pie', text="Physics", icon='PHYSICS')
        op.name = "PIE_MT_ParticleSubPie"
        # TR --
        op = pie.operator('wm.call_menu_pie', text="Mesh", icon='MOD_REMESH')
        op.name = "PIE_MT_MeshSubPie"
        # BL --
        pie.operator("object.modifier_add", text="Bottom Right", icon="MOD_CLOTH")
        # BL --
        pie.operator("object.modifier_add", text="Bottom Left", icon="MOD_CLOTH")