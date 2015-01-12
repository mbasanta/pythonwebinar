import arcpy
import os

SCRATCH_GDB = 'scratch.gdb'
S_XS = 's_xs'
S_PROFIL_BASLN = 's_profil_basln'
S_GEN_STRUCT = 's_get_struct'
WSE = 'wse'

def embed_z():
    # TODO: Check for license errors
    arcpy.CheckOutExtension('3D')
    xs_source = arcpy.GetParameterAsText(0)
    pbl_source = arcpy.GetParameterAsText(1)
    struct_source = arcpy.GetParameterAsText(2)
    wse_source = arcpy.GetParameterAsText(3)
    gdb_path = arcpy.GetParameterAsText(4)
    overwrite = arcpy.GetParameterAsText(5)

    # Set enviroment variables
    if overwrite == 'true':
        arcpy.env.overwriteOutput = True
    else:
        arcpy.env.overwriteOutput = False

    arcpy.AddMessage('Creating geodatabase...')
    arcpy.CreateFileGDB_management(gdb_path, SCRATCH_GDB)
    new_gdb = os.path.join(gdb_path, SCRATCH_GDB)
    arcpy.AddMessage('Done creating geodatabase.')

    # Copy feature classes
    arcpy.AddMessage('Copying features...')
    arcpy.Copy_management(xs_source, os.path.join(SCRATCH_GDB, S_XS))
    arcpy.Copy_management(pbl_source, os.path.join(SCRATCH_GDB, S_PROFIL_BASLN))
    arcpy.Copy_management(struct_source, os.path.join(SCRATCH_GDB, S_GEN_STRUCT))
    arcpy.CopyTin_3d(wse_source, os.path.join(SCRATCH_GDB, WSE))
    arcpy.AddMessage('Done copying features.')

    arcpy.CheckInExtension('3D')


if __name__ == '__main__':
    embed_z()
