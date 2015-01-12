import arcpy


def embed_z():
    xs_source = arcpy.GetParameterAsText(0)
    pbl_source = arcpy.GetParameterAsText(1)
    struct_source = arcpy.GetParameterAsText(2)
    wse_source = arcpy.GetParameterAsText(3)
    new_gdb = arcpy.GetParameterAsText(4)
    overwrite = arcpy.GetParameterAsText(5)

    arcpy.AddMessage('S_XS is: ' + xs_source)

    pbl_source_message = 'S_PROFIL_BASELN is: {0}'
    arcpy.AddMessage(pbl_source_message.format(pbl_source))

    arcpy.AddMessage('S_GEN_STRUCT is: {0}'.format(struct_source))
    arcpy.AddMessage('Water Surface is: {0}'.format(wse_source))
    arcpy.AddMessage('The new GDB is {0}, and overwrite is {1}'.format(new_gdb,
        overwrite))


if __name__ == '__main__':
    embed_z()
