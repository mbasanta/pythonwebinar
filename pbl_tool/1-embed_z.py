import arcpy


def embed_z():
    xs_sorce = arcpy.GetParameterAsText(0)
    pbl_source = arcpy.GetParameterAsText(1)
    struct_source = arcpy.GetParameterAsText(2)
    wse_source = arcpy.GetParameterAsText(3)
    new_gdb = arcpy.GetParameterAsText(4)
    overwrite = arcpy.GetParameterAsText(5)

    #add a message with paramters


if __name__ == '__main__':
    embed_z()
