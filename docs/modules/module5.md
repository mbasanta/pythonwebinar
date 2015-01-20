# 5. Set up embed z values

## Create gdb and copy necessary files over

### Start out creating the python file

- Use help as needed

```python
def embed_z():
    pass

if __name__ == '__main__':
    embed_z()
```

```python
def embed_z():
    xs_sorce = arcpy.GetParameterAsText(0)
    pbl_source = arcpy.GetParameterAsText(1)
    struct_source = arcpy.GetParameterAsText(2)
    wse_source = arcpy.GetParameterAsText(3)
    new_gdb = arcpy.GetParameterAsText(4)
    overwrite = arcpy.GetParameterAsText(5)
```


```python
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
```

### Set up as toolbox tool

- Create Toolbox
- Add Toolbox
- Add... Script...

### Copy files over

- Create GDB
- Copy features
- Check out extensions
- Trap extension errors [http://resources.arcgis.com/en/help/main/10.1/index.html#/CheckOutExtension/018v0000001n000000/](http://resources.arcgis.com/en/help/main/10.1/index.html#/CheckOutExtension/018v0000001n000000/)

```python
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
    arcpy.Copy_management(xs_source, os.path.join(new_gdb, S_XS))
    arcpy.Copy_management(pbl_source, os.path.join(new_gdb, S_PROFIL_BASLN))
    arcpy.Copy_management(struct_source, os.path.join(new_gdb, S_GEN_STRUCT))
    arcpy.CopyTin_3d(wse_source, os.path.join(gdb_path, WSE))
    arcpy.AddMessage('Done copying features.')

    arcpy.CheckInExtension('3D')


if __name__ == '__main__':
    embed_z()
```
