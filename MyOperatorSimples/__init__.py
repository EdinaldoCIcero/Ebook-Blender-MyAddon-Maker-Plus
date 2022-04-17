bl_info = {
    "name"          : "AddonSimples",
    "author"        : "Edinaldo Cicero",
    "version"       : (0, 1),                        
    "blender"       : (2, 75, 0),                   
    "location"      : "View3D > Tools > AddonSimples",              
    "description"   : "Meu proprio Addon",          
    "warning"       : "",                           
    "wiki_url"      : "",                           
    "category"      : "Game Engine",                    
    }


import bpy
from . MyOperatorSimple import *



def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(SimpleOperator)
    

def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    bpy.utils.unregister_class(SimpleOperator)
    
    
    
if __name__ == "__main__":
    register()
    
    
