
import bpy


def main(context):
    for ob in context.scene.objects:
        print(ob)
        


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label  = "Simple Object Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}




class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties VIEW_3D-TOOLS"""
    
    bl_label        = "Hello World Panel"
    bl_idname       = "OBJECT_PT_hello"
    bl_space_type   = 'VIEW_3D'
    bl_region_type  = 'TOOLS'
    
    
    def draw(self, context):
        layout = self.layout

        obj = context.object

        split = layout.split()
        col   = split.column( align=True )
        
        
        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        
        row = layout.row()
        row.prop( obj, "name" )

        row = layout.row()
        row.operator( "mesh.primitive_cube_add" , icon='OBJECT_DATA')
        
        row = layout.row()
        row.operator( "object.simple_operator" , icon='CONSOLE')
