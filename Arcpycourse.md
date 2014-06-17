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

- Open Python Window

```pycon
    >>> x, y, z = 1, 2, 3
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

## 4. Python Language Syntax
