# 5. Geoprocessing to embed z values

## Intersect XS and Structures with PBL

- Look up help for intersect function
- [Intersect Tool](http://resources.arcgis.com/en/help/main/10.1/index.html#//00080000000p000000)
- It's the same as the toolbox tool

```python
XS_INTERSECT = 'xs_intersect'
STRUCT_INTERSECT = 'struct_intersect'

arcpy.AddMessage('Intersecting elevations...')
arcpy.Intersect_analysis([S_XS, S_PROFIL_BASLN], XS_INTERSECT, 'ALL', '', 'POINT')
arcpy.Intersect_analysis([S_XS, S_GEN_STRUCT], STRUCT_INTERSECT, 'ALL', '', 'POINT')
arcpy.AddMessage('Done intersecting elevations.')
```

- Let's also set the workspace

```python
arcpy.env.workspace = new_gdb
```

## Split PBL at points

- [Split Line at Points](http://resources.arcgis.com/en/help/main/10.1/index.html#/Split_Line_At_Point/00170000003w000000/)

## Convert vertices to points

- [Feature vertices to points](http://resources.arcgis.com/en/help/main/10.1/index.html#/Feature_Vertices_To_Points/00170000003p000000/)
