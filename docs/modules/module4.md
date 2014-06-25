# 4. Python Language Basics

## Help

- Google
- [docs.python.org](http://docs.python.org)
- Start Menu > All Programs > ArcGis > Python 2.7 > Python Manuals

## Data Types

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

## Numbers

### Start with a demo

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

### Integers

- Anything without a decimal
- Don't worry about integer vs long integer in Python

### Float

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

## Sequences

### List

### Tuple

### Strings

- String are a sequence of characters
    - Common sequence fuctions will work with strings
- Quotation Concepts and New Line Concepts
    - Can be specified using single or double quotes
    - Escape sequences 
    - Defining a raw string (r"blah blah blah")
    - Defining a new line
- Demo

```pycon
    >>> print 'I'll be back'
    SyntaxError: invalid syntax
    >>> print 'I\'ll be back'
    I'll be back
    >>> print "I'll be back"
    I'll be back
    >>> print 'C:\Python27\newPath\path\path'
    C:\Python27
    ewPath\path\path
    >>> r'C:\Python27\newPath\path\path'
    C:\Python27\newPath\path\path
    >>>
```

## Dictionaries

