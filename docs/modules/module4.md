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
    >>> 17 / 4
    4
    >>> 18 / 4
    4
    >>> 17 % 4
    1
    >>> 18 % 4
    2
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

```pycon
    >>> l1 = [1, 2, 3, 4, 5]
    >>> l1[0]
    1
    >>> l1[4]
    5
    >>> l2 = ['one', 'two', 'three', 'four']
    >>> l2[3]
    'four'
    >>> l2[3] = 4
    >>> l2
    ['one', 'two', 'three', 4]
    >>>
```

### Tuple

```pycon
    >>> t1 = (1,2,3)
    >>> t1[0]
    1
    >>> t1[2] = 30

    Traceback (most recent call last):
      File "<pyshell#29>", line 1, in <module>
        t1[2] = 30
    TypeError: 'tuple' object does not support item assignment
    >>> 
```

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

```pycon
    >>> d1 = {'one':1, 'two':2, 'three':3}
    >>> d1['three']
    3
    >>> d1['two'] = 'dos'
    >>> d1
    {'three': 3, 'two': 'dos', 'one': 1}
    >>> 
```
