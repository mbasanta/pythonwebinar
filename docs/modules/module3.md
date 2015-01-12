# 3. ArcGIS Python Window

## Quick Gotcha

- Indented code vs curly brackets
- Be consistent

## Demo

- Open ArcMap
- Open Python Window

```pycon
    >>> 2 * 3
    6
    >>>
```

```pycon
    >>> x = 1
    >>>  y, z = 2, 3
    >>> x + y + z
    6
    >>>
```

```pycon
    >>> x = 17
    >>> if x == 17:
    ...     print 'Correct'
    ...
    Correct
    >>>
```

```pycon
    >>> import arcpy
    >>> arcpy.GetInstallInfo()
    {'SourceDir'.....
                .....}
    >>> data = arcpy.GetInstallInfo()
    >>> print data['Version']
    10.2.2
    >>>
```

- Save Files
    - Text file (code.txt)
        - Includes prompts and output
        - More of a record of actions
    - Python file (code.py)
        - Only python code is included
        - Reusable script
- Load File
    - Run and view output
    - Notice on output of `print` statement is displayed
- Return value vs print
    - Return value is what is returned from a statement
        - For example `arcpy.GetInstallInfo()` returns a dictionary
        - We assigned that return value to `data`
        - In the console, the return value is shown after a
          statement is run
        - When the statement is run as part of a script, the return value is
          not shown
    - The `print` is used to display values to the screen in a script
