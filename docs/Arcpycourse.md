# Python Course

## 1. Geoprocessing and Modelbuilder

### Toolbox

- Majority of ArcGIS functionality is contained here
- Manipulate and process data
- Extensive functionality
- Not neccesarily user friendly or intuitive
    - Each tool is an individual action
    - Often must use multiple tools to accomplish task
    - Repeat the same action on multiple similar datasets
    - Leads us to...

### ModelBuilder

- Drag and Drop interface for automating Toolbox
- Save as new tool in Toolbox
- Export to Python Script

### Demo

- ModelBuilder
- Convert Model to Script
- Geoprocessing from the Python window
- Geoprocessing from a stand along script


## 2. Intro to Python

### What is Python

- Multipurpose language
    - Scripting
    - Object Oriented Programming
- 2.x vs 3.x
- Capabilities
    - Django
    - Dropbox
    - YouTube
    - Dropbox
    - EventBrite
- _NOT_ ArcObjects
    - ArcObjects is the term for the Software Development Kit (SDK)
        - .NET SDK
        - Java SDK
    - Provides access to the geoprocessing capabilities of ArcGIS at
      a programatic level

### Python and ArcGIS

- Evolution from VBA
- ArcObjects, .NET SDK vs Python
- Future of Python with ArcGIS

### Examples

- Python script in toolbox
    - AddressErrors
    - Huff Model
- Interpreter
    - ArcGIS
    - IDLE
- Text editor
    - Notepad++
    - IDLE
- IDE
    - [PythonWin](http://sourceforge.net/projects/pywin32/)
    - [PyScripter](https://code.google.com/p/pyscripter/)
- Python Anywhere
    - [pythonanywhere.com](https://www.pythonanywhere.com/)
    - Online python interperter
    - Hosting
    - Tutorials
    - Free beginner account

## 3. ArcGIS Python Window

### Demo

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

### Objects, Values, Types

- Numbers
    - float
    - int
    - bool
- Sequences
    - String
    - Tuple
    - List
- Collections
    - Dictionary

## 4. Python Language Basics

### Help

- Google
- [docs.python.org](http://docs.python.org)
- Start Menu > All Programs > ArcGis > Python 2.7 > Python Manuals

### Data Types

- Number
    - Integer 1, 2, 3, 4
    - Float 1.2321, 0.8474, 10.0
- Sequence
    - String (sequence of characters)
    - List [1, 2, 3] _mutable_
    - Tuple (1, 2, 3) _immutable_
    - Dictionary
        - Key Value Pairs
        - `{'key': 'value', 'key': 'value'}`
        - The return value from `arcpy.GetInstallInfo()`

### Numbers

- Start with a demo

```pycon
    >>> 3 * 8
    24
    >>> 16 / 4
    4
    >>> 17 % 4
    1
    >>> 7 / 3
    2
    >>> 7 / 3.0
    2.333333333333
    >>>
```

- Integers
    - Anything without a decimal
    - Don't worry about integer vs long integer in Python
- Float
    - Floating point number (double)
    - Precision varies based on size of number

```pycon
    >>> sum = 0.0
    >>> for i in range(10):
    ...     sum += 0.1
    ...
    >>> sum
    0.99999999999
    >>> print sum
    1.0
    >>>
```

- Conversion
    - `int(17.9)`, `int(round(17.9))`
    - `float(17)`
